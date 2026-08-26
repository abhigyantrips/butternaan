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

		