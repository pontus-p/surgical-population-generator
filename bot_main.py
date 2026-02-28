import discord
from discord.ext import commands
from src.surgical_population_generator import generator

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
    msg = "Usage: !generate [number] [-randomize]\nExample: !generate 10 -randomize"
    await ctx.send(msg)


@bot.command()
async def generate(ctx, count: int, flag: str = None):
    """
    Calls your patient_generator.py logic.
    'flag' will capture '-randomize' if provided.
    """
    # Logic to handle your flag
    is_random = (flag == "-randomize")

    # Call your existing function
    # Assuming your function is named 'create_patients'
    result = generator.create_patients(count, random_sample=is_random)

    # Discord has a 2000 character limit per message
    if len(result) > 2000:
        await ctx.send("Output is too long for Discord! Try a smaller number.")
    else:
        await ctx.send(f"```\n{result}\n```")


bot.run('YOUR_BOT_TOKEN_HERE')