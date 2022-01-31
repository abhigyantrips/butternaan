import disnake
from disnake.ext import commands
from disnake.utils import get
from disnake import (
    SlashCommand,
    Option,
    OptionType,
    OptionChoice,
    ApplicationCommandInteraction,
)



class Letterle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if (message.channel.name != "letterle") or ("https://edjefferson.com/letterle/" not in message.content):
            return
            
        await message.delete()
        
        current_webhooks = await message.channel.webhooks()
        
        for webhook in current_webhooks:
            if webhook.user.id == self.client.user.id and webhook.name == "Butternaan Webhook":
                return await webhook.send(
                    content=(message.content.replace("https://edjefferson.com/letterle/", "")),
                    username=message.author.display_name,
                    avatar_url=message.author.display_avatar,
                )
        
        webhook = await message.channel.create_webhook(name="Butternaan Webhook", reason="Butternaan bhook")
        await webhook.send(
            content=(message.content.replace("https://edjefferson.com/letterle/", "")),
            username=message.author.display_name,
            avatar_url=message.author.display_avatar,
        )


def setup(client):
    client.add_cog(Letterle(client))
