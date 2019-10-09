"""  
 Name: Discord_Bot
 Date: 10/9/2019
 Description: 

 @Author Elias Afzalzada
 Copyright © Elias Afzalzada - All Rights Reserved
"""
import os
import discord

# env library import helps load variables from an .env file
from dotenv import load_dotenv
load_dotenv()
token = os.environ.get("Discord_Token")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
