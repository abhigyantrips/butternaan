import os
import random

import disnake
from disnake.ext import commands

try:
    from dotenv import load_dotenv
except ImportError:
    pass
else:
    load_dotenv()

client = commands.Bot(
    command_prefix="!",
    intents=disnake.Intents().all(),
    help_command=None,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="the world burn."),
    status=disnake.Status.idle,
    test_guilds=[
        int(os.getenv("TEST_GUILDS_ONE")),
        int(os.getenv("TEST_GUILDS_TWO")),
    ],
)
client.loadedcogs = []
client.unloadedcogs = []


@client.event
async def on_ready():

    print("------------ COMMANDS ------------")
    for filename in os.listdir("./commands"):
        try:
            if filename.endswith(".py"):
                client.load_extension(f"commands.{filename[:-3]}")
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f"|  Could not load {filename} due to exception: \n{e}")

    print("---------- INTERACTIONS ----------")
    for filename in os.listdir("./interactions"):
        try:
            if filename.endswith(".py"):
                client.load_extension(f"interactions.{filename[:-3]}")
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f"|  Could not load {filename} due to exception: \n{e}")

    print("----------- UTILITIES ------------")
    for filename in os.listdir("./utils"):
        try:
            if filename.endswith(".py"):
                client.load_extension(f"utils.{filename[:-3]}")
                client.loadedcogs.append(filename[:-3])
                print(f"|  Loaded {filename}.")
            else:
                pass
        except Exception as e:
            print(f"|  Could not load {filename} due to exception: \n{e}")
    print("------------------------------------")
    print("Hello! The bot is back online :]")


client.run(os.getenv("DISCORD_BOT_TOKEN"))
