from . import botlib
from . import botsecrets

CREDS = botlib.Creds(homeserver=botsecrets.HOMESERVER,
                     username=botsecrets.USERNAME,
                     password=botsecrets.PASSWORD,
                     session_stored_file=botsecrets.SESSION_FILE)

