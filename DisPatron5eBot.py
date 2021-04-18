# -*- coding: utf-8 -*-
"""
Created on Sat Apr 3 13:59:57 2021

@author: Nathan Russell
"""

# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(TOKEN)