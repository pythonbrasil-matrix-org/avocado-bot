from nio import RoomMessageText

from . import botlib
from . import register_command
from . import PREFIX
from . import SIGNATURE
from . import COMMAND_REGISTRY

from .bot import avocado

from commands import *

for command_name, command_function in COMMAND_REGISTRY.items():
    avocado.listener._registry.append([command_function, RoomMessageText])

avocado.run()
