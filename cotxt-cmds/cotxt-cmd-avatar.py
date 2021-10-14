import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands

import os

TEST_GUILDS = [int(os.environ.get('TEST_GUILDS'))]

class Reverse(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.user_command(name="Avatar", guild_ids=TEST_GUILDS) # optional
    async def avatar(self, inter: disnake.ApplicationCommandInteraction):
        # inter.target is the user you clicked on
        emb = disnake.Embed(title=f"{inter.target.name}'s avatar")
        emb.set_image(url=inter.target.display_avatar.url)
        await inter.response.send_message(embed=emb)

def setup(client):
    client.add_cog(Reverse(client))