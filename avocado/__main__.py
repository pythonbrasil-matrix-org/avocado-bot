import subprocess

VERSION = subprocess.run(["git", "log",  "-n1", "--pretty=%H"],
                         capture_output=True, encoding="utf-8") \
                                 .stdout.expandtabs().strip()

DATE = subprocess.run(["git", "log",  "-n1", "--pretty=%ar"],
                      capture_output=True, encoding="utf-8") \
                                 .stdout.expandtabs().strip()

from nio import RoomMessageText

from . import botlib

from . import register_command
from . import register_startup_function

from . import PREFIX
from . import SIGNATURE

from . import COMMAND_REGISTRY
from . import STARTUP_FUNCTION_REGISTRY

from .bot import avocado

from commands import *
from startup import *

for command_name, command_function in COMMAND_REGISTRY.items():
    avocado.listener._registry.append([command_function, RoomMessageText])

for startup_function_name, startup_function in\
        STARTUP_FUNCTION_REGISTRY.items():
    avocado.listener._startup_registry.append(startup_function)

avocado.run()
