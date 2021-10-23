import disnake
from disnake.ext import commands
from disnake import Option, OptionChoice, OptionType, ApplicationCommandInteraction

class Activities(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name = "activity",
        description = "Use Discord Activities.",
        options = [
            Option(
                name = "vc_channel", 
                description = "The channel to stream the activity in.", 
                type = OptionType.channel,
                channel_types = [disnake.ChannelType.voice], 
                required = True),
            Option(
                name = "activity", 
                description = "The type of activity to stream.", 
                type = OptionType.string,
                choices = [
                    OptionChoice('YouTube Together', 'YouTube Together'),
                    OptionChoice('Poker Night', 'Poker Night'),
                    OptionChoice('Betrayal.IO', 'Betrayal.IO'),
                    OptionChoice('Fishington.IO', 'Fishington.IO'),
                    OptionChoice('Chess In the Park', 'Chess In The Park')
                ],
                required = True)
        ]
    )
    async def activities(self, ctx: ApplicationCommandInteraction, vc_channel: disnake.VoiceChannel, activity):

        if activity == 'YouTube Together':
            act_val = disnake.PartyType.youtube
        elif activity == 'Poker Night':
            act_val = disnake.PartyType.poker
        elif activity == 'Betrayal.IO':
            act_val = disnake.PartyType.betrayal
        elif activity == 'Fishington.IO':
            act_val = disnake.PartyType.fishing
        elif activity == 'Chess In The Park':
            act_val = disnake.PartyType.chess
        
        link = await vc_channel.create_invite(target_type = disnake.InviteTarget.embedded_application, target_application = act_val)
        await ctx.response.send_message(f"Here's the link for {activity} - {link}", ephemeral = True)

def setup(client):
    client.add_cog(Activities(client))