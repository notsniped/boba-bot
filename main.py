### Modules ###
import os
import time
import random
import pickle
import os.path
import discord
import datetime
from libs.ping import mainloop
import praw
import nekos
from keep_alive import keep_alive
from random import randint
from discord.ext import commands
from discord.ext.commands import *
from discord.ext import tasks
### Modules end ###

### Startup/variables ###
ids = [
  816941773032390676,
  738290097170153472
]
bad = [
  'fuck',
  'asshole',
  'nigga',
  'nigger',
  'motherfucker',
  'fuckyou',
  'bitch',
  'cum',
  'shit',
  'dick',
  'pussy',
  'boob',
  'fucκ',
  'shiτ',
  'penis'
]
whitelist = [
  'document',
  'cucumber',
  'sussex',
  'brainfuck'
]
blacklist = [
  'gouri',
  'gauri'
]
console = False
log = False
if os.name == 'nt':
  os.system('cls')
else:
  os.system('clear')
intents = discord.Intents.all()
errHandlerVer = 'v2.4'
botVer = 'v4.1.7'
currencyVer = 'v2.5'
owner = '𝔼𝕝𝕗𝕚𝕖#7240'
homedir = os.path.expanduser("~")
client = commands.Bot(command_prefix="%", intents=intents)
global startTime
startTime = time.time()
client.remove_command('help')
reddit = praw.Reddit(client_id='_pazwWZHi9JldA',
                     client_secret='1tq1HM7UMEGIro6LlwtlmQYJ1jB4vQ',
                     user_agent='idk', check_for_async=False)
### Startup/variables end ###

### Command variables ###
beg = True
fish = True
work = True
daily = True
monthly = True
weekly = True
snipe = True
editsnipe = True
shop = True
inventory = True
buy = False
networth = True
lbin = True
ah = True
welcomer = True
theme_color = 0x00FFFF
color_success = 0x77b255
color_fail = 0xc92424
loggerHandler_path = 'botLog/log.txt'
errorHandler_path = 'botLog/errors.txt'
mainDB_path = '/pkcdatabase.pickle'
### Functions and classes ###
if os.name == 'nt':
  data_filename = homedir + mainDB_path
else:
  data_filename = "pkcdatabase.pickle"

class Data:
  def __init__(self, boba, special, xp, level):
    self.boba = boba
    self.special = special
    self.xp = xp
    self.level = level

class colors:
  cyan = '\033[96m'
  red = '\033[91m'
  green = '\033[92m'
  end = '\033[0m'

def load_data():
    if os.path.isfile(data_filename):
        with open(data_filename, "rb") as file:
            return pickle.load(file)
    else:
        return dict()

def load_member_data(member_ID):
  data = load_data()
  if member_ID not in data:
    return Data(0, 0, 0, 0)
  return data[member_ID]

def save_member_data(member_ID, member_data):
  data = load_data()
  data[member_ID] = member_data
  with open(data_filename, "wb") as file:
    pickle.dump(data, file)

def get_time():
  now = datetime.datetime.now()
  return now.strftime("%H:%M:%S")

### Functions and classes end ###

currency = True

## Events ###
@client.event
async def on_ready():
    #if os.name == 'nt':
    #  os.system('cls')
    #else:
    #  os.system('clear')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"% commands"))
    print('Bot is online')
    print('==================')
    print('------------------')
    print('Bot Info')
    print(f'Bot version: {colors.cyan}{botVer}{colors.end}')
    print(f'Error handler version: {colors.cyan}{errHandlerVer}{colors.end}')
    print(f'Currency system version: {colors.cyan}{currencyVer}{colors.end}')
    print(f'Username: {colors.green}{client.user.name}{colors.end}\nId: {colors.green}{client.user.id}{colors.end}\nDeveloper name: {colors.green}{owner}{colors.end}')
    print('==================')
    try:
      client.load_extension("cogs.Music")
      print(f'Cogs loaded: {colors.green}SUCCESS{colors.end}')
    except:
      print(f'Cogs loaded: {colors.red}FAIL{colors.end}')
    print('==================')
    print('Bot config:')
    print('------------------')
    print(f'Ping: {round(client.latency * 1000)}')
    print('------------------')
    boot = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    print(f'Startup time: {boot}')
    print('------------------')
    if bool(currency) == True:
      print(f'Currency: {colors.green}{currency}{colors.end}')
    else:
      print(f'Currency: {colors.red}{currency}{colors.end}')
    print('------------------')
    if bool(log) == True:
      print(f'Logging: {colors.green}{log}{colors.end}')
      print('------------------')
    else:
      print(f'Logging: {colors.red}{log}{colors.end}')
      print('------------------')
    if bool(console) == True:
      print(f'Console: {colors.green}{console}{colors.end}')
      print('==================')
    else:
      print(f'Console: {colors.red}{console}{colors.end}')
      print('==================')
      pass
    print('Bot admins')
    print('------------------')
    print(colors.cyan)
    for id in ids:
      print(id)
    print(colors.end)
    print('==================')
    print('System info')
    print('Running as: ' + str(os.system("whoami")))
    print('------------------')
    print('Os name: ' + str(os.name))
    print('------------------')
    print('Current working dir: ' + str(os.getcwd()))
    print('------------------')
    try:
      botpath = 'main.py'
      botsize = os.path.getsize(botpath)
      print(f'Bot file size: {botsize}b')
      print('------------------')
    except FileNotFoundError:
        if os.name == 'posix':
            try:
              print('Bot file size: ' + os.path.getsize('main.py'))
              print('------------------')
            except FileNotFoundError:
              print('Bot file size: ' + os.path.getsize(str(os.getcwd() + '/main.py')))
              print('------------------')

