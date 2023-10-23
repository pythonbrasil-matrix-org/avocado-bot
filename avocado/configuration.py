from . import botlib
from . import botsecrets

CONFIG = botlib.Config()
CONFIG.allowlist = botsecrets.ALLOW_LIST
CONFIG.encryption_enabled = True
CONFIG.emoji_verify = True
CONFIG.ignore_unverified_devices = True
CONFIG.join_on_invite = False
CONFIG.store_path = botsecrets.CRYPTO_STORE
