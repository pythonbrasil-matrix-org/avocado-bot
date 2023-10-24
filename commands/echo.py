import subprocess

#  @avocado.listener.on_message_event
from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import PREFIX
from __main__ import SIGNATURE

#  @avocado.listener.on_message_event
@register_command
async def echo(room, message):
    """Repete o que você falou, só que mais alto"""

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("echo"):

        #  text = message.body
        text = ' '.join([arg for arg in match.args])

        print(room.room_id, message)
        print(text)

        notice=f"""\
# {text}

{SIGNATURE}
"""

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=notice,
                msgtype="m.text")