# Error handler #
@client.event
async def on_command_error(ctx, error):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if isinstance(error, CommandNotFound):
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at CommandNotFound. Details: This command does not exist.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}CommandNotFound{colors.end}. Details: This command does not exist. {colors.red}The user was not notified of this error. This error was logged at \'F:/bot/logs/errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, CommandOnCooldown):
        await ctx.send(f':stopwatch: No, not now! Please try again after **{str(datetime.timedelta(seconds=int(round(error.retry_after))))}**')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at CommandOnCooldown. Details: This command is currently on cooldown.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}CommandOnCooldown{colors.end}. Details: This command is currently on cooldown. {colors.red}This error was logged at \'F:/bot/logs/errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingRequiredArgument):
        await ctx.send('Your command has missing required argument(s).')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingRequiredArgument. Details: The command can\'t be executed because required arguments are missing.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}MissingRequiredArgument{colors.end}. Details: The command can\'t be executed because required arguments are missing. {colors.red}This error was logged at \'F:/bot/logs/errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, MissingPermissions):
        await ctx.send('Dood, you dont have permissions to use this command.')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at MissingPermissions. Details: The user doesn\'t have the required permissions.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}MissingPermissions{colors.end}. Details: The user doesn\'t have the required permissions. {colors.red}This error was logged at \'F:/bot/logs/errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BadArgument):
        await ctx.send('Invalid argument...')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BadArgument.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}BadArgument{colors.end}. {colors.red}This error was logged at \'F:/bot/logs/errors.txt\'{colors.end}')
        else:
            pass
    if isinstance(error, BotMissingPermissions):
        await ctx.send('Oh no, I don\'t have the required permissions to run this command...')
        if os.name == 'nt':
            with open(errorHandler_path, 'a') as f:
                f.write(f'[{current_time}] Ignoring exception at BotMissingPermissions.\n Details: The bot doesn\'t have the required permissions.\n')
                f.close()
                print(f'[{current_time}] Ignoring exception at {colors.green}BotMissingPremissions{colors.end}. Details: The bot doesn\'t have the required permissions. {colors.red}This error was logged at \'F:/bot/logs/errors.txt\'{colors.end}')
        else:
            pass
# Error handler end #

snipe_message_author = {}
snipe_message_content = {}
global dropped
dropped = {}

@client.event
async def on_message_delete(message):
    if not message.author.bot:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        channel = message.channel
        snipe_message_author[message.channel.id] = message.author
        snipe_message_content[message.channel.id] = message.content
        if bool(log) == True:
            with open(loggerHandler_path, 'a') as f:
                f.write(f'[{current_time}] Message deleted by {snipe_message_author[channel.id]}.\n   Content:{snipe_message_content[channel.id]}\n')
                f.close()
            c = client.get_channel(874167956270096434)
            em = discord.Embed(name = f"Last deleted message in <#{channel.id}>", description=f'**Deleted message content:** {snipe_message_content[channel.id]}', color=0xCF1515)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await c.send(embed = em)
        else:
            pass
    else:
        pass
    

@client.event
async def on_message_edit(message_before, message_after):
    if not message_after.author.bot:
        global author
        author = message_before.author
        channel = message_before.channel
        global before
        before = message_before.content
        global after
        after = message_after.content
        if any(x in message_after.content.lower() for x in bad):
            await message_after.delete()
            await channel.send(f'Hey {message_after.author.mention}, no bad language!')
        if bool(log) == True:
            c = client.get_channel(874167956270096434)
            em = discord.Embed(description = f"**Message before**: {message_before.content}\n**Message after**: {message_after.content}", color=0xFFBF00)
            em.set_footer(text = f"This message was edited by {message_before.author} in <#{channel.id}>")
            await c.send(embed = em)
        else:
            pass
    else:
        pass
    

