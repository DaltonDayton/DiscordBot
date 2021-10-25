import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
from itertools import cycle

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
for filename in os.listdir("./XavaatBot/cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

# Clear messages in channel
@client.command()
@commands.has_role("Admin")
async def clear(ctx, amount: int = 10):
    await ctx.channel.purge(limit=amount)
    print("Finished Clearing")


# Command Error Handling
# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send("That is not a command.")
#     elif isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send("Please specify the number of messages to delete.")
#     else:
#         await ctx.send(error)

status = cycle(
    [
        "A rolling golem gathers no rust.",
        "I remain focused.",
        "Magic and steam guide me.",
        "The time of man has come to an end.",
        "I put the 'go' in 'golem'. That was humor. Other golems find that to be appropriately funny.",
        "Exterminate. Exterminate.",
    ]
)

# Change status every minute
@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


# On Ready
@client.event
async def on_ready():
    change_status.start()
    print("Logged in as {0.user}".format(client))


client.run(TOKEN_ID)
