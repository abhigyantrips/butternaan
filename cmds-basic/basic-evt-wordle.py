import disnake
from disnake.ext import commands
from disnake.utils import get

from datetime import datetime


def wordle_day():
    today = datetime.today()
    anchor = datetime(2021, 6, 19)
    return (today - anchor).days


class Wordle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.channel.type != disnake.ChannelType.text:
            return

        if (message.channel.name != "wordle") or (message.author.bot):
            return


def setup(client):
    client.add_cog(Wordle(client))
