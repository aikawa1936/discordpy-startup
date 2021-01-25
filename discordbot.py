# インストールした discord.py を読み込む
import discord
import os
import random

# 自分のBotのアクセストークンに置き換えてください
token = os.environ.get('DISCORD_BOT_TOKEN')

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# 返信する非同期関数を定義
async def reply(message):
    reply = f'{message.author.mention} お呼びですか？' # 返信メッセージの作成
    await message.channel.send(reply) # 返信メッセージを送信

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')
    # メンションメッセージを受信したときの処理
    if client.user in message.mentions: # 話しかけられたかの判定
        await reply(message) # 返信する非同期関数を実行

# Botの起動とDiscordサーバーへの接続
client.run(token)
