import disnake
from disnake import Option, OptionType, OptionChoice, ApplicationCommandInteraction
from disnake.ext import commands

import os

class Cogs(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def autocomp_loadedcogs(ctx: ApplicationCommandInteraction, user_input: str):
        return [cog for cog in ctx.client.loadedcogs if (user_input.lower() in cog) or (user_input in cog)]
    
    async def autocomp_unloadedcogs(ctx: ApplicationCommandInteraction, user_input: str):
        return [cog for cog in ctx.client.unloadedcogs if (user_input.lower() in cog) or (user_input in cog)]
    
    @commands.slash_command(name = 'cog-utils')
    async def cogutils(self, ctx: ApplicationCommandInteraction):
        pass

    @cogutils.sub_command(
        name = 'load',
        description = 'Load a cog/extension (autocomplete options).'
    )
    async def cogload(
        self, ctx: ApplicationCommandInteraction,
        cog: str = commands.Param(desc = 'Enter the cog/extension to be loaded into the bot.', autocomp = autocomp_unloadedcogs)
    ):

        if 'basic' in cog:
            ctx.client.load_extension(f'basic-cmds.{cog}')
        elif 'slash' in cog:
            ctx.client.load_extension(f'slash-cmds.{cog}')
        elif 'cotxt' in cog:
            ctx.client.load_extension(f'cotxt-cmds.{cog}')
        elif 'utils' in cog:
            ctx.client.load_extension(f'utils-cmds.{cog}')
        
        ctx.client.loadedcogs.append(cog)
        ctx.client.unloadedcogs.remove(cog)
        
        await ctx.response.send_message(f'Loaded `{cog}`.')

    @cogutils.sub_command(
        name = 'unload',
        description = 'Unload a cog/extension (autocomplete options).'
    )
    async def cogunload(
        self, ctx: ApplicationCommandInteraction,
        cog: str = commands.Param(desc = 'Enter the cog/extension to be unloaded from the bot.', autocomp = autocomp_loadedcogs)
    ):

        if 'basic' in cog:
            ctx.client.unload_extension(f'basic-cmds.{cog}')
        elif 'slash' in cog:
            ctx.client.unload_extension(f'slash-cmds.{cog}')
        elif 'cotxt' in cog:
            ctx.client.unload_extension(f'cotxt-cmds.{cog}')
        elif 'utils' in cog:
            ctx.client.unload_extension(f'utils-cmds.{cog}')

        ctx.client.loadedcogs.remove(cog)
        ctx.client.unloadedcogs.append(cog)
        
        await ctx.response.send_message(f'Unloaded `{cog}`.')


    @cogutils.sub_command(
        name = 'reload',
        description = 'Reload a cog/extension (autocomplete options).'
    )
    async def cogreload(
        self, ctx: ApplicationCommandInteraction,
        cog: str = commands.Param(desc = 'Enter the cog/extension to be reloaded into the bot.', autocomp = autocomp_loadedcogs)
    ):

        if 'basic' in cog:
            ctx.client.reload_extension(f'basic-cmds.{cog}')
        elif 'slash' in cog:
            ctx.client.reload_extension(f'slash-cmds.{cog}')
        elif 'cotxt' in cog:
            ctx.client.reload_extension(f'cotxt-cmds.{cog}')
        elif 'utils' in cog:
            ctx.client.reload_extension(f'utils-cmds.{cog}')
        
        await ctx.response.send_message(f'Reloaded `{cog}`.')
    
    @cogutils.sub_command(
        name = 'reloadall',
        description = 'Reloads all cogs/extensions.'
    )
    async def cogreloadall(
        self, ctx: ApplicationCommandInteraction
    ):

        await ctx.response.send_message('**Reloading cogs in process...**')

        edit = []
        edit.append('**---------- BASIC COMMANDS ----------**')
        for filename in os.listdir('./basic-cmds'):
            try:
                if filename.endswith('.py'):
                    ctx.client.reload_extension(f'basic-cmds.{filename[:-3]}')
                    edit.append(f'**|  Reloaded {filename}.**')
                else:
                    pass
            except Exception as e:
                edit.append(f'**|  Could not reload {filename} due to exception:** \n```{e}```')

        edit.append('**--------- CONTEXT COMMANDS ---------**')
        for filename in os.listdir('./cotxt-cmds'):
            try:
                if filename.endswith('.py'):
                    ctx.client.reload_extension(f'cotxt-cmds.{filename[:-3]}')
                    edit.append(f'**|  Reloaded {filename}.**')
                else:
                    pass
            except Exception as e:
                edit.append(f'**|  Could not reload {filename} due to exception:** \n```{e}```')

        edit.append('**---------- SLASH COMMANDS ----------**')
        for filename in os.listdir('./slash-cmds'):
            try:
                if filename.endswith('.py'):
                    ctx.client.reload_extension(f'slash-cmds.{filename[:-3]}')
                    edit.append(f'**|  Reloaded {filename}.**')
                else:
                    pass
            except Exception as e:
                edit.append(f'**|  Could not reload {filename} due to exception:** \n```{e}```')

        edit.append('**---------- UTILS COMMANDS ----------**')
        for filename in os.listdir('./utils-cmds'):
            try:
                if filename.endswith('.py'):
                    ctx.client.reload_extension(f'utils-cmds.{filename[:-3]}')
                    edit.append(f'**|  Reloaded {filename}.**')
                else:
                    pass
            except Exception as e:
                edit.append(f'**|  Could not reload {filename} due to exception:** \n```{e}```')
        edit.append('**-----------------------------------------------**')
        edit.append('**COGS RELOADED.**')

        edited = '\n'.join(edit)
        await ctx.edit_original_message(content = edited)

def setup(client):
    client.add_cog(Cogs(client))