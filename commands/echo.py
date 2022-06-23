import typing

import disnake
from disnake.ext import commands
from disnake.utils import get


class Echo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def echo(self, ctx, reply: typing.Optional[disnake.Message]=None, *, message: str):
        
        if (ctx.channel.name != "spam") and (not ctx.author.guild_permissions.administrator): 
            return
        
        await ctx.message.delete()
		
        if not reply:
            if ctx.message.reference:
                if isinstance(ctx.message.reference.resolved, disnake.Message):
                    return await ctx.message.reference.resolved.reply(message, files=[await a.to_file() for a in ctx.message.attachments])
                return await ctx.send(message, files=[await a.to_file() for a in ctx.message.attachments])
            return await ctx.send(message, files=[await a.to_file() for a in ctx.message.attachments])
        
        try:
            await reply.reply(message, files=[await a.to_file() for a in ctx.message.attachments])
        except disnake.HTTPException:
            await ctx.send(message, files=[await a.to_file() for a in ctx.message.attachments])

def setup(client):
    client.add_cog(Echo(client))
