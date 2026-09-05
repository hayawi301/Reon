import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot is ready: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!hello!":
        await message.channel.send("عمل بنجاح")

client.run(os.getenv("DISCORD_TOKEN"))
