import disnake
from disnake.ext import commands
from disnake.utils import get

import os

class AutoRole(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: disnake.Member):

        if member.guild.id != int(os.environ.get("TEST_GUILDS_ONE")):
            return
        
        if member.bot:
            bot_role = get(member.guild.roles, name="◍ • Bots")
            await member.add_roles(bot_role)
    
    @commands.Cog.listener()
    async def on_member_update(self, before: disnake.Member, after: disnake.Member):

        if (before.guild.id != int(os.environ.get("TEST_GUILDS_ONE")) or (before.bot)):
            return

        if before.pending and not after.pending:
            member_role = get(after.guild.roles, name="▧ • Members")
            await after.add_roles(member_role)


def setup(client):
    client.add_cog(AutoRole(client))
