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
                await message.channel.send('Uso correto: !timer <tempo em minutos>')
        elif  message.content.startswith('!mu'):
                voice_channel_name = message.content.split()[1]
                voice_channel = discord.utils.get(message.guild.voice_channels, name=voice_channel_name)
                if voice_channel and len(voice_channel.members) > 0:
                    mentions = [member.mention for member in voice_channel.members]
                    response = " ".join(mentions) + "hora de passar raiva!"
                    await message.channel.send(response)
                else:
                    response = "Nenhum usuário está conectado ao canal de voz especificado."
                    await message.channel.send(response)

client = MyClient(intents=intents)
client.run('TOKEN')
