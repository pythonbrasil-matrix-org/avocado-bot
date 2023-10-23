from . import botlib
from . import botsecrets

CONFIG = botlib.Config()
CONFIG.allowlist = botsecrets.ALLOW_LIST
CONFIG.encryption_enabled = True
CONFIG.emoji_verify = False
CONFIG.ignore_unverified_devices = False
CONFIG.join_on_invite = False
CONFIG.store_path = botsecrets.CRYPTO_STORE
