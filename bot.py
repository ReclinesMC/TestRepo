#Import Discord
import discord
from discord.ext import commands
#Import JSON
import json
#Import OS
import os

#Set intents of disc client
intents = discord.Intents.default()
intents.message_content = True

#Save useful information from the config
with open('config.json', 'r') as tokenfile:
    data = json.load(tokenfile)
    token = data['token']
    prefix = data['prefix']

bot = commands.Bot(command_prefix = prefix, intents = intents)

# Load cogs (command files)
initial_extensions = ['cogs.Utility']

@bot.event
async def on_ready():
    for extension in initial_extensions:
        await bot.load_extension(extension)

#Start the client
bot.run(token)