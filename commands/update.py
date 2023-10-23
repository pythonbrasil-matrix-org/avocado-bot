import subprocess

from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import PREFIX
from __main__ import SIGNATURE

@register_command
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
