# インストールした discord.py を読み込む
from discord.ext import commands
import discord
import traceback
import os

bot = commands.Bot(command_prefix='/')
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ただいま出勤いたしましたー！')

    
# メッセージ受信時に動作する処理
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
        
# Botの起動とDiscordサーバーへの接続
bot.run(TOKEN)
