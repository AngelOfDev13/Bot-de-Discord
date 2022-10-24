

import discord
import os
from dotenv import load_dotenv
load_dotenv()
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$mlb'):
        name_player = message.content.split(' ')[1]
        search_player = requests.get(f'http://lookup-service-prod.mlb.com/json/named.search_player_all.bam?&name_part={name_player}')
        #response = search_player.json()
        print(search_player)
        await message.channel.send(search_player)
        

client.run(os.environ['TOKEN'])