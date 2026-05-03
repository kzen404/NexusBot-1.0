import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

# Comando de exemplo: !oi
@bot.command()
async def oi(ctx):
    await ctx.send(f"Olá, {ctx.author.name}! 👋")

# Comando: !ping
@bot.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! Latência: {round(bot.latency * 1000)}ms")

bot.run(os.environ["DISCORD_TOKEN"])
