import disnake
from disnake.ext import commands
from disnake import Option, OptionChoice, ApplicationCommandInteraction

class Demo(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.slash_command(
    name = 'command',
    description = 'A basic command showing the structure of slash commands.',
    options = [
        Option(
                            type = 3,
                            name = 'required',
                            description = 'A required option. (This takes a string.)',
                            required = True
                    ),
        Option(
                            type = 3,
                            name = 'optional',
                            description = 'An optional option. (This takes a string.)',
                            required = False
                    ),
        Option(
                            type = 3,
                            name = 'string',
                            description = 'A string input.',
                            required = False
                    ),
        Option(
                            type = 3,
                            name = 'string_choice',
                            description = 'A string input option with choices, can have up to 25 choices.',
                            choices = [
                                OptionChoice(
                                    name = 'Choice 1',
                                    value = 'choice_1'
                                ),
                                OptionChoice(
                                    name = 'Choice 2',
                                    value = 'choice_2'
                                )
                            ],
                            required = False
                    ),
        Option(
                            type = 4,
                            name = 'integer',
                            description = 'An integer input. Can take any integer between -2^53 and 2^53.',
                            required = False
                    ),
        Option(
                            type = 4,
                            name = 'integer_choice',
                            description = 'An integer input option with choices, can have up to 25 choices.',
                            choices = [
                                OptionChoice(
                                    name = 'Choice 1',
                                    value = 1
                                ),
                                OptionChoice(
                                    name = 'Choice 2',
                                    value = 2
                                )
                            ],
                            required = False
                    ),
        Option(
                            type = 5,
                            name = 'boolean',
                            description = 'A boolean input. Takes True or False.',
                            required = False
                    ),
        Option(
                            type = 6,
                            name = 'user',
                            description = 'A Discord user input. Select a user from the options that show up or paste the ID of the user.',
                            required = False
                    ),
        Option(
                            type = 7,
                            name = 'channel',
                            description = 'A channel input. Can take all channel types. Select a channel above or use a channel ID.',
                            required = False
                    ),
        Option(
                            type = 8,
                            name = 'role',
                            description = 'A role input. Select a role from the menu above or use a role ID of a role in the CURRENT server.',
                            required = False
                    ),
        Option(
                            type = 9,
                            name = 'mentionable',
                            description = 'A mention input. Select a user/role from the above menu or enter it\'s ID.',
                            required = False
                    ),
        Option(
                            type = 10,
                            name = 'number',
                            description = 'A number input. Takes either an integer or float. Any double between -2^53 and 2^53',
                            required = False
                    ),
        Option(
                            type = 10,
                            name = 'number_choice',
                            description = 'A number input option with choices, can have up to 25 choices.',
                            choices = [
                                OptionChoice(
                                    name  = 'Integer Choice 1',
                                    value  = 1
                                ),
                                OptionChoice(
                                    name = 'Integer Choice 2',
                                    value = 2
                                ),
                                OptionChoice(
                                    name = 'Float Choice 1',
                                    value = 0.1
                                ),
                                OptionChoice(
                                    name = 'Float Choice 2',
                                    value = 0.2
                                )
                            ],
                            required = False
                    )
        ]
    )
    async def command(self, inter: ApplicationCommandInteraction, 
    required,
    optional: None,
    string:None,
    string_choice: None,
    integer: None,
    integer_choice: None,
    boolean: None,
    user: None,
    channel: None,
    role: None,
    mentionable: None,
    number: None,
    number_choice: None):
        await inter.response.send_message('[Ok.](https://abhigyantrips.is-a.dev/)')

def setup(client):
    client.add_cog(Demo(client))