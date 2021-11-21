import discord
from discord.ext import commands
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext.commands import Bot
import youtube_dl
import os

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is ready.')


@client.command()
async def hello(ctx):
    await ctx.send(f'Hi')


@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency * 1000)}ms')


@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@client.command()
async def leave(ctx):
    guild = ctx.message.guild
    voice_client = guild.voice_client
    await voice_client.disconnect()


@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
            print("Removed old song file")
    except PermissionError:
        print("Trying to delete song file, but it's being played")
        await ctx.send("Error: Music player")
        return

    await ctx.send("Getting everything ready now")

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
        }]
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloading audio now\n")
        ydl.download([url])

    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")

    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.10

    await ctx.send("Playing")
    print("playing")


@client.event
async def on_member_join(member):
    role = get(member.guild.roles, name="Role 3")
    await member.add_roles(role)


client.run('')
