import discord
from discord.ext import commands

import random
import os


description = '''This is unstoppable machine.'''

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
bot = commands.Bot(command_prefix='?', description=description, intents=intents)

names = ["mem1.png", "mem2.png", "mem3.png"]

@bot.command(name="memes")
async def mem(ctx):
    random_img = random.choice(names)
    with open(f'images/{random_img}', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)


bot.run("")
