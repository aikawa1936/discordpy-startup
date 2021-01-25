import discord
from discord.ext import commands
import traceback
import random
import os
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print("おはようございます。今日もよろしくお願いします！")
    print(discord.__version__)

client.run(token)
