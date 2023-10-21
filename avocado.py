#!/usr/bin/env python

import subprocess

import simplematrixbotlib as botlib

import credentials

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
async def echo(room, message):

    command = subprocess.run("fortune", capture_output=True)
    fortune = command.stdout.decode("utf-8").expandtabs()\
                                            .replace('\n', '\n    ')

    print(room.room_id, message)

    #  await avocado.api.send_text_message(
    await avocado.api.send_markdown_message(
            room_id=room.room_id,
            #  message=f"`{message.body}`",
            message=f"""\
    {fortune}

*beep-beep, I'm a bot*
""",
            msgtype="m.notice")
            #  msgtype="m.text")


avocado.run()
