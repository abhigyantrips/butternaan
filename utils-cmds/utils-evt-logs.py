import disnake
from disnake.ext import commands

class EventLogging(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        if before.author.bot:
            return

        embed = disnake.Embed(
        title = "Message Edited.",
        color = 0x303136,
        description = f"A message by {before.author.mention} was edited in {before.channel.mention}."
        )

        embed.set_thumbnail(url = before.author.avatar)

        embed.add_field(name = "Before", value = before.content, inline = False)
        embed.add_field(name = "After", value = after.content, inline = False)

        await self.client.get_channel(891527413866053653).send(embed = embed) # The ID refers to the server log in my server.

    @commands.Cog.listener()
    async def on_message_delete(self, message):

        async for entry in message.guild.audit_logs(limit = 1, action = disnake.AuditLogAction.message_delete):
            deleter = entry.user

        if deleter == message.author:
            desc = f"{message.author.mention} deleted their message in {message.channel.mention}."
        else:
            desc = f"A message by {message.author.mention} was deleted in {message.channel.mention} by {deleter.mention}."

        embed = disnake.Embed(
            title = "Message Deletion.",
            color = 0x303136,
            description = desc
        )

        embed.set_thumbnail(url = message.author.avatar)

        if message.reference is not None and not message.is_system:
            ref_msg = client.get_message(message.reference.id)
            embed.add_field(name = f"Replying to {ref_msg.author.mention}", value = ref_msg.content, inline = False)
        
        embed.add_field(name = f"Deleted Message", value = message.content, inline = False)

        await self.client.get_channel(891527413866053653).send(embed = embed) # The ID refers to the server log in my server.

def setup(client):
    client.add_cog(EventLogging(client))