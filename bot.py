import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

TOKEN = "" #Your Token Here

Client = discord.Client
bot = commands.Bot(command_prefix = "-")

@client.event
async def on_ready():
    print('Ready For Action! OwO')

@client.event
async def on_message(message):
    if "OwO" in message.content:
        await client.send_message(message.channel, 'What\'s This?')

client.run(TOKEN)