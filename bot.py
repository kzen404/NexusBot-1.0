import discord
import os
from discord.ext import commands
from flask import Flask
from threading import Thread

# Keepalive para o Render não hibernar
app = Flask('')

@app.route('/')
def home():
    return "Nexus online!"

def run():
    app.run(host='0.0.0.0', port=3000)

Thread(target=run).start()

# Bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Nexus bot online como {bot.user}')

@bot.event
async def on_member_join(member):
    canal = bot.get_channel(SEU_CANAL_ID_AQUI)
    await canal.send(f'Bem vindo ao Nexus, {member.mention}! 🟣')

bot.run(os.environ['TOKEN'])
