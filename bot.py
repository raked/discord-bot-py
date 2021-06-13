import discord
from dotenv import load_dotenv
import os

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$cornbarge'):
        i = 10
        while i > 0:
            await message.channel.send('Wake up ' + message.author)
            i = i - 1
        

client.run(TOKEN)