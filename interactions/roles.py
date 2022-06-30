import disnake
from disnake.ext import commands

ROLES = {
    "He/Him": 840617596474753055,
    "She/Her": 840617643517542421,
    "They/Them": 840617669333745694,
}


class Roles(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command()
    async def pronouns(
        self, ctx: disnake.CommandInteraction, role: str = commands.Param(choices=ROLES.keys())
    ):
        """Choose a pronoun role to be displayed on your profile.

        Parameters
        ----------
        role: The pronoun role to be displayed."""
        pronoun = disnake.utils.get(ctx.guild.roles, id=ROLES[role])

        if pronoun in ctx.author.roles:
            await ctx.author.remove_roles(pronoun)
            await ctx.response.send_message(
                f"{pronoun.mention} has been removed from your profile.", ephemeral=True
            )
        else:
            await ctx.author.add_roles(pronoun)
            await ctx.response.send_message(
                f"{pronoun.mention} has been added to your profile.", ephemeral=True
            )


def setup(client):
    client.add_cog(Roles(client))
