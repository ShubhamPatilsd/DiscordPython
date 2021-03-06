import pyjokes
import discord

intents=discord.Intents.all()
client=discord.Client(intents=intents)

s=input("What is the text channel ID you want to put it in?: ")
st=input("What is the token of the bot?: ")


@client.event
async def on_ready():
    global welcome_channel
    await client.wait_until_ready()
    welcome_channel=client.get_channel(int(s))
    await welcome_channel.send("Logged In")

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith('$joke'):
        joke=pyjokes.get_joke(language='en',category='neutral')
        await message.channel.send(joke)

@client.event
async def on_member_join(member):

    await welcome_channel.send("Welcome "+member.display_name)


client.run(str(st))
