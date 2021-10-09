import disnake
from disnake.ext import commands
from disnake import Option, OptionType, OptionChoice, ApplicationCommandInteraction

import requests, json

test_guilds = [860414380444483584]

india_states = ['Andhra Pradesh', 'Arunachal Pradesh ', 'Assam', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Odisha', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal', 'Andaman and Nicobar Islands', 'Chandigarh', 'Lakshadweep', 'Delhi']

class COVID(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def autocomp_states(ctx: ApplicationCommandInteraction, user_input: str):
        return [state for state in india_states if (user_input.lower() in state) or (user_input in state)]

    @commands.slash_command()
    async def covid(self, ctx: ApplicationCommandInteraction):
        pass

    @covid.sub_command(
        name = 'stats',
        description = 'Get statistics on COVID cases, per state.',
        guild_ids = test_guilds
    )
    async def _stats(
        self, ctx: ApplicationCommandInteraction, 
        state: str = commands.Param(desc = 'Enter the State/UT to get info on.', autocomp = autocomp_states)
    ):
        
        covidjson = json.loads(requests.get('https://api.rootnet.in/covid19-in/stats/latest/').text)

        embed = disnake.Embed(
            title = 'COVID Statistics',
            description = 'Fetched from [this API](https://api.rootnet.in/covid19-in/stats/latest/).',
            color = 0x303136
        )

        if covidjson['success']:
            jsonstate = list(covidjson['data']['regional'])
            for state_ut in jsonstate:   
                if state_ut['loc'] == state:
                    embed.add_field(name = 'Confirmed Cases (Indian)', value = state_ut['confirmedCasesIndian'], inline = True)
                    embed.add_field(name = 'Confirmed Cases (Foreign)', value = state_ut['confirmedCasesForeign'], inline = True)
                    embed.add_field(name = 'Patients Discharged', value = state_ut['discharged'], inline = False)
                    embed.add_field(name = 'Deaths', value = state_ut['deaths'], inline = True)
                    embed.add_field(name = 'Total Confirmed', value = state_ut['totalConfirmed'], inline = True)
        else:
            embed.add_field(name = 'API Status Error', value = 'Unable to access API at this time.')

        embed.set_thumbnail('https://i.imgur.com/C3nRUXM.jpeg')
        embed.set_footer(text = f'Requested by {ctx.author.name} [{ctx.author.id}]')
        await ctx.response.send_message(content = f'Statistics for **{state}**', embed = embed)
    
    @covid.sub_command(
        name = 'resources',
        description = 'Information regarding Hospitals, Beds & Contacts, per state.',
        guild_ids = test_guilds
    )
    async def _resources(
        self, ctx: ApplicationCommandInteraction,
        state: str = commands.Param(desc='Enter the State/UT to get info on.', autocomp = autocomp_states)
    ):
        
        contactjson = json.loads(requests.get('https://api.rootnet.in/covid19-in/contacts/').text)
        resourcejson = json.loads(requests.get('https://api.rootnet.in/covid19-in/hospitals/beds').text)

        embed = disnake.Embed(
            title = 'COVID Statistics',
            description = 'Fetched from [this API](https://api.rootnet.in/covid19-in/stats/latest/).',
            color = 0x303136
        )

        if contactjson['success'] and resourcejson['success']:
            contactstate = list(contactjson['data']['contacts']['regional'])
            for state_ut in contactstate:   
                if state_ut['loc'] == state:
                    embed.add_field(name = f'Local Contact Helpline', value = f'{state} - {state_ut["number"]}', inline = False)
                    embed.add_field(name = f'National Contact Helpine', value = f'```\nNumber: {contactjson["data"]["contacts"]["primary"]["number"]}\nToll-free: {contactjson["data"]["contacts"]["primary"]["number-tollfree"]}\nE-mail: {contactjson["data"]["contacts"]["primary"]["email"]}```', inline = False)
            hospbedstate = list(resourcejson['data']['regional'])
            for state_ut in hospbedstate:   
                if state_ut['state'] == state:
                    embed.add_field(name = f'Available Hospitals & Beds', value = f'```Total Hospitals: {state_ut["totalHospitals"]}\n(Urban - {state_ut["urbanHospitals"]}; Rural - {state_ut["ruralHospitals"]})\nTotal Beds: {state_ut["totalBeds"]}\n(Urban - {state_ut["urbanBeds"]}; Rural - {state_ut["ruralBeds"]})```', inline = False)
        else:
            embed.add_field('API Status Error', 'Unable to access API at this time.')

        embed.set_thumbnail('https://i.imgur.com/vEp2BW7.jpeg')
        embed.set_footer(text = f'• Requested by {ctx.author.name} [{ctx.author.id}]')
        await ctx.response.send_message(content = f'Resources/Contacts for **{state}**', embed = embed)

def setup(client):
    client.add_cog(COVID(client))