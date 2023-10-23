import subprocess

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
