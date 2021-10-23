import disnake
from disnake.ext import commands
from disnake.utils import get
from disnake import SlashCommand, Option, OptionType, OptionChoice, ApplicationCommandInteraction

import os
import requests

class Funni(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    test_guilds = [860414380444483584]

    @commands.slash_command(
        name = "ping",
        description = "Gives the ping, I guess.",
        guild_ids = test_guilds
    )
    async def ping(self, ctx: ApplicationCommandInteraction):
        await ctx.response.send_message("I'm not here to play table-tennis, dumbass.")
    
    @commands.command()
    async def echo(self, ctx, member: disnake.Member, *, content):

        await ctx.message.delete()
        current_webhooks = await ctx.message.channel.webhooks()
        new_webhook = ''
        webhook_count = []
        for webhook in current_webhooks:
            if webhook.name == "Butternaan Webhook":
                webhook_count.append(webhook)
        if (len(webhook_count) > 1):
            new_webhook = await ctx.message.channel.create_webhook(name='Butternaan Webhook', reason="Bot Webhook")
            for webhook in webhook_count:
                await webhook.delete()
        elif len(webhook_count) == 0:
            new_webhook = await ctx.message.channel.create_webhook(name='Butternaan Webhook', reason="Bot Webhook")
        elif len(webhook_count) == 1:
            for webhook in webhook_count:
                new_webhook = webhook
        await new_webhook.send(content=content, username=member.display_name, avatar_url=member.avatar)

def setup(client):
    client.add_cog(Funni(client))