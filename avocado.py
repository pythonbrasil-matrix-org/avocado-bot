#!/usr/bin/env python

import subprocess

import simplematrixbotlib as botlib

import credentials

SIGNATURE ="*beep-bop, I'm a [bot](https://github.com/pythonbrasil-matrix-org/avocado-bot)*"
PREFIX = '!'

creds = botlib.Creds(homeserver=credentials.HOMESERVER,
                     username=credentials.USERNAME,
                     password=credentials.PASSWORD,
                     session_stored_file=credentials.SESSION_FILE)

config = botlib.Config()
config.encryption_enabled = True
config.emoji_verify = True
config.ignore_unverified_devices = False
config.join_on_invite = False
config.store_path = credentials.CRYPTO_STORE

avocado = botlib.Bot(creds=creds, config=config)

@avocado.listener.on_message_event
async def fortune(room, message):

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("fortune"):

        command = subprocess.run("fortune", capture_output=True)
        fortune = command.stdout.decode("utf-8").expandtabs()\
                                                .replace('\n', '\n    ')\
                                                .strip()

        print(room.room_id, message)

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=f"""\
    {fortune}

{SIGNATURE}
""",
                msgtype="m.notice")

avocado.run()
