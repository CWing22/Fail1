#!/usr/bin/env python3
import os
import requests
import aiml
import irc.bot

USERNAME = "crack_azz" # Substitute your bot's username
TOKEN = "oauth:obejk6vxzumkae8hhgxpujowx1px3u" # OAUTH token (Get one here: https://twitchapps.com/tmi/)
CHANNEL = "#stilettoninja" # Twitch channel to join

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
        server = 'irc.chat.twitch.tv'
        port = 443
        print("Connecting to {} on port {}...".format(server, port))
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, token)], username, channel)

    def on_welcome(self, c, e):
        print("Joining " + self.channel)
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        print(e.arguments[0])
        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] in BOT_PREFIX:
            cmd = e.arguments[0].split(' ')[0][1:]
            print("Received command: " + cmd)
            self.do_command(e, cmd)
            return
        aiml_response = self.aiml_kernel.respond(e.arguments[0])
        c.privmsg(self.channel, aiml_response)

    def do_command(self, e, cmd):
        c = self.connection
        # Handle commands here
        if cmd == "booty":
            c.privmsg(self.channel, "(__)__)")

if __name__ == "__main__":
    bot = ChattyCathy(USERNAME, TOKEN, CHANNEL)
    bot.start()
