import discord
import os
print("Token encontrado:", bool(os.environ.get('TOKEN')))
from discord.ext import commands
from flask import Flask
from threading import Thread

# Keepalive
app = Flask('')

@app.route('/')
def home():
    return "Nexus online!"

def run():
    app.run(host='0.0.0.0', port=3000)

Thread(target=run).start()

# Config do bot
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

# IDs dos canais
CANAL_BOAS_VINDAS = 000000000000000000  # troca pelo ID do canal

@bot.event
async def on_ready():
    print(f'✅ Nexus bot online como {bot.user}')
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name="site.n3xus.workers.dev"
        )
    )

@bot.event
async def on_member_join(member):
    canal = bot.get_channel(CANAL_BOAS_VINDAS)
    if canal:
        embed = discord.Embed(
            title="Welcome to Nexus! 🟣",
            description=f"Hey {member.mention}, glad you're here!\nCheck the channels and grab your free key.",
            color=0x9b30ff
        )
        embed.set_footer(text="Nexus • site.n3xus.workers.dev")
        await canal.send(embed=embed)

@bot.command()
async def script(ctx):
    embed = discord.Embed(
        title="📜 Nexus Script",
        description="Copy and execute this in your executor while in-game.",
        color=0x9b30ff
    )
    embed.add_field(name="Script", value="```lua\nloadstring(game:HttpGet('https://site.n3xus.workers.dev/'))()```")
    embed.set_footer(text="Nexus • site.n3xus.workers.dev")
    await ctx.send(embed=embed)

@bot.command()
async def key(ctx):
    embed = discord.Embed(
        title="🔑 Free Keys",
        description=f"Keys are dropped in <#1500319930824921109>!\nKeep notifications on so you don't miss it.",
        color=0x9b30ff
    )
    embed.set_footer(text="Nexus • site.n3xus.workers.dev")
    await ctx.send(embed=embed)

@bot.command()
async def site(ctx):
    embed = discord.Embed(
        title="🌐 Nexus Website",
        description="[Click here to visit our website](https://site.n3xus.workers.dev/)",
        color=0x9b30ff
    )
    embed.set_footer(text="Nexus • site.n3xus.workers.dev")
    await ctx.send(embed=embed)

bot.run(os.environ['TOKEN'])
