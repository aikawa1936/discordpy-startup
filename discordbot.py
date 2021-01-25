import discord
from discord.ext import commands
import asyncio
import traceback
import random
import os
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == "/hello":
        msg = message.author.mention + "さん、おはようございます！今日もよろしくお願いします。"
    await client.send_message(message.channel, msg)

client.run(token)
