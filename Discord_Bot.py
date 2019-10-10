"""  
 Name: Discord_Bot
 Date: 10/9/2019
 Description: 

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""
import os
import discord
import requests

# env library import helps load variables from an .env file
from dotenv import load_dotenv
#Snags var's
load_dotenv()

token = os.environ.get("Discord_Token")
server = os.environ.get("Discord_Server")
client = discord.Client()

#discord starts its call here using a decorator
@client.event
async def on_ready():

    #discord.py likes to call its servers "guilds" also discord.py built in get method is nice
    guild = discord.utils.get(client.guilds, name=server)

    #Console status output for debugging purposes
    print(
        f"\n{client.user} is connected to discord. Currently connected Servers:"
        f"\n- {guild.name} (ID: {guild.id})"
    )

#decorator
@client.event
async  def on_message(message):
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

#Catching exception and writing it to a file
@client.event
async def on_error(event, *args, **kwargs):
    with open("error.log", "a") as f:
        if event == "on_message":
            f.write(f"Unhandled message: {args[0]}\n")
        else:
            raise

#Run Bot
client.run(token)

#Test/Old methods kept for notes
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
