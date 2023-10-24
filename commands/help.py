import subprocess

#  @avocado.listener.on_message_event
from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import PREFIX
from __main__ import SIGNATURE

from __main__ import COMMAND_REGISTRY

#  @avocado.listener.on_message_event
@register_command
async def help(room, message):
    """Exibe esta lista de comandos"""

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("help"):

        help = str()
        help += "    Os comandos são:\n"
        help += "    \n"

        for name, func in COMMAND_REGISTRY.items():
            help += f"    {name} - {func.__doc__ if hasattr(func, '__doc__') else ''}\n"

        print(room.room_id, message)
        print(help)

        notice=f"""\
    {help}

{SIGNATURE}
"""

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=notice,
                msgtype="m.notice")
