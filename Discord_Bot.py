"""  
 Name: Discord_Bot
 Date: 10/9/2019
 Description: Discord bot made to play around with python, discord.py, json, and HTTp requests.
 Please mind the excessive comments in certain area's as they are for my personal notes!

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""
import os
import discord
import requests
import random
# env library import helps load variables from an .env file
from dotenv import load_dotenv
# Bot subclass of client import adds extra functionality
from discord.ext import commands
# Reddit data
from Data import RedditData, DataExtractor
import json

# Grab our token and server from our .env file
load_dotenv()
token = os.environ.get("Discord_Token")
server = os.environ.get("Discord_Server")

# Switched to using bot instead of client (everywhere it says bot client use to be there)
bot = commands.Bot(command_prefix="!", description="Test bot to play around with.")


# discord starts its call here using a decorator
@bot.event
async def on_ready():
    # discord.py likes to call its servers "guilds" also discord.py built in get method is nice
    guild = discord.utils.get(bot.guilds, name=server)

    # Console status output for debugging purposes
    print(
        f"\n{bot.user.name} is connected to discord. Currently connected Servers:"
        f"\n- {guild.name} (ID: {guild.id})"
    )


# catches exception of users putting in wrong arguments
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        return await ctx.send("Wrong arguments entered.")


# command decorator is technically a callback ctx is the context in which its called.
@bot.command(pass_context=True, help="Adds two numbers.")
# converter used to convert user input to appropiate data type e.g. a: int, b: int
async def add(ctx, x: int, y: int):
    await ctx.send(x + y)

@bot.command(name="sub", help="Subtracts two numbers.")
async def subtract(ctx, x: int, y: int):
    await ctx.send(x - y)

@bot.command(name="mult", help="Multiply's two numbers.")
async def multiply(ctx, x: int, y: int):
    await ctx.send(x * y)

@bot.command(name="div", help="Divide's two numbers.")
async def divide(ctx, x: float, y: float):
    try:
        await ctx.send(x / y)
    except ZeroDivisionError:
        await ctx.send(0)


# Running joke among friends that pings a specific friend of ours for patch notes on a game.
@bot.command(name="patchnotes", help="Asks the expert what the patch notes are for anything.")
async def patch_notes(ctx, subject):
    await ctx.send("<@!251728492272680971> Whats the patchnotes for " + subject)


# list of quotes from everyones favorite show command, choses one by random.
@bot.command(name="topgear", help="Random quotes from Top Gear")
async def top_gear(ctx):
    top_gear_quotes = [
        "\"To test the new Range Rover, I went to the United States, which is in America.\" - Jeremy Clarkson",
        "\"How hard can it be?\" - Jeremy Clarkson",
        "\"We are on the cutting edge of cocking about.\" - Richard Hammond",
        "\"I AM A DRIVING GOD!\" - Richard Hammond",
        "\"Aye?! It's not a kit car, it's a Lamborghini... philistine.\" - James May",
        "\"My colander's leaking.\" - James May"
    ]
    response = random.choice(top_gear_quotes)
    await ctx.send(response)


# Reddit command that grabs the top post from a requested subbreddit.
@bot.command(name="rtop", help="Returns today's top post from requested subreddit.")
async def rtop(ctx, subreddit):
    url = "https://www.reddit.com/r/" + subreddit.lower() + "/top/.json?"
    response = requests.get(url, verify=True, headers={'User-agent': 'discord bot 0.1'})

    data = response.content
    obj = json.loads(data, object_hook=RedditData)

    await ctx.send(obj.data.children[0].data.url)


# Runs Bot
bot.run(token)
