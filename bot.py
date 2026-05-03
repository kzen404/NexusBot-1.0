import discord
import os
from flask import Flask
from threading import Thread
import time

app = Flask('')

@app.route('/')
def home():
    return "Nexus online!"

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

Thread(target=run, daemon=True).start()

time.sleep(3)

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ {client.user} online!')

client.run(os.environ.get('TOKEN'))
