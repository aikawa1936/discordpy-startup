from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')


bot.run(token)
