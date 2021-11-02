import disnake
from disnake.ext import commands
from disnake import Option, OptionType

import requests, json

class GitHub(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(
        name = 'github', 
        description = 'Gets a GitHub user\'s info', 
        options = [
            Option(
                name = 'user',
                description = 'Enter the username. (Don\'t mess this up.)', 
                type = OptionType.string, 
                required = True)
        ]
    )
    async def github(self, ctx: disnake.ApplicationCommandInteraction, user: str):
    
        githuburl = requests.get(f'https://api.github.com/users/{user}') 

        githubjson = json.loads(githuburl.text)    
        
        embed = disnake.Embed(
        title = 'GitHub', 
        description = f'{user}\'s Profile', 
        color = 0x303136
        )
        embed.add_field(name = 'Name', value = githubjson["name"], inline = True)
        embed.add_field(name = 'Location', value = githubjson["location"], inline = True)
        embed.add_field(name = 'Website', value = f'https://{githubjson["blog"]}/', inline = False)
        embed.add_field(name = 'Twitter', value = f'`@{githubjson["twitter_username"]}`', inline = True)
        embed.add_field(name = 'Followers', value = f'**{githubjson["followers"]}**', inline = True)
        embed.add_field(name = 'Following', value = f'**{githubjson["following"]}**', inline = True)
        embed.add_field(name = 'Bio', value = githubjson["bio"], inline = False)
        embed.add_field(name = 'Repos', value = githubjson["public_repos"], inline = True)
        embed.add_field(name = 'Gists', value = githubjson["public_gists"], inline = True)
        embed.set_thumbnail(url = githubjson["avatar_url"])

        await ctx.response.send_message(content = f'<{githubjson["html_url"]}>', embed = embed)

def setup(client):
    client.add_cog(GitHub(client))