import discord
from discord.ext import commands
# from src.surgical_population_generator import generator
import os
TOKEN = os.getenv('DISCORD_TOKEN')
import generator


# Setup Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')


@bot.command()
async def instructions(ctx):
    """Basic instruction command"""
    msg = "Usage: !generate [number] [-random_sample]\nExample: !generate 10 -random_sample"
    await ctx.send(msg)


@bot.command()
async def generate(ctx, count: int, flag: str = None):
    """
    Calls your patient_generator.py logic.
    'flag' will capture '-randomize' if provided.
    """
    # Logic to handle your flag
    random_sample = (flag == "-random_sample")

    # Call your existing function
    # Assuming your function is named 'create_patients'

    result = generator.create_patients(count, random_sample=random_sample)

    # Discord has a 2000 character limit per message
    for part in result:
        await ctx.send(f"```\n{part}\n```")


bot.run(TOKEN)