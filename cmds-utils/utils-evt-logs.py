import disnake
from disnake.ext import commands

import os
import time
import datetime
import typing


class Logs(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message: disnake.Message):

        if (
            (message.guild.id != int(os.getenv("TEST_GUILDS_ONE")))
            or (message.author.bot)
            or (not message.content)
        ):
            return

        if message.channel.name == "uwuchat":
            return

        log_channel = disnake.utils.get(message.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Message Deleted.",
            description=f"Message by {message.author.mention} in {message.channel.mention} was deleted.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        embed.add_field(
            name="Content",
            value=message.content or "None",
            inline=False,
        )
        embed.add_field(
            name="Timestamp",
            value=f"<t:{round(time.mktime(message.created_at.timetuple()))}:f>",
            inline=False,
        )

        if message.reference:
            reference = self.client.fetch_message(message.reference.message_id)
            embed.add_field(
                name="Reference",
                value=f"{reference.author.mention} - {reference.content}",
                inline=False,
            )

        if message.attachments:
            embed.set_image(url=message.attachments[0].url)

        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_message_edit(self, before: disnake.Message, after: disnake.Message):

        if (
            (before.guild.id != int(os.getenv("TEST_GUILDS_ONE")))
            or (before.author.bot)
            or (not before.content)
            or (before.content == after.content)
        ):
            return

        log_channel = disnake.utils.get(before.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Message Edited.",
            description=f"Message by {before.author.mention} in {before.channel.mention} was edited.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        embed.add_field(
            name="Before",
            value=before.content or "None",
            inline=False,
        )
        embed.add_field(
            name="After",
            value=after.content or "None",
            inline=False,
        )
        embed.add_field(
            name="Timestamp",
            value=f"<t:{round(time.mktime(after.created_at.timetuple()))}:f>",
            inline=False,
        )
        embed.add_field(
            name="Edited",
            value=f"<t:{round(time.mktime(after.edited_at.timetuple()))}:f>",
            inline=False,
        )

        if before.reference:
            reference = self.client.fetch_message(before.reference.message_id)
            embed.add_field(
                name="Reference",
                value=f"{reference.author.mention} - {reference.content}",
                inline=False,
            )

        if before.attachments:
            embed.set_image(url=before.attachments[0].url)

        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_clear(
        self, message: disnake.Message, reactions: typing.List[disnake.Reaction]
    ):

        if (
            (message.guild.id != int(os.getenv("TEST_GUILDS_ONE")))
            or (message.author.bot)
            or (not message.content)
            or (not reactions)
        ):
            return

        log_channel = disnake.utils.get(message.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Reactions Cleared.",
            description=f"Reactions on the message by {message.author.mention} in {message.channel.mention} were cleared.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        embed.add_field(
            name="Content",
            value=message.content or "None",
            inline=False,
        )
        embed.add_field(
            name="Reactions",
            value=" ".join(str(reaction.emoji) for reaction in reactions),
            inline=False,
        )

        if message.reference:
            reference = self.client.fetch_message(message.reference.message_id)
            embed.add_field(
                name="Reference",
                value=f"{reference.author.mention} - {reference.content}",
                inline=False,
            )

        if message.attachments:
            embed.set_image(url=message.attachments[0].url)

        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: disnake.abc.GuildChannel):

        if channel.guild.id != int(os.getenv("TEST_GUILDS_ONE")):
            return

        async for entry in channel.guild.audit_logs(
            limit=1, action=disnake.AuditLogAction.channel_create
        ):
            entry = entry

        log_channel = disnake.utils.get(channel.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Channel Created.",
            description=f"A channel {channel.mention} was created by {entry.user.mention}.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        embed.add_field(
            name="Name",
            value=channel.name,
            inline=False,
        )
        embed.add_field(
            name="Position",
            value=f"Category - {channel.category.name}; Position - {channel.position}",
            inline=False,
        )
        embed.add_field(
            name="Created",
            value=f"<t:{round(time.mktime(channel.created_at.timetuple()))}:f>",
            inline=False,
        )

        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel: disnake.abc.GuildChannel):

        if channel.guild.id != int(os.getenv("TEST_GUILDS_ONE")):
            return

        async for entry in channel.guild.audit_logs(
            limit=1, action=disnake.AuditLogAction.channel_delete
        ):
            entry = entry

        log_channel = disnake.utils.get(channel.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Channel Deleted.",
            description=f"A channel #{channel.name} was deleted by {entry.user.mention}.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        embed.add_field(
            name="Name",
            value=channel.name,
            inline=False,
        )
        embed.add_field(
            name="Position",
            value=f"Category - {channel.category.name}; Position - {channel.position}",
            inline=False,
        )
        embed.add_field(
            name="Created",
            value=f"<t:{round(time.mktime(channel.created_at.timetuple()))}:f>",
            inline=False,
        )

        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_update(
        self, before: disnake.abc.GuildChannel, after: disnake.abc.GuildChannel
    ):

        if before.guild.id != int(os.getenv("TEST_GUILDS_ONE")):
            return

        async for entry in before.guild.audit_logs(
            limit=1, action=disnake.AuditLogAction.channel_update
        ):
            entry = entry

        log_channel = disnake.utils.get(before.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Channel Updated.",
            description=f"A channel {before.mention} was updated by {entry.user.mention}.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        if before.name != after.name:
            embed.add_field(
                name="Name",
                value=f"Before: {before.name}\nAfter: {after.name}",
                inline=False,
            )

        if before.category != after.category:
            embed.add_field(
                name="Category",
                value=f"Before: {before.category.name}\nAfter: {after.category.name}",
                inline=False,
            )

        if before.position != after.position:
            embed.add_field(
                name="Position",
                value=f"Before: {before.position} from top.\nAfter: {after.position} from top.",
                inline=False,
            )

        if before.changed_roles != after.changed_roles:
            embed.add_field(
                name="Changed Roles",
                value="\n".join(role.mention for role in before.changed_roles),
                inline=False,
            )

        if embed.fields == disnake.Embed.Empty:
            return

        await log_channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_thread_join(self, thread: disnake.Thread):

        if thread.guild.id != int(os.getenv("TEST_GUILDS_ONE")):
            return

        log_channel = disnake.utils.get(thread.guild.channels, name="bot-logs")

        embed = disnake.Embed(
            title="Thread Created.",
            description=f"A thread {thread.mention} was created by {thread.owner.mention}.",
            color=0x303136,
            timestamp=datetime.datetime.now(),
        )

        embed.add_field(
            name="Name",
            value=thread.name,
            inline=False,
        )
        embed.add_field(
            name="Archived",
            value=thread.archived,
            inline=True,
        )
        embed.add_field(
            name="Locked",
            value=thread.locked,
            inline=True,
        )
        embed.add_field(
            name="Invitable",
            value=thread.invitable,
            inline=True,
        )
        embed.add_field(
            name="Channel",
            value=thread.parent.mention,
            inline=False,
        )
        embed.add_field(
            name="Created",
            value=f"<t:{round(time.mktime(thread.created_at.timetuple()))}:f>",
            inline=False,
        )

        await log_channel.send(embed=embed)


def setup(client):
    client.add_cog(Logs(client))
