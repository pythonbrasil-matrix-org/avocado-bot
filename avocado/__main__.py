from nio import RoomMessageText

from . import register_command
from . import COMMAND_REGISTRY

from .bot import avocado

for command_name, command_function in COMMAND_REGISTRY.items():
    avocado.listener._registry.append([command_function, RoomMessageText])

avocado.run()