@client.event
async def on_member_join(member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = member.guild.name
    guildID = member.guild.id
    if welcomer == True:
        if guildID == 874160923860955136:
            c = client.get_channel(874161322475024454)
            await c.send(f'{member.mention}')
            embedWelcome = discord.Embed(title=f'Welcome to {guild}, {member}!', description='Pls go through the <#879001663644500029> and <#874161448346066985> section :)')
            embedWelcome.set_footer(icon_url=member.guild.icon_url, text=f'And thank you for bringing us to {member.guild.member_count} members :>')
            await c.send(embed = embedWelcome)
        else:
            pass
    else:
        pass
    if bool(log) == True:
        if os.name == 'nt':
            print(f'[{current_time}] {colors.cyan}{member}{colors.end} joined {colors.green}{guild}{colors.end}')
            try:
                with open(loggerHandler_path, 'a') as f:
                    f.write(f'[{current_time}] {member} joined {guild}\n')
                    f.close()
            except:
                print(f'[{current_time}] Ignoring exception at {colors.green}UnableToLog{colors.end}. {colors.red}This error was logged at /logs/errors.txt{colors.end}')
        else:
            pass
    else:
        pass

@client.event
async def on_member_remove(member):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    guild = member.guild.name
    if bool(log) == True:
        if os.name == 'nt':
            print(f'[{current_time}] {colors.cyan}{member}{colors.end} left {colors.green}{guild}{colors.end}')
            try:
                with open(loggerHandler_path, 'a') as f:
                    f.write(f'[{current_time}] {member} left {guild}\n')
                    f.close()
            except:
                print(f'[{current_time}] Ignoring exception at {colors.green}UnableToLog{colors.end}. {colors.red}This error was logged at /logs/errors.txt{colors.end}')
        else:
            pass
    else:
        pass

@client.event
async def on_message(message):
    if message.guild.id not in dropped:
      dropped[message.guild.id] = None
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f'[{current_time}] {colors.cyan}{message.author.display_name}{colors.end} messaged in {colors.green}{message.guild.name} <#{message.channel.name}>{colors.end}: {message.content}')
    if not message.author.bot:
        if any(x in message.content.lower() for x in whitelist):
            pass
        elif any(x in message.content.lower() for x in blacklist):
            try:
                await message.delete()
            except discord.errors.NotFound:
                print(f'{colors.red}Error: Failed to delete message.{colors.end} Description: Message couldn\'t be found.')
        elif any(x in message.content.lower() for x in bad):
            try:
                await message.delete()
            except discord.errors.NotFound:
                print(f'{colors.red}Error: Failed to delete message.{colors.end} Description: Message couldn\'t be found.')
            await message.channel.send(f'Hey {message.author.mention}, no bad language!', delete_after=5)
        else:
            pass
    else:
        pass
    if '<@!912353042718924860>' in message.content:
        await message.channel.send(f'{message.author.mention}, my prefix is `%` .__.')
    else:
        pass
    if not message.author.bot:
        member_data = load_member_data(message.author.id)
        member_data.xp += randint(1, 5)
        if message.guild.id == 874160923860955136:
                channel_id = client.get_channel(912009910663909407)
                if member_data.level == 0:
                    if member_data.xp >= 25:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 1:
                    if member_data.xp >= 50:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 2:
                    if member_data.xp >= 100:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 3:
                    if member_data.xp >= 500:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 4:
                    if member_data.xp >= 750:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 5:
                    if member_data.xp >= 1000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 6:
                    if member_data.xp >= 1200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 7:
                    if member_data.xp >= 1400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 8:
                    if member_data.xp >= 1600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 9:
                    if member_data.xp >= 1800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 10:
                    if member_data.xp >= 2000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 11:
                    if member_data.xp >= 2200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 12:
                    if member_data.xp >= 2400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 13:
                    if member_data.xp >= 2600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 14:
                    if member_data.xp >= 2800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 15:
                    if member_data.xp >= 3000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 16:
                    if member_data.xp >= 3200:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 17:
                    if member_data.xp >= 3400:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 18:
                    if member_data.xp >= 3600:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level == 19:
                    if member_data.xp >= 3800:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                elif member_data.level >= 20:
                    if member_data.xp >= 4000:
                        member_data.xp -= member_data.xp
                        member_data.level += 1
                        await channel_id.send(f"<@{message.author.id}>, you are now level **{member_data.level}**! To view your level, type `%level` or `%rank`")
                    else:
                        pass
                else:
                    pass
                save_member_data(message.author.id, member_data)
        else:
            pass
    else:
        pass
    await client.process_commands(message)

