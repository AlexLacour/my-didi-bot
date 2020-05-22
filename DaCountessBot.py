"""
DaCountessBot code
"""
import os

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name="repeat")
async def hello(ctx, *args):
    response = " ".join(x for x in [str(word) for word in args])
    await ctx.send(response)

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

async def play(ctx):
    voice = bot.voice_clients()
    await "MECOUILLE"

async def leave(ctx):
    await ctx.voice_client.disconnect()

bot.run(TOKEN)
