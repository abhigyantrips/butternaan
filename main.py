import disnake as discord
from disnake.ext import commands
from disnake.ext.commands import ConversionError
from disnake.utils import get
from disnake import SlashCommand

from dotenv import load_dotenv
load_dotenv(dotenv_path = '.\settings.env')

import os
import random
import asyncio

client = commands.Bot(command_prefix = "!", intents = discord.Intents().all())
test_guilds = [860414380444483584]

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Activity(type= discord.ActivityType.watching, name = "the world burn.",))
    print("------------------------------------")
    print('Hello! The bot is back online :]')

print("---------- BASIC COMMANDS ----------")
for filename in os.listdir('./basic-cmds'):
    try:
        if filename.endswith('.py'):
            client.load_extension(f'basic-cmds.{filename[:-3]}')
            print(f"|  {filename} loaded.")
        elif filename == "__pycache__":
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

print("---------- SLASH COMMANDS ----------")
for filename in os.listdir('./slash-cmds'):
    try:
        if filename.endswith('.py'):
            client.load_extension(f'slash-cmds.{filename[:-3]}')
            print(f"|  {filename} loaded.")
        elif filename == "__pycache__":
            pass
    except Exception as e:
        print(f'|  Could not load {filename} due to exception: \n{e}')

### LOG EVENTS ###

@client.event
async def on_message_edit(before, after):

    embed = discord.Embed(
    title = "Message Edited.",
    color = 0x303136,
    description = f"A message by {before.author.mention} was edited in {before.channel.mention}."
    )

    embed.set_thumbnail(url = before.author.avatar)

    embed.add_field(name = "Before", value = before.content, inline = False)
    embed.add_field(name = "After", value = after.content, inline = False)

    await client.get_channel(891527413866053653).send(embed = embed) # The ID refers to the server log in my server.

@client.event
async def on_message_delete(message):

    async for entry in message.guild.audit_logs(limit = 1, action = discord.AuditLogAction.message_delete):
        deleter = entry.user

    if deleter == message.author:
        desc = f"{message.author.mention} deleted their message in {message.channel.mention}."
    elif deleter == self.user:
        pass
    else:
        desc = f"A message by {message.author.mention} was deleted in {message.channel.mention} by {deleter.mention}."

    embed = discord.Embed(
        title = "Message Deletion.",
        color = 0x303136,
        description = desc
    )

    embed.set_thumbnail(url = message.author.avatar)

    if message.reference is not None and not message.is_system:
        ref_msg = client.get_message(message.reference.id)
        embed.add_field(name = f"Replying to {ref_msg.author.mention}", value = ref_msg.content, inline = False)
    
    embed.add_field(name = f"Deleted Message", value = message.content, inline = False)

    await client.get_channel(891527413866053653).send(embed = embed) # The ID refers to the server log in my server.

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
                await ctx.send(f"**|  {filename} reloaded.**")
            elif filename == "__pycache__":
                pass
        except Exception as e:
            await ctx.send(f'**|  Could not reload {filename} due to exception:** \n```{e}```')

    await ctx.send("**---------- SLASH COMMANDS ----------**")
    for filename in os.listdir('./slash-cmds'):
        try:
            if filename.endswith('.py'):
                client.reload_extension(f'slash-cmds.{filename[:-3]}')
                await ctx.send(f"**|  {filename} reloaded.**")
            elif filename == "__pycache__":
                pass
        except Exception as e:
            await ctx.send(f'**|  Could not reload {filename} due to exception:** \n```{e}```')
    await ctx.send("**-----------------------------------------------**")
    await ctx.send("**COGS RELOADED.**")

DISCORD_BOT_TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
client.run(DISCORD_BOT_TOKEN)