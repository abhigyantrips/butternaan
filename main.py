import disnake
from disnake.ext import commands

import dotenv
dotenv.load_dotenv()

import os
import random
import asyncio

client = commands.Bot(command_prefix = "!", intents = disnake.Intents().all(), strip_after_prefix = True, test_guilds = [int(os.environ.get('TEST_GUILDS'))])
client.loadedcogs = []
client.unloadedcogs = []

@client.event
async def on_ready():
    await client.change_presence(status = disnake.Status.idle, activity = disnake.Activity(type= disnake.ActivityType.watching, name = "the world burn.",))
    print("------------------------------------")
    print('Hello! The bot is back online :]')

print("---------- BASIC COMMANDS ----------")
for filename in os.listdir('./basic-cmds'):
    try:
        if filename.endswith('.py'):
            client.load_extension(f'basic-cmds.{filename[:-3]}')
            client.loadedcogs.append(filename[:-3])
            print(f"|  Loaded {filename}.")
        else:
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

print("--------- CONTEXT COMMANDS ---------")
for filename in os.listdir('./cotxt-cmds'):
    try:
        if filename.endswith('.py'):
            client.load_extension(f'cotxt-cmds.{filename[:-3]}')
            client.loadedcogs.append(filename[:-3])
            print(f"|  Loaded {filename}.")
        else:
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

print("---------- SLASH COMMANDS ----------")
for filename in os.listdir('./slash-cmds'):
    try:
        if filename.endswith('.py'):
            client.load_extension(f'slash-cmds.{filename[:-3]}')
            client.loadedcogs.append(filename[:-3])
            print(f"|  Loaded {filename}.")
        else:
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

print("---------- UTILS COMMANDS ----------")
for filename in os.listdir('./utils-cmds'):
    try:
        if filename.endswith('.py'):
            client.load_extension(f'utils-cmds.{filename[:-3]}')
            client.loadedcogs.append(filename[:-3])
            print(f"|  Loaded {filename}.")
        else:
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
client.run(DISCORD_BOT_TOKEN)