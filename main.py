import disnake
from disnake.ext import commands

import dotenv
dotenv.load_dotenv()

import os
import random
import asyncio

client = commands.Bot(
    command_prefix = "!", 
    intents = disnake.Intents().all(), 
    test_guilds = [int(os.environ.get('TEST_GUILDS'))],
    help_command = None
)
client.loadedcogs = []
client.unloadedcogs = []

@client.event
async def on_ready():
    await client.change_presence(status = disnake.Status.idle, activity = disnake.Activity(type= disnake.ActivityType.watching, name = "the world burn.",))
    print("---------- BASIC COMMANDS ----------")
    for filename in os.listdir('./cmds-basic'):
        try:
            if filename.endswith('.py'):
                client.load_extension(f'cmds-basic.{filename[:-3]}')
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f'|  Could not load {filename} due to exception: \n{e}')

    print("--------- CONTEXT COMMANDS ---------")
    for filename in os.listdir('./cmds-cotxt'):
        try:
            if filename.endswith('.py'):
                client.load_extension(f'cmds-cotxt.{filename[:-3]}')
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f'|  Could not load {filename} due to exception: \n{e}')

    print("---------- SLASH COMMANDS ----------")
    for filename in os.listdir('./cmds-slash'):
        try:
            if filename.endswith('.py'):
                client.load_extension(f'cmds-slash.{filename[:-3]}')
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f'|  Could not load {filename} due to exception: \n{e}')

    print("---------- UTILS COMMANDS ----------")
    for filename in os.listdir('./cmds-utils'):
        try:
            if filename.endswith('.py'):
                client.load_extension(f'cmds-utils.{filename[:-3]}')
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f'|  Could not load {filename} due to exception: \n{e}')    
    print("------------------------------------")
    print('Hello! The bot is back online :]')

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
client.run(DISCORD_BOT_TOKEN)