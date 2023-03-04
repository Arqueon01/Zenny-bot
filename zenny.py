import discord
import asyncio
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = True
intents.message_content = True

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        async def mark_users(ctx, voice_channel_name):
            await mark_all_users(ctx, voice_channel_name)

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.content == 'ping':
            await message.channel.send('pong')
        elif message.content.startswith('tempo'):
            try:
                time = int(message.content.split()[1])*60
                await message.channel.send(f'Sinta {time} segundos de tranquilidade.')
                await asyncio.sleep(time)
                await message.channel.send(f'{message.author.mention}, Acabou a tranquilidade de {time} segundos.')
            except:
                await message.channel.send('Uso correto: !timer <tempo em segundos>')

client = MyClient(intents=intents)
client.run('TOKEN')