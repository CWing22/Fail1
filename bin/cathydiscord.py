
import discord
import os
import random
import pkg_resources
from discord.ext 
import commands
import requests

USERNAME = "FoxyVamp" # Substitute your bot's username
TOKEN = "NTQ2MTEzOTkzMDU2NTgzNjgw.D1sh_Q.ElLUJNLbN81ixm7D2lyFBHfj38k" # OAUTH token (Get one here: https://twitchapps.com/tmi/)
CHANNEL = "foxyvamp"

STARTUP_FILE = "std-startup.xml"
BOT_PREFIX = ('?', '!')

class ChattyCathy(irc.bot.SingleServerIRCBot):
    def __init__(self, username, token, channel):
        self.token = token
        self.channel = "#" + channel

        # Load AIML kernel
        self.aiml_kernel = aiml.Kernel()
        self.aiml_kernel.learn(STARTUP_FILE)
        self.aiml_kernel.respond("LOAD AIML B")

        # Create IRC bot connection
        server = 'foxyvamp'
        port = 667
        print("Connecting to {} on port {}...".format(server, port))
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, channel)

    def on_welcome(self, c, e):
        print("Joining " + self.channel)
        c.join(self.channel)


self.discord_client = commands.Bot(command_prefix=BOT_PREFIX)
        self.setup()

    def setup(self):

        @self.discord_client.event
        @asyncio.coroutine
        def on_ready():
            print("FoxyVamp Online!")
            print("Name: {}".format(self.discord_client.user.name))
            print("ID: {}".format(self.discord_client.user.id))
            yield from self.discord_client.change_presence(game=discord.Game(name='Chatting with th Foxy fam'))

        @self.discord_client.event
        @asyncio.coroutine
        def on_message(message):
            if message.author.bot or str(message.channel) != self.channel_name:channel_name
                return

            if message.content is None:
                print("Empty message received.")
                return

            print("Message: " + str(message.content))

            if message.content.startswith(BOT_PREFIX):
                # Pass on to rest of the client commands
                yield from self.discord_client.process_commands(message)
            else:
                aiml_response = self.aiml_kernel.respond(message.content)
                yield from self.discord_client.send_typing(message.channel)
                yield from asyncio.sleep(random.randint(1,3))
                yield from self.discord_client.send_message(message.channel, aiml_response)

    def run(self:  self.discord_client.run(self.token
