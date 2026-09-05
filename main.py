import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'البوت اشتغل وصار أونلاين باسم {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!مرطبا!':
        await message.channel.send('عمل بنجاح')

client.run('MTU0NTYyMzQ0MzU3MDA0MDk3Mg.GxMClh.UifW-DUzKMphLDQA2jZWRkr8l43y6BhcOujhMw')
