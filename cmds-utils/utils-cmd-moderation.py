import disnake
from disnake.ext import commands
from disnake import Option, OptionType, ChannelType, ApplicationCommandInteraction

from datetime import datetime, timedelta


class Moderation(commands.Cog):
    def __init__(self, client):
        """Moderation-related commands."""
        self.client = client

    """All commands are registered under the 'mod' group."""

    @commands.slash_command(name="mod", description="Moderation-related commands.")
    async def mod(self, ctx: ApplicationCommandInteraction):
        pass

    ### PURGE & PRUNE ###

    @mod.sub_command(
        name="purge",
        description="Deletes the specified number of messages in the channel.",
        options=[Option("amount", "Amount of messages to be cleared.", OptionType.integer, True)],
    )
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def purge(self, ctx: ApplicationCommandInteraction, amount):

        if amount >= 100:
            return await ctx.response.send_message(
                "You're asking me to delete too many messages at once, mate."
            )

        await ctx.response.send_message("Purging messages in progress...", ephemeral=True)
        await ctx.channel.purge(limit=amount)
        await ctx.edit_original_message(content=f"Successfully purged {amount} messages.")

    @mod.sub_command(
        name="prune",
        description="Purges all messages from a user in the last 24 hours.",
        options=[Option("user", "The user to delete messages of.", OptionType.user, True)],
    )
    @commands.bot_has_permissions(manage_messages=True)
    async def prune(self, ctx: ApplicationCommandInteraction, user: disnake.Member):

        await ctx.response.send_message(f"Deleting messages from `{user}` in the last 24 hours.")

        channels = ctx.guild.text_channels
        deleted = []
        for channel in channels:
            deleted += await channel.purge(
                limit=None,
                check=lambda m: m.author == user,
                after=datetime.now() - timedelta(days=1),
            )

        await ctx.edit_original_message(content=f"Deleted **{len(deleted)}** messages by `{user}`.")

    @mod.sub_command(
        name="channel-prune",
        description="Purges all messages from a user in the last 24 hours. (In specified channel.)",
        options=[
            Option("user", "The user to delete messages of.", OptionType.user, True),
            Option(
                "channel",
                "Channel to delete messages from.",
                OptionType.channel,
                True,
                None,
                None,
                [ChannelType.text],
            ),
        ],
    )
    @commands.bot_has_permissions(manage_messages=True)
    async def channelprune(
        self,
        ctx: ApplicationCommandInteraction,
        user: disnake.Member,
        channel: disnake.TextChannel,
    ):

        await ctx.response.send_message(f"Deleting messages from `{user}` in the last 24 hours.")

        deleted = []
        deleted += await channel.purge(
            limit=None,
            check=lambda m: m.author == user,
            after=datetime.now() - timedelta(days=1),
        )

        await ctx.edit_original_message(
            content=f"Deleted **{len(deleted)}** messages by `{user}` in {channel.mention}."
        )


def setup(client):
    client.add_cog(Moderation(client))
