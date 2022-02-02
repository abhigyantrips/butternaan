import disnake
from disnake.ext import commands
from disnake.utils import get

import os

class DMs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if (message.channel.type != disnake.ChannelType.private) or (not message.content) or (message.author.bot):
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
    async def reply(self, ctx, user: disnake.Member, *, message):
        try:

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



def setup(client):
    client.add_cog(DMs(client))
