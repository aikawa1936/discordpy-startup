from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_message(message):
    try:
        if message.author.bot:    # メッセージ送信者がBotだった場合は無視する
            return
        await bot.process_commands(message)
    except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')

@bot.commands
async def neko(ctx):
    await ctx.send('にゃーん')        
        
bot.run(TOKEN)
