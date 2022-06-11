import disnake
from disnake import ApplicationCommandInteraction, Option, OptionType
from disnake.ext import commands


class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.user_command(name="Avatar")
    async def avatar(self, inter: disnake.ApplicationCommandInteraction):
        embed = disnake.Embed(title=f"{inter.target.name}'s avatar", color=0x303136)
        embed.set_image(url=inter.target.display_avatar.url)
        await inter.response.send_message(embed=embed)


def setup(client):
    client.add_cog(Avatar(client))