### Events end ###

### Commands ###

@client.command(aliases=['xp', 'level', 'lvl', 'experience', 'exp'])
async def rank(ctx, user:discord.User=None):
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        e = discord.Embed(title=f"{ctx.message.author.display_name}'s XP", color=theme_color)
        if member_data.level == 0:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/25'))
        elif member_data.level == 1:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/50'))
        elif member_data.level == 2:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/100'))
        elif member_data.level == 3:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/500'))
        elif member_data.level == 4:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/750'))
        elif member_data.level == 5:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1000'))
        elif member_data.level == 6:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1200'))
        elif member_data.level == 7:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1400'))
        elif member_data.level == 8:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1600'))
        elif member_data.level == 9:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1800'))
        elif member_data.level == 10:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2000'))
        elif member_data.level == 11:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2200'))
        elif member_data.level == 12:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2400'))
        elif member_data.level == 13:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2600'))
        elif member_data.level == 14:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2800'))
        elif member_data.level == 15:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3000'))
        elif member_data.level == 16:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3200'))
        elif member_data.level == 17:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3400'))
        elif member_data.level == 18:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3600'))
        elif member_data.level == 19:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3800'))
        elif member_data.level >= 20:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/4000'))
        e.set_footer(text='To level up, keep on chatting or consume bobas!')
        await ctx.send(embed=e)
    else:
        member_data = load_member_data(user.id)
        e = discord.Embed(title=f"{user.display_name}'s XP", color=theme_color)
        if member_data.level == 0:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/25'))
        elif member_data.level == 1:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/50'))
        elif member_data.level == 2:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/100'))
        elif member_data.level == 3:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/500'))
        elif member_data.level == 4:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/750'))
        elif member_data.level == 5:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1000'))
        elif member_data.level == 6:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1200'))
        elif member_data.level == 7:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1400'))
        elif member_data.level == 8:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1600'))
        elif member_data.level == 9:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/1800'))
        elif member_data.level == 10:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2000'))
        elif member_data.level == 11:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2200'))
        elif member_data.level == 12:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2400'))
        elif member_data.level == 13:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2600'))
        elif member_data.level == 14:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/2800'))
        elif member_data.level == 15:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3000'))
        elif member_data.level == 16:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3200'))
        elif member_data.level == 17:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3400'))
        elif member_data.level == 18:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3600'))
        elif member_data.level == 19:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/3800'))
        elif member_data.level == 20:
            e.add_field(name='Level', value=str(member_data.level))
            e.add_field(name='XP', value=str(f'{member_data.xp}/4000'))
        e.set_footer(text='To level up, keep on chatting or consume bobas!')
        await ctx.send(embed=e)

@client.command()
async def add_xp(ctx, user:discord.User, *, arg1):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'{ctx.author.mention}, you cannot use this command!')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.xp += int(arg1)
            save_member_data(user.id, member_data)
            await ctx.send(f':bubble_tea: Done! I added {arg1} XP to {user.display_name}\'s account')
        else:
            await ctx.reply(f'{ctx.author.mention}, {arg1} is not a number...')

@client.command()
async def edit_snipe(ctx):
    try:
        em = discord.Embed(description=f'**Message before**: {before}\n**Message after**:{after}', color=theme_color)
        em.set_footer(text=f'This message was edited by {author}')
        await ctx.send(embed = em)
    except:
        await ctx.reply(f'Hmmm... There aren\'t any recently edited messages in <#{ctx.channel.id}>')

@client.command()
async def add_lvl(ctx, user : discord.User, *, arg1):
    if ctx.message.author.id not in ids:
        await ctx.reply(f'Oops, {ctx.author.mention}, you cannot use this command!')
    else:
        if arg1.isdigit:
            member_data = load_member_data(user.id)
            member_data.level += int(arg1)
            save_member_data(user.id, member_data)
            await ctx.send(f':bubble_tea: Done! I added {arg1} level(s) to {user.display_name}\'s account')
        else:
            await ctx.reply(f'{ctx.author.mention}, {arg1} is not a number...')

