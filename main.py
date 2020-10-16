from telethon.sync import TelegramClient, events
from telethon.tl.types import InputPeerChannel
import asyncio
from decouple import config

# Defining the need variables
api_id = config('API_ID') #Input your api_id here
api_hash = config('API_HASH') #Input your api_hash here

loop = asyncio.new_event_loop()
client = TelegramClient('runner', api_id, api_hash, loop=loop)
client.start()

channel = client.get_input_entity('https://t.me/techguided')

chat = InputPeerChannel(channel_id=channel.channel_id, access_hash=channel.access_hash) # Input channel id and access_hash

# import pdb; pdb.set_trace()
channel = client.get_entity(1270515419)

# Handler to receive the channel message
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    await client.send_message('codefred', f'{event.stringify()}')


client.add_event_handler(handler)

# Run endlessly 
client.run_until_disconnected() 