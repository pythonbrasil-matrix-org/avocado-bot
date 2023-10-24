import subprocess

from __main__ import avocado
from __main__ import botlib
from __main__ import register_command
from __main__ import PREFIX
from __main__ import SIGNATURE

WIDE_MAP = dict((i, i + 0xFEE0) for i in range(0x21, 0x7F))
WIDE_MAP[0x20] = 0x3000


def widen(s):
    """
    Convert all ASCII characters to the full-width counterpart.

    >>> print widen('test, Foo!')
    ｔｅｓｔ，　Ｆｏｏ！
    >>>
    """
    return s.translate(WIDE_MAP)


@register_command
async def widen(room, message):
    """Converte texto normal para ＦＵＬＬＷＩＤＴＨ"""

    match = botlib.MessageMatch(room=room,
                                event=message,
                                bot=avocado,
                                prefix=PREFIX)

    if match.is_not_from_this_bot() and match.prefix() and \
        match.command("widen"):

        #  text = message.body
        text = widen(' '.join([arg for arg in match.args()]))

        print(room.room_id, message)
        print(text)

        notice=f"""\
{text}

{SIGNATURE}
"""

        await avocado.api.send_markdown_message(
                room_id=room.room_id,
                message=notice,
                msgtype="m.text")