@client.command(aliases=['consume_boba', 'cons', 'consume', 'consumeboba', 'cb'])
@commands.cooldown(1, 30, commands.BucketType.user)
async def consume_bubbletea(ctx, arg1:int = None):
    member_data = load_member_data(ctx.message.author.id)
    if member_data.boba <= 0:
        await ctx.reply(f'{ctx.message.author.mention}, you don\'t have any bobas!')
        return 
    else:
        if arg1 == None:
            member_data.boba -= 1
            member_data.xp += 100
            save_member_data(ctx.message.author.id, member_data)
            await ctx.reply(f'You consumed 1 boba tea and earned **100 XP**! To see your XP, run `%level`')
        elif arg1 <= 0:
            await ctx.reply(f'{ctx.message.author.mention}, you can\'t consume 0 bobas!')
            return
        elif arg1 > 20:
            await ctx.send(f'{ctx.message.author.mention}, you can\'t consume more than 20 bobas at a time!')
        else:
            xpToAdd = 100 * arg1
            member_data.boba -= arg1
            member_data.xp += xpToAdd
            save_member_data(ctx.message.author.id, member_data)
            await ctx.reply(f'You consumed {arg1} boba tea(s) and earned **{xpToAdd} XP**! To see your XP, run `%level`')

@client.command(aliases=['bobatea', 'boba_tea', 'bubbletea'])
async def bubble_tea(ctx):
    boba_imgs = [
        'https://www.thespruceeats.com/thmb/cI9Yn1OsIA2stjuFzPd7g1GxSpQ=/4609x3073/filters:fill(auto,1)/types-of-bubble-tea-766451-hero-01-a6dca4dd096a4d8abdde1a754766f851.jpg',
        'https://www.cremashop.eu/content/www.crema.fi/media/info/guides/what-is-bubble-tea/illustration_1a5ad14874a750bbff917c1b027bb2e5.jpeg',
        'https://veggiefestchicago.org/wp-content/uploads/2021/05/21-bumble.jpg',
        'https://thenovicechefblog.com/wp-content/uploads/2020/03/Bubble-Tea-with-Boba.jpg',
        'https://d3mvlb3hz2g78.cloudfront.net/wp-content/uploads/2020/04/thumb_720_450_dreamstime_m_93782496.jpg'
    ]
    boba_img_display = random.choice(boba_imgs)
    emb = discord.Embed(title='Boba Tea :bubble_tea:', color=theme_color)
    emb.set_image(url=boba_img_display)
    await ctx.send(embed=emb)

@client.command(aliases=['cg', 'neko'])
async def catgirl(ctx):
    if ctx.message.channel.id == 888660822572806165:
        random_catgirl = nekos.img('neko')
        emb = discord.Embed(name='Catgirl (Neko)', color=theme_color)
        emb.set_image(url=random_catgirl)
        await ctx.send(embed=emb)
    else:
        await ctx.reply(f'{ctx.message.author.mention}, you aren\'t allowed to use this command here. It is restricted to <#888660822572806165> .-.')

@client.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f'{text}')

