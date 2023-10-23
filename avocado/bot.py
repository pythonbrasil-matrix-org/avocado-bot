from . import botlib
from . import botsecrets

from .configuration import CONFIG
from .credentials import CREDS

avocado = botlib.Bot(creds=CREDS, config=CONFIG)
