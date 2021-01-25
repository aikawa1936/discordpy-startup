from discord.ext import commands
import os
import traceback

client = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@client.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        await bot.process_commands(message)
    except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')
async def on_command_error(ctx, error):
    await ctx.send(str(error))

@client.command()
async def neko(ctx):
    await ctx.send('にゃーん')

client.run(token)
