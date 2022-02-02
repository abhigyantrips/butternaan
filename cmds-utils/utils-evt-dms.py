import disnake
from disnake.ext import commands
from disnake.utils import get

import os

class DMs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if (message.channel.type != disnake.ChannelType.private) or (not message.content):
            return

        guild = get(self.client.guilds, id=int(os.environ.get("TEST_GUILDS_ONE")))
        staff_channel = get(guild.channels, name="staff-chat")

        embed = disnake.Embed(
            description=message.content,
            color=0x303136,
            timestamp=message.created_at,
        )

        embed.set_author(name=message.author, icon_url=message.author.avatar)

        await staff_channel.send(embed=embed)



def setup(client):
    client.add_cog(DMs(client))
