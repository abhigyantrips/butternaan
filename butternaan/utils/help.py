import disnake
from disnake.ext import commands


class Help(commands.Cog):
	"""Information and statistics about the bot."""

	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(3, 15)
	async def help(self, ctx: commands.Context) -> None:
		"""A very helpful command."""
		await ctx.send("Help yourself.")

	@commands.command()
	@commands.cooldown(2, 15)
	async def help(self, ctx: commands.Context) -> None:
		"""Returns the latency of the bot."""
		await ctx.send(f"Pong. Gateway latency is around {round(self.bot.latency*1000)}ms.")

def setup(bot: commands.Bot) -> None:
	"""Loads the Help cog."""
	bot.add_cog(Help(bot))