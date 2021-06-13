import discord
import random
from dotenv import load_dotenv
import os

client = discord.Client()
prefix = '$'

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f'{prefix}hello'):
        await message.channel.send('Hello!')

    if message.content.startswith(f'{prefix}cornbarge'):
        i = 4
        while i > 0:
            await message.channel.send('Wake up ' + str(message.author))
            i = i - 1

    if message.content.startswith(f'{prefix}roulette'):
       randomMember = random.choice(discord.member.id)
       print(randomMember)
       #await randomMember.move_to(None)

client.run(TOKEN)