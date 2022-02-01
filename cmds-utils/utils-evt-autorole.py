import disnake
from disnake.ext import commands
from disnake.utils import get

import os

class AutoRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):

        if member.guild.id != os.environ.get("TEST_GUILDS_ONE"):
            return
        
        if member.bot:
            bot_role = get(member.guild.roles, name="◍ • Bots")
            await member.add_roles(bot_role)



def setup(client):
    client.add_cog(AutoRole(client))
