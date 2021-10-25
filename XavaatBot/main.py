import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN_ID = os.getenv("TOKEN_ID")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())


# Load extension
@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension}")


# Unload extension
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"Unloaded {extension}")


# Reload extension
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"Reloaded {extension}")


# Load all extensions
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Clear messages in channel
@client.command()
@commands.has_role("Admin")
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount)


# Command Error Handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("That is not a command.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please specify the number of messages to delete.")
    else:
        await ctx.send(error)


# On Ready
@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle, activity=discord.Game("Hello there!")
    )
    print("Logged in as {0.user}".format(client))


client.run(TOKEN_ID)
