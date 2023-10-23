from functools import wraps

import simplematrixbotlib as botlib

import botsecrets

PREFIX = '!'
SIGNATURE = ""

COMMAND_REGISTRY = {}

def register_command(f, *args, **kwargs):

    @wraps(f)
    def decorator
