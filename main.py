import discord
from discord.ext import commands
import os,getgifs
from dotenv import load_dotenv
load_dotenv()


intents = discord.Intents().all()
client = commands.Bot(command_prefix='/',intents=intents)

@client.event
async def on_ready():
    print('The bot is ready to teach you')

@client.command()
async def hello(ctx):
    print('hello there, what can i do for you?')
    await ctx.send('Thank you for your command, what can i do for you?')

@client.command()
async def tellmeabout(ctx,arg):
    await ctx.send('Sure. I will send you the info about '+ str(arg))

@client.command()
async def quiz(ctx,arg):
    await ctx.send('Sure, i\'ll quiz you on the same')

@client.command()
async def gif(ctx,*args):
    print(' '.join(args))
    gifurl = getgifs.geturl(' '.join(args),10)
    await ctx.send(gifurl)

client.run(os.getenv('TOKEN'))