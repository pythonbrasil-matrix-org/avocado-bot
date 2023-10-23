from functools import wraps

import simplematrixbotlib as botlib

import botsecrets

PREFIX = '!'
SIGNATURE = ""

COMMAND_REGISTRY = {}

def register_command(f, *args, **kwargs):

    @wraps(f)
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)

    COMMAND_REGISTRY.update({f.__name__, f})

    return decorator
