import asyncio
import os
from datetime import datetime

from aiohttp import ClientSession
from disnake import AllowedMentions, Embed, Intents
from disnake.ext import commands

from . import constants


class Bot(commands.Bot):
	"""The core of the bot."""

	def __init__(self) -> None:
		intents = Intents.default()
		intents.members = True
		intents.message_content = True
		intents.presences = True

		self.http_session = ClientSession()

		test_guilds = None
		if constants.TEST_GUILDS:
			test_guilds = constants.TEST_GUILDS

		super().__init__(
			command_prefix=constants.PREFIX,
			intents=intents,
			allowed_mentions=AllowedMentions(
				everyone=None,
				users=True,
				replied_user=True,
			),
			reload=True
		)

		self.initiated = False

	def load_extensions(self) -> None:
		"""Load all extensions from the exts/ folder."""
		print("\n")
		for extension in constants.EXTENSIONS.glob("*/*.py"):
			if extension.name.startswith("_"):
				continue # ignore underscored files
			ext_path = str(extension).replace(os.sep, ".")[:-3] # truncate .py
			self.load_extension(ext_path)
			print(f"|  Loaded {ext_path}.")

	def run(self) -> None:
		"""Run the bot with token present in .env."""
		if constants.BOT_TOKEN is None:
			raise EnvironmentError(
				"Token value is None. Make sure you have configured the TOKEN field in .env"
			)

		super().run(constants.BOT_TOKEN)

	async def on_ready(self) -> None:
		"""Runs the bot when connected to Discord and is ready."""
		if not self.initiated:
			await asyncio.sleep(2)
			self.load_extensions()
			await self.starup_alert()
			self.initiated = True
		print("The bot is online!")

	async def startup_alert(self) -> None:
		"""Announce the bot's presence in the staff chat."""
		embed = Embed(
			title="Bot Startup",
			description="The bot is back online!",
			color=constants.Colors.green,
			timestamp=datetime.now(),
		)
		await self.get_channel(constants.Channels.log).send(embed=embed)

	async def close(self) -> None:
		"""Close the bot gracefully."""
		await super().close()