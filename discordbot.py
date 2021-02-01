# coding: UTF-8
import discord
import random
from datetime import datetime, timedelta, timezone
import os

token = os.environ.get('DISCORD_BOT_TOKEN')

# インテント設定
my_intents = discord.Intents.default()
my_intents.members = True

client = discord.Client(intents = my_intents)

# チャンネルID置き場
channel_01 = 799059509443166208 # 初めにお読みください
channel_02 = 800882842519207936 # bot-control

##時間に関する定義
today = datetime.now().strftime('%y/%m/%d')
now = datetime.now().strftime('%H:%M')

# 30秒に1度、時間情報を取得する
# ループ処理を実行する
#time_check.start()

##リマインダーの処理
#remind_list = [] # 日時格納用リスト

#@client.event
#async def remind(): # remindという名前の関数を入れる箱を作った
#    if today == '2021/02/01': # 登録した日付の
#        if now == '20:00': # 登録した時間になったら
#            channel = client.get_channel(channel_02) # このチャンネルに
#            await channel.send('時報のテストを行っていまーす！') # 登録したメッセージを送信する

##起動時の処理
@client.event
async def on_ready():
    activity = discord.Activity(name = today, type = discord.ActivityType.playing)
    await client.change_presence(activity=activity)
    print(today +' '+ now + '分、ログインしました')

##メッセージに関する処理
# 反応リスト
list01 = ['にゃーん♪', 'にゃっ！', 'にゃぁ……', 'うにゃ？'] # にゃーん返信リスト
list02 = ['わーちょっとまってー！今いそがし……あーっ！！', 'はーい♪ 何かご用事ですか？', 'さん、おはようございます♪\n今日もよろしくお願いします', '早く新しいお仕事を覚えなきゃ……！'] # メンションへの反応
list03 = ['滝上 絢椛に対するテキストコマンドのヘルプ。\n・/neko：４つのパターンでねこの鳴き真似を返します。\n・/exit（管理者のみ）：滝上 絢椛を終了します。\n・/cleanup（管理者のみ）入力したテキストチャンネルのログを全削除します。\n・/remind（未実装）：リマインダー登録します。登録方法は"/remind タイトル,yyyy/MM/dd,hh:mm,コメント"です。\n・/remind_list（未実装）：登録中のリマインダーをリストで呼び出します。'] # ヘルプコマンドの反応

# botがメンションを受け取った時の返信定義
async def reply(message):
    reply = f'{message.author.mention} ' + random.choice(list02) 
    await message.channel.send(reply)

# ヘルプコマンド
async def help(message):
    help = list03[0]
    await message.channel.send(help)

@client.event
async def on_message(message):
    # botの相手はしないようにする
    if message.author.bot:
        return
    ##管理者限定コマンド
    # 強制終了コマンド
    if message.content == '/exit':
        if message.author.guild_permissions.administrator:
            await message.channel.send('それでは帰ります。お先に失礼しまーす')
            await client.logout()
        else:
            await message.channel.send('ごめんなさい。貴方にその権限は付与されていません。')
    #ログの全削除
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.send('こちらのチャンネルのお掃除をしますね！')
            await message.channel.purge()
        else:
            await message.channel.send('ごめんなさい。貴方にその権限は付与されていません。')
    # にゃーん
    if message.content == '/neko':
        await message.channel.send(random.choice(list01))
    # メンション受信判定
    if client.user in message.mentions:
        await reply(message)
    # ヘルプ
    if message.content == '/help':
        await help(message)
    # リマインダー
    if message.content == '/reminder':
        await message.channel.send('今は概ね' + today + now + 'です。\nいつ、何をお知らせしますか？\n登録方法は"/remind タイトル,YYYY/MM/DD,hh:mm,コメント"です（未実装）')
    # リマインダーリスト表示
    if message.content == '/remind_list':
        await message.channel.send('今お預かりしているリマインダー項目は次の通りです（未実装）')

##ウェルカムメッセージの処理
@client.event
async def on_member_join(member):
    channel = client.get_channel(channel_01)
    await channel.send(f"{member.mention}さん、初めまして♪\n【こんるーそる】へようこそ！\n" + "１．まずは<#799065375924158494>をごらんください。至ってシンプルです。\n" + "２．<#796924782636826688>はみんなが読めるテキストチャンネルです。\n　　こちらに一言でもご挨拶いただけるとみんな喜びます。\n" + "３．<#796928673805762561>には各チャンネルの役割について書いています。\n" + "４．【こんるーそる】について何か意見や要望があれば<#799232703605637121>に書き込んでくださると助かります。\n" + "ご案内は以上になります。\n" + "どうぞよろしくお願いします。")

client.run(token)
