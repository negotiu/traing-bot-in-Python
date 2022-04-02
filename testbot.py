from multiprocessing.connection import Client
from re import A
import discord
from discord.ext import commands,tasks
from discord.utils import get

client = commands.Bot(command_prefix = ['-', '; '])
client.run('OTU5MDkxMzAzMzUyNzk1MjE3.YkW1YQ.vSB8rCdXvJ2Cxdm9rNwQKb9Hk5g')

@client.event()
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name = "Portal"))

@client.event()
async def on_ready():
    general_channel = client.get_all_channels(959093582432718880)
    await general_channel.send("it is working?")

@client.command()
async def test(ctx):
    await ctx.send("Hello World!")




# @client.command()
#    async def join(ctx):