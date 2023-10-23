import subprocess

#  @avocado.listener.on_message_event
from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import PREFIX
from __main__ import SIGNATURE

@register_command
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
