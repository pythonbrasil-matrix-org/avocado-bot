import subprocess

from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import DATE
from __main__ import VERSION
from __main__ import PREFIX
from __main__ import SIGNATURE

@register_command
async def reboot(room, message):

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_from_allowed_user() and match.prefix() \
        and match.command('reboot'):

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=f"""\
    Rebooting... (version {VERSION}, {DATE})

{SIGNATURE}
""",
                msgtype="m.notice")

        #  print(room.room_id, message)

        exit(0)
