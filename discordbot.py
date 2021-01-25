from discord.ext import commands
import os
import traceback
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        await bot.process_commands(message)
    except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')

@bot.command()
async def hello(ctx):
    msg = message.author.mention+'さん、こんにちは！'
    await ctx.send(message,channel,msg)

bot.run(token)
