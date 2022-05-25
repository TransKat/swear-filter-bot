import discord
from discord import *
import json

client = discord.Client()
token = json.load(open('config.json')).get('TOKEN')
words = json.load(open('words.json')).get('WORDS')

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(ele in message.content for ele in words):
        await message.delete()
    
client.run(token)