import disnake
from disnake.ext import commands

import os

from imgurpython import ImgurClient


def upload_image(images):

    imgur_client = ImgurClient(
        client_id=os.environ.get("IMGUR_API_ID"),
        client_secret=os.environ.get("IMGUR_API_SC"),
    )

    links = []

    for image in images:

        response = imgur_client.upload_from_url(image, anon=True)

        links.append(response["link"])

    return "\n".join(links)


class Imgur(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def imgur(self, ctx):

        try:

            files = ctx.message.attachments
            link = upload_image(files)

            embed = disnake.Embed(
                title="Image Uploaded.",
                description="The image has been successfully uploaded, and the link has been copied to your clipboard.",
                color=0x303136,
            )

            msg_content = "**Upload Success.**"
            embed.add_field(name="Imgur Link(s)", value=link)
            embed.set_image(url=link)
            embed.set_footer(text=f"Requested by {ctx.message.author} [{ctx.message.author.id}]")

        except:

            embed = disnake.Embed(
                title="Image Upload Failure.",
                description="Either the file format is unsupported, or the API could not be reached a this time.",
                color=0x303136,
            )

            msg_content = "**Upload Failure.**"
            embed.set_footer(text=f"Requested by {ctx.message.author} [{ctx.message.author.id}]")

        await ctx.message.delete()
        await ctx.send(content=msg_content, embed=embed)


def setup(client):
    client.add_cog(Imgur(client))
