import discord
import os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} online!")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="geral")
    if channel:
        await channel.send(f"👋 Welcome {member.mention} to **Nexus**!")

@bot.command()
async def script(ctx):
    await ctx.send("📜 Get the script at: https://site.n3xus.workers.dev/")

@bot.command()
async def key(ctx):
    await ctx.send("🔑 Free keys are dropped at <#1500319930824921109> — keep an eye out!")

bot.run(os.getenv("TOKEN"))
