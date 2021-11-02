import disnake
from disnake import ApplicationCommandInteraction
from disnake.ext import commands

class HelpCommand(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command(name = 'help')
    async def helpcmd(self, ctx):
        await ctx.send("Help yourself.")
    
    @commands.slash_command(
        name = 'help',
        description = 'Guess what this does.'
    )
    async def helpslash(self, ctx: ApplicationCommandInteraction):
        await ctx.response.send_message("Help yourself.", ephemeral = True)


def setup(client):
    client.add_cog(HelpCommand(client))