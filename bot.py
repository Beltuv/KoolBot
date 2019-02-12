import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Club Penguin'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('!roll'):
        randomlist = ["1","2","3","4","5","6"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!hi'):
        await client.send_message(message.channel,'Hello, <@%s> !'  %(message.author.id))
    if message.content == '!help':
        await client.send_message(message.channel,'Go the #rules-and-information channel and read it.')
    if message.content == '!BeltuvIsGreat':
        await client.send_message(message.channel,'Of course he is!')
    if message.content == '!WhoIsBeltuv':
        await client.send_message(message.channel,'Maybe you should learn. You are in his server.')
    if message.content == '!KoolBot':
        await client.send_message(message.channel,'Yeah, that is me.')
    if message.content.startswith('!FavouriteFood'):
        randomlist = ["It is obviously pizza!","Hotdogs can never be beaten!","Toothbrush, I love eating those brushs!","Chocolate.","Does juice count?","Cheeseburgers are dreams that came true!!!","Beltuv.","Just my saliva."]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!icosahedron'):
        randomlist = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!KoolBotVersion':
        await client.send_message(message.channel,'0.2.0')
    if message.content == '!ServerVersion':
        await client.send_message(message.channel,'0.1.7')
    if message.content == '!IsThisACommand':
        await client.send_message(message.channel,'Yes, it is.')
    if message.content == '!pizza':
        em = discord.Embed(description='Amazing. Right?')
        em.set_image(url='https://cdn.discordapp.com/attachments/488894112724942848/544861230385463307/BFV36537_CC2017_2IngredintDough4Ways-FB.png')
        await client.send_message(message.channel, embed=em)
    if message.content == '!unknown':
        await client.send_message(message.channel,'That will always be a mystery...')
    if message.content == '!BeltuvIsBad':
        await client.send_message(message.channel,'I will have to alert you to the authorities.')
client.run('NTQ0NzI0MzgzNjcxNzc5MzU4.D0RSfw.ho4ejt7rc-AxiyfpxVLOXsx9dHY')

