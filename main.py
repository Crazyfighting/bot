import discord
import keep_alive
import os
from os import system
from discord import channel
from discord import message
from discord import Color
from discord.ext import commands
import json
import random
import re as regex
import datetime
import asyncio
from discord.flags import Intents
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
from BeautifulReport import BeautifulReport
## Chrome WebDriver 需要DRIVER Manager的支援
from webdriver_manager.chrome import ChromeDriverManager
import time

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='-', intents=intents)

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


@bot.event
async def on_ready():
    status_now = discord.Status.online
    activity_now = discord.Activity(type=discord.ActivityType.playing,
                                    name="實習豬")
    await bot.change_presence(status=status_now, activity=activity_now)
    flag = 0
    channel = bot.get_channel(935457641134690324)
    await channel.send('<a:rnbw_ckrch_spning:1035443105937235998>')
    time = datetime.datetime.now().strftime('%H%M')
    num = 0
    online = []
    while bot.is_ready() and flag != 1:
        for member in channel.guild.members:
            if str(member.status
                   ) == 'online' and member.name != '油圖小精靈 なび' and flag != 1:
                online.append(member)
                num += 1
        flag = 1
    names = []
    for name in online:
        names.append(name.name)
    #print(names)
    channel = bot.get_channel(731883226527694921)


@bot.command(name='re')
async def re(ctx, *, msg):
    if ctx.message.author != bot.user:
        await ctx.message.delete()
        await ctx.send(msg)


@bot.command(name='avatar')
async def avatar(ctx):
    embed = discord.Embed(title=ctx.author.display_name, color=Color.green())
    embed.set_thumbnail(url=ctx.author.avatar_url)
    if ctx.author.activity:
        if ctx.author.activity.type == discord.ActivityType.custom:
            embed.add_field(name="狀態", value=ctx.author.activity.name)
        if ctx.author.activity.type == discord.ActivityType.playing:
            embed.add_field(name="正在玩",
                            value=ctx.author.activity.name,
                            inline=True)
        if ctx.author.activity.type == discord.ActivityType.listening:
            embed.add_field(name="正在聽",
                            value=ctx.author.activity.name,
                            inline=True)
        if ctx.author.activity.type == discord.ActivityType.watching:
            embed.add_field(name="正在觀看",
                            value=ctx.author.activity.name,
                            inline=True)
        if ctx.author.activity.type == discord.ActivityType.streaming:
            embed.add_field(name="正在直播",
                            value=ctx.author.activity.name,
                            inline=True)
            embed.add_field(name="平台", value=ctx.author.activity.platform)
    await ctx.channel.send(embed=embed)


