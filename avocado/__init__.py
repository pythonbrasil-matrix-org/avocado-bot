from functools import wraps

import simplematrixbotlib as botlib

import botsecrets

PREFIX = '!'
SIGNATURE = ""

COMMAND_REGISTRY = {}
STARTUP_FUNCTION_REGISTRY = {}

def register_command(f, *args, **kwargs):

    @wraps(f)
    async def decorator(*args, **kwargs):
        return await f(*args, **kwargs)

    COMMAND_REGISTRY.update({f.__name__: f})

    return decorator

def register_startup_function(f, *args, **kwargs):

    @wraps(f)
    def decorator(*args, **kwargs):
        return f(*args, **kwargs)

    STARTUP_FUNCTION_REGISTRY.update({f.__name__: f})

    return decorator
