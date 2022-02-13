import datetime

import disnake
from disnake.ext import commands
from disnake.enums import TextInputStyle

class ExampleModal(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.slash_command()
	async def modal(self, ctx: disnake.ApplicationCommandInteraction):
		"""A test modal, with basic attributes."""
		await ctx.response.send_modal(
			title="Modal Title",
			custom_id="modal",
			components=[
				disnake.ui.TextInput(
					label="Short Text Input",
					custom_id="short_text_input",
					placeholder="Short Text Placeholder",
					style=TextInputStyle.short,
					max_length=50
				),
				disnake.ui.TextInput(
					label="Long Text Input",
					custom_id="long_text_input",
					placeholder="Long Text Placeholder",
					style=TextInputStyle.short,
					max_length=1024
				),
			],
		)

		modal_inter: disnake.ModalInteraction = await self.client.wait_for(
			"modal_submit",
			check=lambda modal: modal.custom_id == "modal" and modal.author.id == inter.author.id,
			timeout=300,
		)

		embed = disnake.Embed(title="Modal Test", color=0x303136, timestamp=datetime.datetime.now())
		for key, value in modal_inter.text_values.items():
			embed.add_field(name=key.capitalize(), value=value[:1024], inline=False)
		await modal_inter.response.send_message(embed=embed)

def setup(client):
	client.add_cog(ExampleModal(client))