@bot.command(name='server')
async def server(ctx):
    embed = discord.Embed(
        title="FTB Revelation",
        url=
        "https://www.curseforge.com/minecraft/modpacks/ftb-revelation/files/2778969",
        color=0xfdd872)
    embed.set_author(name="模組包生存")
    embed.set_thumbnail(
        url=
        "https://media.forgecdn.net/avatars/thumbnails/134/670/64/64/636493650464216291.png"
    )
    embed.add_field(name="IP", value="123.252.2.81:25565", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def guild(ctx):
    channel = bot.get_channel(736610658807971911)
    num = 0
    for member in channel.guild.members:
        if str(member.status) == 'online' and member.name != '油圖小精靈 なび':
            num += 1
    embed = discord.Embed(title=channel.guild.name,
                          url="https://discord.gg/ETczJAkrPE",
                          description="一群遊戲虐佬,資工領域天才的樂園",
                          color=0x17b8ee)
    embed.set_thumbnail(
        url=
        "https://memeprod.sgp1.digitaloceanspaces.com/meme/bf395c955b2b735268f32ea26392a994.png"
    )
    embed.add_field(name="作息不正常", value="#日夜顛倒 #虐 #資訊工程師 #實習豬", inline=False)
    embed.add_field(name="在線人數:", value=num, inline=True)
    await ctx.send(embed=embed)
@bot.command(name='ASMR')
async def ASMR(ctx):
  channel=ctx.channel
  count_asmr=0
  messages=await ctx.channel.history(limit=None).flatten()
  for i in messages:
      count_asmr+=i.content.count('<:ASMR:1029436791708725290>')
  send="這個頻道用了"+str(count_asmr)+"次<:ASMR:1029436791708725290>"
  await channel.send(send)
@bot.command(name='pepeclown')
async def pepeclown(ctx):
  channel=ctx.channel
  count=0
  messages=await ctx.channel.history(limit=200).flatten()
  for i in messages:
      count+=i.content.count('<:pepeclown:934997002398363738>')
  send="這個頻道最近用了"+str(count)+"次<:pepeclown:934997002398363738>"
  await channel.send(send)
@bot.command(name='LOL')
async def LOL(ctx):
    await ctx.channel.send(
                'https://media.discordapp.net/attachments/878220596561993759/933067451338457148/IMG_1665.png'
            )
@bot.command(name='draw')
async def draw(ctx, *, msg):
    channel = bot.get_channel(ctx.channel)
    if ' ' in msg:
        numberlist = msg.split(' ')
        flag = 0
        for i in range(0, int(len(numberlist) - 1)):
            if regex.search('^-?[0-9]\d*(\.\d+)?$', str(
                    numberlist[i])) != None:
                continue
            else:
                flag = 1
        if flag == 0:
            if int(numberlist[0]) > int(numberlist[1]):
                temp = numberlist[1]
                numberlist[1] = numberlist[0]
                numberlist[0] = temp
            number = random.randint(int(numberlist[0]), int(numberlist[1]))
            await ctx.send(number)
        else:
            str1 = random.choice(numberlist)
            await ctx.send(str1)
    else:
        if regex.search('^-?[0-9]\d*(\.\d+)?$', str(msg)) != None:
            if (int(msg) < 0):
                number = random.randint(int(msg), 0)
            else:
                number = random.randint(0, int(msg))
            await ctx.send(number)
        else:
            await ctx.send('只有一個選項是要抽個毛')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(736610658807971911)
    await channel.send(f'歡迎新的gay<@{member.id}>')
    
@bot.event
async def on_reaction_add(reaction, user):
  if 'noway' in reaction.emoji.name.lower():
    await reaction.clear()




@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(736610658807971911)
    await channel.send(f'<@{member.id}> 願來世再相見')


@bot.event
async def on_message(msg):
  if msg.author != bot.user and not '-' in msg.content:
    keyword = ['vt', 'VT', 'vt豚', 'VT豚', 'vt豬', 'VT豬']
    if msg.content in keyword:
      random_pic = random.choice(jdata['PIC_Vtuber'])
      await msg.channel.send(random_pic)
    if msg.content == '注意看':
      await msg.channel.send('這個男人太狠了')
    if msg.content == '狂戰':

      embed = discord.Embed(
          title="狂戰",
          url="https://www.youtube.com/channel/UCuilM7lWxp5INa3AL1Te1dQ",
          description="從沒紅過的白工youtuber",
          color=0xec3e13)
      embed.set_thumbnail(
          url=
          "http://n.sinaimg.cn/sinacn20190822ac/217/w1455h1962/20190822/776f-icqznfz7612082.jpg"
      )
      embed.add_field(name="音game頻道",
                      value="#maimai #osu! #sdvx",
                      inline=False)
      await msg.channel.send(embed=embed)

    if msg.reference is not None:
      reply = await msg.channel.fetch_message(msg.reference.message_id)
      if reply.author == bot.user:
        await msg.channel.send('電話忙線中，請稍後')

    if msg.content == 'ㄐㄐ':
      await msg.channel.send(f'<@{msg.author.id}>你好噁喔')
    if msg.content == '無量空處' or msg.content == '領域展開' or msg.content == '🤞':
      await msg.channel.send(jdata['VOID'])
    if msg.content == ':fingers_crossed:':
      await msg.channel.send(jdata['VOID'])
    if msg.content == '噁':
      await msg.channel.send(f'<@{msg.author.id}>你才噁')
    if msg.content == 'lisa' or msg.content == 'Lisa' or msg.content == 'LISA':
      await msg.channel.send('泰勞')
    if msg.content == 'LiSA':
      await msg.channel.send('鬼滅女人')
    if msg.content == '為什麼' or msg.content == '為甚麼':
      await msg.channel.send('宸仔管理員請問可以請教為什麼嗎')
    if '非洲' in msg.content:
      await msg.channel.send(
          'https://cdn.discordapp.com/attachments/727117094860095498/894163416850239549/image0.gif'
      )
    if '寒心' in msg.content or '心寒' in msg.content:
      await msg.channel.send(
          'https://media.discordapp.net/attachments/915820672134045736/981420609231781938/unknown.png'
      )
    if '喂有聲音嗎' == msg.content:
      await msg.channel.send('沒有')
    if '虐' == msg.content:
      await msg.channel.send('600')
    if '選課機器' in msg.content or '搶課' in msg.content:
      await msg.channel.send(
          'https://media.discordapp.net/attachments/1026335727509839882/1056479671644078210/image.png'
      )
    if '暈' == msg.content or '暈船' == msg.content:
      await msg.channel.send('https://imgur.com/osvlxTh')
    if 'noway' in msg.content.lower():
      await msg.delete()
    if bot.user.mentioned_in(msg):
      await msg.channel.send('咩事啊？')
    elif len(msg.stickers) != 0:
      s_name = msg.stickers[0].name
      s_name = ''.join(regex.split(r'[_\-,?]', s_name))
      print(s_name)
      if 'noway' in s_name:
        await msg.delete()
  await bot.process_commands(msg)


keep_alive.keep_alive()


try:
	bot.run(jdata['TOKEN'])
except discord.errors.HTTPException:
    print("\n\n\nBLOCKED BY RATE LIMITS\nRESTARTING NOW\n\n\n")
    system("python restarter.py")
    system('kill 1')
