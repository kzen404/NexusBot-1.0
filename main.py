import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online como {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="geral")
    if channel:
        await channel.send(f"👋 Welcome to Nexus, {member.mention}! Check the rules and grab a free key!")

@bot.command()
async def script(ctx):
    await ctx.send("📜 Get the Nexus script at: https://site.n3xus.workers.dev/")

@bot.command()
async def key(ctx):
    await ctx.send(f"🔑 Free keys are dropped at <#1500319930824921109> — keep an eye on it!")

bot.run(os.environ["DISCORD_TOKEN"])
