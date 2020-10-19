from telethon.sync import TelegramClient
import asyncio
from decouple import config

# Defining the need variables
api_id = config('API_ID') #Input your api_id here
api_hash = config('API_HASH') #Input your api_hash here

# loop = asyncio.new_event_loop()
with TelegramClient('runner', api_id, api_hash) as client:
    # group = client.get_entity('https://t.me/joinchat/AAAAAFN3WcSjlXS5rbXArQ')
    group = client.get_entity('https://t.me/electrumchain_eauric')
    members = client.get_participants(group)

    # Collect from text file
    with open("test.txt", "r") as file:
        data = file.readlines()

    clean_data = [i.strip('@') for i in data]
    users = [client.get_entity(i) for i in clean_data]

    users_id = [user.id for user in users]

    # Make comparison
    for i in members:
        if i.id in users_id:
            print(f"{i.username} - {i.id}")
        else:
            pass

    print("DONE")