import subprocess

#  @avocado.listener.on_message_event
from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import PREFIX
from __main__ import SIGNATURE

#  @avocado.listener.on_message_event
@register_command
async def fortune2(room, message):
    """Exibe uma frase talvez interessante, sem codeblocks"""

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("fortune2"):

        fortune2 = subprocess.run("fortune", capture_output=True,
                                 encoding="utf-8")\
                                 .stdout\
                                 .strip()
                                 #  .expandtabs()
                                 #  .strip()
                                 #  .replace('\n', '\n    ')\

        print(room.room_id, message)
        print(fortune2)

        notice=f"""\
{fortune2}

{SIGNATURE}
"""

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=notice,
                msgtype="m.text")
