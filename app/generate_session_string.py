import os

from telethon.sync import TelegramClient
from telethon.sessions import StringSession

api_id = 7684605
api_hash = "d270d70e8d3c3ad969ea6ecb5857e30b"

with TelegramClient(StringSession(), api_id, api_hash) as client:
    print("\n" + client.session.save())
