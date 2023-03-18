import openapi
import discord
import os

client = discord.Client()

client.run(open("TOKEN.txt").read())
