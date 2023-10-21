#!/usr/bin/env python

import subprocess

import simplematrixbotlib as botlib

import credentials

SIGNATURE = "*beep-bop, I'm a bot*"
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

        #print(room.room_id, message)

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=f"""\
    {fortune}

{SIGNATURE}
""",
                msgtype="m.notice")

@avocado.listener.on_message_event
async def update(room, message):

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("update"):

        command = subprocess.run(["git", "stash"],
                                 capture_output=True)
        git_stash_output = command.stdout.decode("utf-8").expandtabs()\
                                                .replace('\n', '\n    ')\
                                                .strip()

        command = subprocess.run(["git", "pull"],
                                 capture_output=True)

        git_pull_output = command.stdout.decode("utf-8").expandtabs()\
                                                .replace('\n', '\n    ')\
                                                .strip()

        #print(room.room_id, message)

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=f"""\
I'm updating:

$ git stash

    {git_stash_output}

$ git pull

    {git_pull_output}

Rebooting now... (version x.x.x)

{SIGNATURE}
""",
                msgtype="m.notice")
        #  await avocado.async_client.close()
        exit(0)
        #  exit(0)

@avocado.listener.on_startup
async def online_notice(room_id):
    await avocado.api.send_markdown_message(
        room_id=room_id,
        message=f"""\
    I'm online!

{SIGNATURE}
""",
        msgtype="m.notice")

avocado.run()