@client.command()
async def uptime(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
    await ctx.send(f'This session has been running for {uptime}')

@client.command()
async def snipe(ctx):
    channel = ctx.channel
    try:
        if any(x in snipe_message_content[channel.id] for x in bad):
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = f'||{snipe_message_content[channel.id]}||', color=0xcf1515)
            em.set_footer(text = f"WARNING! This message contains profane text.\nThis message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
        else:
            em = discord.Embed(name = f"Last deleted message in #{channel.name}", description = snipe_message_content[channel.id], color=theme_color)
            em.set_footer(text = f"This message was sent by {snipe_message_author[channel.id]}")
            await ctx.send(embed = em)
    except:
        await ctx.send(f"Hmm... There are no recently deleted messages in <#{ctx.channel.id}>")
@client.command(aliases=['commands'])
async def help(ctx):
    emb = discord.Embed(title=f'My Commands',  description=f'Hi! I am Boba bot and here are the commands that I can do.\n\n**Economy:** `%collectboba` `%dailyboba` `%weeklyboba` `%monthlyboba` `%consumeboba` `%level` `%giftboba` `%dropboba`\n**Bot Information:** `%help` `%snipe` `%edit_snipe` `%userinfo` `%ping`\n**Moderation:** `%kick` `%ban`\n**Fun:** `%say` `%meme` `%boba` `%softwaregore` `%cat` `%catgirl`', color=theme_color)
    await ctx.send(embed = emb)

@client.command(aliases=['ui', 'memberinfo'])
async def userinfo(ctx, user:discord.User = None):
    if user == None:
        is_bot = 'NA'
        if ctx.author.bot == True:
            is_bot = 'Bot'
        elif ctx.author.bot == False:
            is_bot = 'Normal user'
        userAvatar = ctx.author.avatar_url
        embed683 = discord.Embed(title=f'User info for {ctx.author}', description=f'User Name: {ctx.author}\nDisplay Name: {ctx.author.display_name}\nUser ID: {ctx.author.id}\nAvatar URL: {userAvatar}\nAccount Created: {ctx.author.created_at}\nUser Type: {is_bot}\n', color=theme_color)
        embed683.set_thumbnail(url=userAvatar)
        embed683.set_footer(text=f'User info requested by {ctx.author}')
        await ctx.send(embed=embed683)
    else:
        is_bot = 'NA'
        if user.bot == True:
            is_bot = 'Bot'
        elif user.bot == False:
            is_bot = 'Normal user'
        await ctx.trigger_typing()
        userAvatar = user.avatar_url
        embed683 = discord.Embed(title=f'User info for {user}', description=f'Display Name: {user.display_name}\nDiscord Tag: {user}\nUser ID: {user.id}\nAvatar URL: {userAvatar}\nAccount Created: {user.created_at}\nUser Type: {is_bot}\n', color=theme_color)
        embed683.set_thumbnail(url=userAvatar)
        embed683.set_footer(text=f'User info requested by {ctx.author}')
        await ctx.send(embed=embed683)

@client.command(aliases=['pong'])
async def ping(ctx):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    await ctx.send(f':ping_pong: Pong! In **{round(client.latency * 1000)}ms**.')
    if bool(log) == True:
        with open(loggerHandler_path, 'a') as f:
            f.write(f'[{current_time}] Bot ping is {round(client.latency * 1000)}ms\n')
            f.close()
        print(f'[{current_time}] Bot ping is {colors.green}{round(client.latency * 1000)}ms{colors.end}')
        pass
    else:
        return

@client.command()
async def invite(ctx, is_raw=None):
    if is_raw == None:
        await ctx.send(f':sparkles:SERVER INVITE:sparkles:\n\nhttps://discord.gg/JYMmmDgYhN')
        await ctx.send('Copy-paste the above message in other servers!')
    elif is_raw == 'raw':
        await ctx.send('```:sparkles:SERVER INVITE:sparkles:\n\nhttps://discord.gg/JYMmmDgYhN```')
        await ctx.send('Copy-paste the above message in other servers!')

@client.command()
async def meme(ctx):
  memes_submissions = reddit.subreddit('memes').hot()
  post_to_pick = random.randint(1, 100)
  for i in range(0, post_to_pick):
    submission = next(x for x in memes_submissions if not x.stickied)
  embed = discord.Embed(title = submission.title, color=theme_color)
  embed.set_image(url=submission.url)
  embed.set_footer(text='Memes be like')
  await ctx.send(embed = embed)

@client.command(aliases=['sg'])
async def softwaregore(ctx):
    if ctx.message.channel.id == 888660822572806165:  # Bot-commands channel #
        sg_submissions = reddit.subreddit('softwaregore').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in sg_submissions if not x.stickied)
        embed = discord.Embed(title = submission.title, color=theme_color)
        embed.set_image(url=submission.url)
        embed.set_footer(text='Error: 404: Could not be found')
        await ctx.send(embed = embed)
    elif ctx.message.channel.id == 874172041207627797:  # Pics channel #
        sg_submissions = reddit.subreddit('softwaregore').hot()
        post_to_pick = random.randint(1, 100)
        for i in range(0, post_to_pick):
            submission = next(x for x in sg_submissions if not x.stickied)
        embed = discord.Embed(title = submission.title, color=theme_color)
        embed.set_image(url=submission.url)
        embed.set_footer(text='Error: 404: Could not be found')
        await ctx.send(embed = embed)
    else:
        await ctx.reply(f'{ctx.message.author.mention}, you aren\'t allowed to use this command here. It is restricted to <#888660822572806165> and <#874172041207627797> .-.')
    
@client.command()
async def credits(ctx):
  emb = discord.Embed(title='Bot Credits', description='Owner: 𝔼𝕝𝕗𝕚𝕖#7240\nCo-owner: notsniped#6776', color=theme_color)
  emb.set_footer(text='Boba bot 2021, a part of Lavender Army', icon_url='https://cdn.discordapp.com/icons/874160923860955136/aa875d989234c397fbc41e7487b72028.png?size=4096')
  await ctx.send(embed=emb)

## Economy Commands ##

