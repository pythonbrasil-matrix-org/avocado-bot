#!/usr/bin/env python

import subprocess

import simplematrixbotlib as botlib

import botsecrets

PREFIX = '!'
#  SIGNATURE = "*beep-bop, I'm a bot*"
SIGNATURE = ""

creds = botlib.Creds(homeserver=botsecrets.HOMESERVER,
                     username=botsecrets.USERNAME,
                     password=botsecrets.PASSWORD,
                     session_stored_file=botsecrets.SESSION_FILE)

config = botlib.Config()
config.allowlist = botsecrets.ALLOW_LIST
config.encryption_enabled = True
config.emoji_verify = True
config.ignore_unverified_devices = True
config.join_on_invite = False
config.store_path = botsecrets.CRYPTO_STORE

avocado = botlib.Bot(creds=creds, config=config)

@avocado.listener.on_message_event
async def fortune(room, message):

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("fortune"):

        fortune = subprocess.run("fortune", capture_output=True,
                                 encoding="utf-8")\
                                 .stdout\
                                 .expandtabs()\
                                 .replace('\n', '\n    ')\
                                 .strip()

        print(room.room_id, message)
        print(fortune)

        notice=f"""\
    {fortune}

{SIGNATURE}
"""

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=notice,
                msgtype="m.notice")

@avocado.listener.on_message_event
async def update(room, message):

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.is_from_allowed_user() \
            and match.prefix() and match.command("update"):

        version = subprocess.run(["git", "log",  "-n1", "--pretty=%H"],
                                 capture_output=True, encoding="utf-8") \
                                         .stdout.expandtabs().strip()

        date = subprocess.run(["git", "log",  "-n1", "--pretty=%ar"],
                              capture_output=True, encoding="utf-8") \
                                         .stdout.expandtabs().strip()

        git_stash_output = subprocess.run(["git", "stash"],
                                          capture_output=True,
                                          encoding="utf-8")\
                                          .stdout\
                                          .expandtabs()\
                                          .replace('\n', '\n    ')\
                                          .strip()

        git_pull_output = subprocess.run(["git", "pull"], capture_output=True,
                                         encoding="utf-8")\
                                         .stdout\
                                         .expandtabs()\
                                         .replace('\n', '\n    ')\
                                         .strip()

        #print(room.room_id, message)

        notice=f"""\
I'm updating:

$ git stash

    {git_stash_output}

$ git pull

    {git_pull_output}

Rebooting now... (version {version}, {date})

{SIGNATURE}
"""

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=notice,
                msgtype="m.notice")
        exit(0)

@avocado.listener.on_message_event
async def reboot(room, message):

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_from_allowed_user() and match.prefix() \
        and match.command('reboot'):

        version = subprocess.run(["git", "log",  "-n1", "--pretty=%H"],
                                 capture_output=True) \
                                         .stdout \
                                         .decode("utf-8") \
                                         .expandtabs() \
                                         .strip()

        date = subprocess.run(["git", "log",  "-n1", "--pretty=%ar"],
                              capture_output=True) \
                                         .stdout \
                                         .decode("utf-8") \
                                         .expandtabs() \
                                         .strip()


        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=f"""\
    Rebooting... (version {version}, {date})

{SIGNATURE}
""",
                msgtype="m.notice")

        #  print(room.room_id, message)

        exit(0)


@avocado.listener.on_startup
async def online_notice(room_id):
    version = subprocess.run(["git", "log",  "-n1", "--pretty=%H"],
                             capture_output=True, encoding="utf-8")\
                                     .stdout\
                                     .expandtabs() \
                                     .strip()


    date = subprocess.run(["git", "log",  "-n1", "--pretty=%ar"],
                          capture_output=True) \
                                     .stdout \
                                     .decode("utf-8") \
                                     .expandtabs() \
                                     .strip()

    await avocado.api.send_markdown_message(
        room_id=room_id,
        message=f"""\
    I'm online! (version {version}, {date})

{SIGNATURE}
""",
        msgtype="m.notice")

avocado.run()
