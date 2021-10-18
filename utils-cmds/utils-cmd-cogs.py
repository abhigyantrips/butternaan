import disnake
from disnake import Option, OptionType, OptionChoice, ApplicationCommandInteraction
from disnake.ext import commands

class CogLoad(commands.Cog):

    def __init__(self, client):
        self.client = client
    

def setup(client):
    client.add_cog(CogLoad(client))