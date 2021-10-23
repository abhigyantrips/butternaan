import disnake
from disnake.ext import commands
from disnake import Option, SlashCommand, ApplicationCommandInteraction

test_guilds=[860414380444483584]

class Moderator(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    ### KICK ###

    @commands.slash_command(
        name = "kick",
        description = "Kicks a user.",
        options = [
            Option(
                name = "user",
                description = "The user to be kicked.",
                type = 6,
                required = True
            ),
            Option(
                name = "reason",
                description = "Enter the reason of kicking the user. (Will be attached in DMs.)",
                type = 3,
                required = False
            )
        ],
        guild_ids = test_guilds
    )
    async def kick(self, ctx, user, reason=None):
        
        if reason == None or ' ':
            await user.send(f"You got kicked lel. \n**No reason given, git gud.**")
            await ctx.response.send_message(f"Alrighty, kicked **{user}**. \n**No reason given.**")
        else:
            await user.send(f"You got kicked lel. \n**Reason:** {reason}")
            await ctx.response.send_message(f"Alrighty, kicked **{user}**. \n**Reason:** {reason}")
        
        await ctx.guild.kick(user, reason = reason)



def setup(client):
    client.add_cog(Moderator(client))