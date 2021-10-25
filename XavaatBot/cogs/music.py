import discord
from discord.ext import commands
import youtube_dl

# discord.py
## GITHUB: https://github.com/Rapptz/discord.py
## DOCUMENTATION: https://discordpy.readthedocs.io/en/latest/

# youtube-dl DOCS   https://github.com/ytdl-org/youtube-dl


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self, ctx):
        await joinVoiceChannel(ctx)

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        await joinVoiceChannel(ctx)

        ctx.voice_client.stop()

        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }
        YDL_OPTIONS = {"format": "bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self, ctx):
        ctx.voice_client.pause()
        await ctx.send("Paused")

    @commands.command()
    async def resume(self, ctx):
        ctx.voice_client.resume()
        await ctx.send("Resume")

    @commands.command()
    async def stop(self, ctx):
        ctx.voice_client.stop()
        await ctx.send("Stopped")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Music Cog Loaded.")


async def joinVoiceChannel(ctx):
    if ctx.author.voice is None:
        await ctx.send("You have to join a voice channel first nerd.")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
        await voice_channel.connect()
    else:
        await ctx.voice_client.move_to(voice_channel)


def setup(client):
    client.add_cog(Music(client))