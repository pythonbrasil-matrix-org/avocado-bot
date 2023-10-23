import subprocess

from __main__ import avocado
from __main__ import botlib
from __main__ import register_startup_function
from __main__ import PREFIX
from __main__ import SIGNATURE

#  @avocado.listener.on_startup
@register_startup_function
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

