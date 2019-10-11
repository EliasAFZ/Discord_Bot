"""  
 Name: Discord_Bot
 Date: 10/9/2019
 Description: Discord bot made to play around with python, discord.py, and json commands
 Please mind the excessive comments in certain area's as they are for my personal notes!

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""
import os
import discord
import requests
# env library import helps load variables from an .env file
from dotenv import load_dotenv
# Bot subclass of client import adds extra functionality
from discord.ext import commands

# Grab our token and server from our .env file
load_dotenv()
token = os.environ.get("Discord_Token")
server = os.environ.get("Discord_Server")

# Switched to using bot instead of client (everywhere it says bot client use to be there)
bot = commands.Bot(command_prefix="!", description="Test bot to play around with.")
# client = discord.Client()

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


# command decorator is technically a callback ctx is the context in which its called.
@bot.command(pass_context = True, help="Adds two numbers.\n Command format: \"!add x y\"")
# converter used to convert user input to appropiate data type e.g. a: int, b: int
async def add(ctx, x: int, y: int):
        await ctx.send(x + y)

@bot.command(name="sub", help="Subtracts two numbers.\n Command format: \"!subtract x y\"")
async def subtract(ctx, x: int, y: int):
    await ctx.send(x - y)


@bot.command(name="mult", help="Multiply's two numbers.\n Command format: \"!multiply x y\"")
async def multiply(ctx, x: int, y: int):
    await ctx.send(x * y)


@bot.command(name="div", help="Divide's two numbers.\n Command format: \"!divide x y\"")
async def divide(ctx, x: float, y: float):
    try:
        await ctx.send(x / y)
    except ZeroDivisionError:
        await ctx.send(0)


@bot.command(name="patchnotes", help="Asks the expert what the patch notes are for anything.")
async def patchnotes(ctx, str):
    await ctx.send("<@!251728492272680971> Whats the patchnotes for " + str)

# catches exception of users putting in wrong arguments
@bot.event
async def on_command_error(error, ctx):
    if isinstance(error, commands.MissingRequiredArgument):
        return await ctx.send("No varibales detected, please enter your variables.")

    #nothing caught?
    #raise error

# Run Bot
bot.run(token)




# Old methods/tests kept for notes please ignore below.
"""
*COROUTINES* are generalization of subroutines. They are used for cooperative multitasking 
where a process voluntarily yield (give away) control periodically or when idle in order 
to enable multiple applications to be run simultaneously.
"""
"""
#decorator
@client.event
async  def on_message(message):
    #checks to see if the message is from a user to prevent bot recursion
    if message.author == client.user:
        return

    if message.content == "!test":
        response = "Testing self ping: "
        my_id = "<@!313686003594559488>"
        #await suspends the execution of the surrounding coroutine until each coroutine has finished.
        await message.channel.send(response + my_id + " pong")

    if message.content == "!patchnotes":
        response = "<@!251728492272680971> I could make the bot do this but its funnier " \
                                           "to have a bot ping you for patch notes."
        await message.channel.send(response)

    if message.content == "!smallbraincoder":
        response = "<@!120554480541368320> Rust is a neat language - Python Bot"
        await message.channel.send(response)

    if message.content == "!avoidslegday":
        response = "<@!277561909803483136> Oh hey look a hill, guess I'll " \
                                           "just take the elevator - Tevin"
        await message.channel.send(response)

    #manual exception raise from discord to console
    elif message.content == "!exception":
        response = "Error: exception written to error.log"
        await  message.channel.send(response)
        raise discord.DiscordException
        
# Catching exceptions for on_message function and writing it to a file
@bot.event
async def on_error(event, *args, **kwargs):
    with open("error.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise       
"""
"""
# Dm's users that just joined the server for the first time
@client.event
async def on_member_join(member):
    #waits on exec of the higher coroutine until each inner coroutine has finished
    await member.create_dm()
    await member.dm_channel.send(
        f"Sigh {member.name}, I guess you can join the server."
    )
"""
"""
#looks for matching server name as bot can be in multiple servers
    for guild in client.guilds:
        if guild.name == guild:
            break
"""
""" 
#Prints all members of the server in a formatted string to console
members = "\n - " .join([member.name for member in guild.members])
print(f"Server Members:\n - {members}")
"""
