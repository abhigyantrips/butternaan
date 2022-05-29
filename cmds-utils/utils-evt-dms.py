import disnake
from disnake.ext import commands
from disnake.utils import get

import os


# async def is_owner(ctx):
#     return ctx.author.id == 434621628152938497


class DMs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if (
            (message.channel.type != disnake.ChannelType.private)
            or (not message.content)
            or (message.author.bot)
        ):
            return

        guild = get(self.client.guilds, id=int(os.environ.get("TEST_GUILDS_ONE")))
        staff_channel = get(guild.channels, name="bot-messages")

        embed = disnake.Embed(
            description=message.content,
            color=0x303136,
            timestamp=message.created_at,
        )

        embed.set_author(name=message.author, icon_url=message.author.avatar)

        await staff_channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def message(self, ctx, user: disnake.Member, *, message):
        try:

            await ctx.message.delete()

            channel = await user.create_dm()
            sent_message = await channel.send(message)

            embed = disnake.Embed(
                description=sent_message.content,
                color=0x303136,
                timestamp=sent_message.created_at,
            )

            embed.set_author(name=self.client.user, icon_url=self.client.user.avatar)
            embed.set_footer(text=f"{ctx.author.name} -> {user.name}", icon_url=ctx.author.avatar)

            await ctx.send(embed=embed)

        except Exception as e:

            await ctx.send(f"Could not send message to user.\n```{e}```")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def fetch(self, ctx, user: disnake.Member):
        try:

            await ctx.message.delete()

            channel = await user.create_dm()
            history = ""

            async for message in channel.history(limit=20):
                history += f"{message.author.name} [{message.created_at}] - {message.content}\n"

            await ctx.send(f"**Requested by {ctx.author}**\n```{history}```")

        except Exception as e:

            await ctx.send(f"Could not send message to user.\n```{e}```")


def setup(client):
    client.add_cog(DMs(client))
