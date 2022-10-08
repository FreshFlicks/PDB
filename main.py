import discord
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('logged in as {0.user}'.format(client))
  return


@client.event
async def on_message(message):
  if message.author == client.user:
    return

keep_alive()
client.run(os.getenv('TKN'))