import disnake
from disnake.ext import commands
from disnake import Option, OptionType, OptionChoice, ApplicationCommandInteraction

import os, requests, json
    
test_guilds = [860414380444483584]

WEATHER_API_KEY = os.environ.get('WEATHER_API_KEY')

class Weather(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def autocomp_weather(ctx: ApplicationCommandInteraction, user_input: str):

        if user_input != '' or None:
            autocompjson = list(json.loads(requests.get(f'http://api.weatherapi.com/v1/search.json?key={WEATHER_API_KEY}&q={user_input}').text))
            autocomplist = []
            for result in autocompjson:
                autocomplist.append(result['name'])
                if len(autocomplist) == 10:
                    break
            return autocomplist
    
    @commands.slash_command()
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def weather(self, ctx: ApplicationCommandInteraction):
        pass

    @weather.sub_command(
        name = 'info',
        description = 'Gives information about the weather at an entered location',
        guild_ids = test_guilds
    )
    async def _forecast(
        self, ctx: ApplicationCommandInteraction,
        location: str = commands.Param(desc = 'Enter the location to get info on.', autocomp = autocomp_weather)
    ):

        weatherjson = json.loads(requests.get(f'http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={location}&aqi=yes').text)

        embed = disnake.Embed(
            title = 'Weather Forecast',
            description = f'Showing data for **{location}**.',
            color = 0x303136
        )
        embed.add_field(name = 'Temperature', 
                        value = f'`{weatherjson["current"]["temp_c"]} °C - {weatherjson["current"]["temp_f"]} °F`', 
                        inline = False)
        embed.add_field(name = 'Condition', 
                        value = f'{(weatherjson["current"]["condition"]["text"]).capitalize()}', 
                        inline = True)
        embed.add_field(name = 'Humidity', 
                        value = f'{weatherjson["current"]["humidity"]}%', 
                        inline = True)        
        embed.add_field(name = 'Wind Speed', 
                        value = f'{weatherjson["current"]["wind_mph"]} MPH - {weatherjson["current"]["wind_kph"]} KMPH', 
                        inline = False)
        embed.add_field(name = 'Wind Degree, Direction', 
                        value = f'{weatherjson["current"]["wind_degree"]}° - {weatherjson["current"]["wind_dir"]}', 
                        inline = False)
        embed.add_field(name = 'Air Quality', 
                        value = f'```PM 2.5: {round(weatherjson["current"]["air_quality"]["pm2_5"], 1)}\nPM 10: {round(weatherjson["current"]["air_quality"]["pm10"], 1)}```', 
                        inline = False)
        embed.set_thumbnail(url = ("http:" + (weatherjson["current"]["condition"]["icon"])))
        
        await ctx.response.send_message(embed = embed)


    
def setup(client):
    client.add_cog(Weather(client))