@client.command(aliases=['daily'])
@commands.cooldown(1, 86400, commands.BucketType.user)
async def dailyboba(ctx):
  if bool(currency) == False:
    await ctx.reply('Currency is temporarily disabled.')
    return
  else:
    pass
  now = datetime.datetime.now()
  current_time = now.strftime("%H:%M:%S") 
  member_data = load_member_data(ctx.message.author.id)
  member_data.boba += 1000
  await ctx.reply('You claimed your daily **1,000 bobas!** :bubble_tea:')
  save_member_data(ctx.message.author.id, member_data)
  if bool(log) == True:
    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} claimed {colors.green}1000{colors.end} bobas from daily command.')
  else:
    pass

@client.command(aliases=['weekly'])
@commands.cooldown(1, 604800, commands.BucketType.user)
async def weeklyboba(ctx):
  if bool(currency) == False:
    await ctx.reply('Currency is temporarily disabled.')
    return
  else:
    pass
  now = datetime.datetime.now()
  current_time = now.strftime("%H:%M:%S") 
  member_data = load_member_data(ctx.message.author.id)
  member_data.boba += 10000
  await ctx.reply('You claimed your weekly **10,000 bobas!** :bubble_tea:')
  save_member_data(ctx.message.author.id, member_data)
  if bool(log) == True:
    print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} claimed {colors.green}10000{colors.end} bobas from daily command.')
  else:
    pass

@client.command(aliases=['monthly'])
@commands.cooldown(1, 2592000, commands.BucketType.user)
async def monthlyboba(ctx):
    if bool(currency) == False:
        await ctx.reply('Currency is temporarily disabled.')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S") 
    member_data = load_member_data(ctx.message.author.id)
    member_data.boba += 125000
    await ctx.reply('You claimed your monthly **1,25,000 bobas!** :bubble_tea:')
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} claimed {colors.green}125000{colors.end} bobas from daily command.')
    else:
        pass

@client.command(aliases=['claimboba', 'work', 'collect', 'claim'])
@commands.cooldown(1, 1800, commands.BucketType.user)
async def collectboba(ctx):
    if bool(currency) == False:
        await ctx.send('Currency is temporarily disabled.')
        return
    else:
        pass
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    member_data = load_member_data(ctx.message.author.id)
    coins = randint(100, 2000)
    member_data.boba += coins
    await ctx.send(f"You worked and got **{coins} bobas!** :bubble_tea:")
    save_member_data(ctx.message.author.id, member_data)
    if bool(log) == True:
        with open(loggerHandler_path, 'a') as f:
                f.write(f'[{current_time}] {ctx.message.author.display_name} earned {coins} bobas.\n')
                f.close()
        print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} earned {colors.green}{coins}{colors.end} bobas')
    else:
        pass

@client.command(aliases=['purchase'])
async def buylavender(ctx, arg1:int = None):
    member_data = load_member_data(ctx.message.author.id)
    if arg1 == None:
        await ctx.reply(f'{ctx.message.author.mention}, how many lavenders do you wanna buy? Please run this command again as `;buylavender [amount]`')
        return
    elif arg1 <= 0:
        await ctx.reply(f'{ctx.message.author.mention}, you can\'t buy 0 lavenders!')
        return
    else:
        toPay = arg1 * 100
        if member_data.boba < toPay:
            await ctx.reply(f'You don\'t have that many bobas!')
            return
        else:
            member_data.boba -= toPay
            member_data.special += arg1
            save_member_data(ctx.message.author.id, member_data)
            await ctx.send(f'{ctx.message.author.mention}, you just bought {arg1} lavenders for {toPay} bobas!')

@client.command(aliases=['bal', 'inv', 'balance', 'currency'])
async def inventory(ctx, user:discord.User=None):
    if bool(currency) == False:
        await ctx.send('Currency is temporarily disabled.')
        return
    else:
        pass
    if user == None:
        member_data = load_member_data(ctx.message.author.id)
        embed = discord.Embed(title=f"{ctx.message.author.display_name}'s Inventory", color=theme_color)
        embed.add_field(name=":bubble_tea: Bobas", value=str(member_data.boba))
        embed.add_field(name="Lavenders", value=str(member_data.special))
        embed.set_footer(text=f'Currency API made by {owner}')
        await ctx.send(embed=embed)
    else:
        member_data = load_member_data(user.id)
        embed = discord.Embed(title=f"{user.display_name}'s Inventory", color=theme_color)
        embed.add_field(name=":bubble_tea: Bobas", value=str(member_data.boba))
        embed.add_field(name="Lavenders", value=str(member_data.special))
        embed.set_footer(text=f'Currency API made by {owner}')
        await ctx.send(embed=embed)

