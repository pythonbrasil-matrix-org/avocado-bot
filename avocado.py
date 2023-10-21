#!/usr/bin/env python

import simplematrixbotlib as botlib

import credentials

creds = botlib.Creds(credentials.HOMESERVER,
                     credentials.USERNAME,
                     credentials.PASSWORD)

avocado = botlib.Bot(creds)
