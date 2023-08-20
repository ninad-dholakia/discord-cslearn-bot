import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('The bot is ready to teach you')

#second event: sending message
@client.event
async def on_message(message):
  
  #check who sent the message
  if message.author == client.user:
    return
  
  if message.content.startswith('!') and str(message.channel.name) == "admin":
    print('it stsarts with !')
    await message.channel.send("hello there, what can i do for you?")

client.run(os.getenv('TOKEN'))