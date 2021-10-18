import disnake
from disnake.ext import commands

import dotenv
dotenv.load_dotenv()

import os
import random
import asyncio

client = commands.Bot(command_prefix = "!", intents = disnake.Intents().all(), strip_after_prefix = True, test_guilds = [int(os.environ.get('TEST_GUILDS'))])

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
            print(f"|  Loaded {filename}.")
        else:
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

### COG COMMANDS ###

@client.command()
async def load(ctx, extension_folder, extension):
    client.load_extension(f'{extension_folder}.{extension}')
    await ctx.send(f'{extension} is now loaded.')

@client.command()
async def unload(ctx, extension_folder, extension):
    client.unload_extension(f'{extension_folder}.{extension}')
    await ctx.send(f'{extension} is now unloaded.')

@client.command()
async def reload(ctx, extension):
    if "slash-cmd" in extension:
        client.reload_extension(f'slash-cmds.{extension}')
        await ctx.send(f"**{extension}** has been reloaded.")
    elif "basic-cmd" in extension:
        client.reload_extension(f'basic-cmds.{extension}')
        await ctx.send(f"**{extension}** has been reloaded.")

@client.command()
async def reloadall(ctx):

    await ctx.send("**---------- BASIC COMMANDS ----------**")
    for filename in os.listdir('./basic-cmds'):
        try:
            if filename.endswith('.py'):
                client.reload_extension(f'basic-cmds.{filename[:-3]}')
                await ctx.send(f"**|  Reloaded {filename}.**")
            else:
                pass
        except Exception as e:
            await ctx.send(f'**|  Could not reload {filename} due to exception:** \n```{e}```')

    await ctx.send("**--------- CONTEXT COMMANDS ---------**")
    for filename in os.listdir('./cotxt-cmds'):
        try:
            if filename.endswith('.py'):
                client.reload_extension(f'cotxt-cmds.{filename[:-3]}')
                await ctx.send(f"**|  Reloaded {filename}.**")
            else:
                pass
        except Exception as e:
            await ctx.send(f'**|  Could not reload {filename} due to exception:** \n```{e}```')

    await ctx.send("**---------- SLASH COMMANDS ----------**")
    for filename in os.listdir('./slash-cmds'):
        try:
            if filename.endswith('.py'):
                client.reload_extension(f'slash-cmds.{filename[:-3]}')
                await ctx.send(f"**|  Reloaded {filename}.**")
            else:
                pass
        except Exception as e:
            await ctx.send(f'**|  Could not reload {filename} due to exception:** \n```{e}```')
    await ctx.send("---------- UTILS COMMANDS ----------")
    for filename in os.listdir('./utils-cmds'):
        try:
            if filename.endswith('.py'):
                client.reload_extension(f'utils-cmds.{filename[:-3]}')
                await ctx.send(f"**|  Reloaded {filename}.**")
            else:
                pass
        except Exception as e:
            await ctx.send(f'**|  Could not reload {filename} due to exception:** \n```{e}```')
    await ctx.send("**-----------------------------------------------**")
    await ctx.send("**COGS RELOADED.**")

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
client.run(DISCORD_BOT_TOKEN)