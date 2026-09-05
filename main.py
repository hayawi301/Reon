import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'مرحبا!':
        await message.channel.send('عمل بنجاح')

client.run('MTU0NTYyMzQ0MzU3MDA0MDk3Mg.GrweA8.nH5IDAcpx6lEk7SiuLsf9aDV_a3z8lRKKvvu9I')
