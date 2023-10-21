#!/usr/bin/env python

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

    print(room.room_id, message)

    #  await avocado.api.send_text_message(
    await avocado.api.send_markdown_message(
            room_id=room.room_id,
            message=f"`{message.body}`",
            msgtype="m.notice")
            #  msgtype="m.text")


avocado.run()
