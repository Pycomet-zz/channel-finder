from telethon.sync import TelegramClient, events
import asyncio
import os

# Defining the need variables
api_id = os.getenv('API_ID') #Input your api_id here
api_hash = os.getenv('API_HASH') #Input your api_hash here

loop = asyncio.new_event_loop()
client = TelegramClient('runner', api_id, api_hash, loop=loop)
client.start()

channel = client.get_entity('https://t.me/DayTradingAlerts')

import pdb; pdb.set_trace()

# Handler to receive the channel message
@client.on(events.NewMessage(chats=channel, incoming=True)
async def handler(event):
    await event.reply(f'{event.stringify()}')


client.add_event_handler(handler)

# Run endlessly 
client.run_until_disconnected()