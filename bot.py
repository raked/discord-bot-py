import discord
import random
import math
from dotenv import load_dotenv
import os

client = discord.Client(intents=discord.Intents().all())
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
        randomMember = random.choice(message.guild.members)
        print(randomMember)
        await randomMember.move_to(None)

    if message.content.startswith(f'{prefix}fbi'):
        guild = message.author.guild
        randomNumber = random.random()
        if randomNumber <= 0.5:
            randomMember = guild.get_member(420715647128043536)
        else:
            randomMember = guild.get_member(259859886412660737)
        await randomMember.move_to(None)
        await message.channel.send('User: ' + str(randomMember) + ' was kicked from the channel.')

    if message.content.startswith(f'{prefix}bitrate'):
        ch = client.get_channel(115486192971022339)
        randomBitrate = random.random() * 64000
        if randomBitrate <= 8000:
            await ch.edit(bitrate=8000)
        else:
            await ch.edit(bitrate=randomBitrate)
            await message.channel.send('Channel bitrate set to: ' + str(math.floor(randomBitrate)))

    if message.content.startswith(f'{prefix}defbitrate'):
        ch = client.get_channel(115486192971022339)
        await ch.edit(bitrate=64000)
        await message.channel.send('Channel bitrate set to: 64000')

client.run(TOKEN)
