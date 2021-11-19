import disnake
from disnake import Option, OptionType, OptionChoice, ApplicationCommandInteraction
from disnake.ext import commands

from datetime import datetime, timedelta, timezone
import asyncio, time


def validate_time(sesh_time):
    if len(sesh_time) != 5:
        return "Invalid time format."
    else:
        if int(sesh_time[0:2]) > 24:
            return "Invalid HOUR format."
        elif int(sesh_time[3:5]) > 59:
            return "Invalid MINUTE format."
        else:
            return "Ok."


class Sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    #### 1ST SESSION ####

    @commands.slash_command(
        name="sessions",
        description="Set a reminder for a Vedantu/Unacademy session.",
        options=[
            Option(
                name="sesh_time",
                description="Enter time in 'HH:MM AM/PM' format.",
                type=OptionType.string,
                required=True,
            ),
            Option(
                name="sesh_name",
                description="Name of the session.",
                type=OptionType.string,
                required="true",
            ),
        ],
    )
    async def sessions(self, ctx: ApplicationCommandInteraction, sesh_time, sesh_name):

        validate = validate_time(sesh_time.lower())

        if validate != "Ok.":

            await ctx.response.send_message(
                "You didn't enter the time correctly, dumbass."
            )

        else:

            await ctx.response.send_message(
                f"Oki, noted.\n\n**Session Name:** {sesh_name}\n**Session Time:** {sesh_time}"
            )

            sesh_hour = sesh_time[0:2]
            sesh_min = sesh_time[3:]

            while True:

                now = datetime.now(tz=timezone(timedelta(hours=5.5)))

                current_hour = now.strftime("%H")
                current_min = now.strftime("%M")
                current_sec = now.strftime("%S")

                if current_hour == sesh_hour:
                    if current_min == sesh_min:
                        await ctx.channel.send(
                            f"Oi {ctx.author.mention}! It's **{current_hour}:{current_min}** right now, aka time for **{sesh_name}**.",
                            tts=True,
                        )
                        break
                await asyncio.sleep(40)


def setup(client):
    client.add_cog(Sessions(client))
