from telethon.sync import TelegramClient
import asyncio
from decouple import config

# Defining the need variables
api_id = config('API_ID') #Input your api_id here
api_hash = config('API_HASH') #Input your api_hash here

# loop = asyncio.new_event_loop()
with TelegramClient('runner', api_id, api_hash) as client:
    # group = client.get_entity('https://t.me/joinchat/AAAAAFN3WcSjlXS5rbXArQ')
    group = client.get_entity('https://t.me/joinchat/NssIYle5vhM9nkTOgkoWBg')
    members = client.get_participants(group)
    

    # Collect from text file
    with open("test.txt", "r") as file:
        data = file.readlines()

    # import pdb ; pdb.set_trace()

    clean_data = [i.strip('@') for i in data]
    cleaned = [i.strip('\n') for i in clean_data]
    # users = []
    # count = 0

    ##### check_group = client.get_entity('https://t.me/DayTradeAlerts')
    ##### users = client.get_participants(check_group)

    ##### cleaned = [i.id for i in users]

    # for i in cleaned:
    #     try:
    #         single = client.get_entity(i)
    #         users.append(single)
    #         print('good')
    #     except Exception as e:
    #         # import pdb ; pdb.set_trace()
    #         count += 1
    #         print(f"{e}")
    #         pass

    # users_id = [user.id for user in users]

    # # Collect the second party group participants
    # with open('target.txt', 'r') as file:
    #     raw_members = file.readlines()

    # clean_members = [i.strip('@') for i in raw_members]

    # members = [client.get_entity(i) for i in clean_members]

    # Make comparison
    for i in members:
        if i.username in cleaned:
            print(f"{i.username} - {i.id}")
        else:
            pass

    print("DONE")



# @jypafadisin