@client.command(aliases=['pick'])
async def pickboba(ctx):
  if dropped[str(ctx.guild.id)] == None:
    await ctx.reply('There are no bobas to pick!')
    return
  else:
    await ctx.send(f'{ctx.author.mention} picked {dropped[str(ctx.guild.id)]} bobas! :bubble_tea:')
    member_data = load_member_data(ctx.message.author.id)
    member_data.boba += dropped[str(ctx.guild.id)]
    save_member_data(ctx.message.author.id, member_data)
    dropboba[str(ctx.guild.id)] = None

@client.command(aliases=['drop'])
async def dropboba(ctx, amount:int = None):
  member_data = load_member_data(ctx.message.author.id)
  if amount == None:
    await ctx.reply('I don\'t know how much boba you want to drop. Please mention how much next time.')
    return
  elif member_data.boba < amount:
    await ctx.reply(f'You don\'t have enough bobas to do that!')
    return
  elif amount < 1:
    raise(BadArgument)
  else:
    dropped[str(ctx.guild.id)] = amount
    member_data.boba -= amount
    save_member_data(ctx.message.author.id, member_data)
    await ctx.reply(f':white_check_mark: Dropped {dropped[str(ctx.guild.id)]} bobas!')

@client.command(aliases=['add_boba'])
async def add_bal(ctx, user:discord.User, amount:int):
  if ctx.author.id not in ids:
    return
  else:
    member_data = load_member_data(user.id)
    member_data += amount
    save_member_data(user.id, member_data)
    await ctx.reply(f'Added {amount} bobas to {user.display_name}\'s account.')

## Economy Commands End ##

## Moderation Commands ##

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member:discord.Member, *, reason = None):
    embedKick = None
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if member == ctx.message.author:
        await ctx.reply('Don\'t kick yourself!')
        return
    else:
        try:
            await member.kick()
            if reason == None:
                embedKick = discord.Embed(description=f':white_check_mark: _I **kicked** {member} from this server._', color=color_success)
            else:
                embedKick = discord.Embed(description=f':white_check_mark: _I **kicked** {member} from this server._ Reason: {reason}', color=color_success)
            await ctx.send(embed=embedKick)
            if bool(log) == True:
                with open(loggerHandler_path, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} kicked {member.display_name} from {ctx.message.guild.name}\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} kicked {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.message.guild.name}{colors.end}.')
            else:
                pass
        except:
            embedKick = discord.Embed(description=f':x: I can\'t kick {member}!', color=color_fail)
            await ctx.send(embed=embedKick)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member:discord.Member, *, reason = None):
    embedBan = None
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if member == ctx.message.author:
        await ctx.reply('Don\'t ban yourself!')
        return
    else:
        try:
            await member.ban()
            if reason == None:
                embedBan = discord.Embed(description=f':white_check_mark: _I **banned** {member} from this server._', color=color_success)
            else:
                embedBan = discord.Embed(description=f':white_check_mark: _I **banned** {member} from this server._ Reason: {reason}', color=color_success)
            await ctx.send(embed=embedBan)
            if bool(log) == True:
                with open(loggerHandler_path, 'a') as f:
                    f.write(f'[{current_time}] {ctx.message.author.display_name} banned {member.display_name} from {ctx.message.guild.name}\n')
                    f.close()
                print(f'[{current_time}] {colors.cyan}{ctx.message.author.display_name}{colors.end} banned {colors.green}{member.display_name}{colors.end} from {colors.green}{ctx.message.guild.name}{colors.end}.')
            else:
                pass
        except:
            embedBan = discord.Embed(description=f':x: I can\'t ban {member}!', color=color_fail)
            await ctx.send(embed=embedBan)

@client.command(description="Unmutes a server member.", aliases=['unsilence'])
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member:discord.Member):
    if member.id == ctx.author.id:
        await ctx.send(f'{ctx.author.mention}, you can\'t mute urself.')
        return
    else:
        pass
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(mutedRole)
    await member.send(f"Hi, {member.mention}, you were unmuted in {ctx.guild.name}!")
    embed = discord.Embed(title="Unmute User", description=f":white_check_mark: {member.mention} has been unmuted.", colour=theme_color)
    await ctx.send(embed=embed)

@client.command(description="Mutes a server member.", alises=['silence'])
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member:discord.Member, *, reason=None):
    if member.id == ctx.author.id:
        await ctx.send(f'{ctx.author.mention}, you can\'t unmute urself.')
        return
    else:
        pass
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    embed = discord.Embed(title="Mute User", description=f":white_check_mark: {member.mention} has been muted.", colour=theme_color)
    embed.add_field(name="Reason", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"{member.mention}, you have been muted in {guild.name}.\nReason: *{reason}*")

## Moderation Commands End ##

### Commands end ###
keep_alive()
mainloop()
client.run('')