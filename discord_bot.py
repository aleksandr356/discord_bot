import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

plastic_crafts = ['подставка для карандашей', 'мозайка из крышек от пластиковых бутылок', 'ваза или цветочный горшок из пластиковых бутылок']
interesting_facts = ['Одна платиковая бутылка разлогается 450 лет', 'Около 12% поверхности земли - это заповедники', 'Солнечная энергия является наиболее экологически чистой, но для производства солнечных панелей всё равно используются продукты переработки нефти']

bot_commands = ['$podelki - поделка из пластика', '$advices - советы по сохранению окружающей среды', '$facts - интересные факты проо окружающую среду']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    await ctx.send('Чтобы увидеть список команд, напишите $bot_help')

@bot.command()
async def podelki(ctx):
    await ctx.send(random.choice(plastic_crafts))
    
@bot.command()
async def bot_help(ctx):
    for i in range(len(bot_commands)):
        await ctx.send(bot_commands[i])

@bot.command()
async def advices(ctx):
    await ctx.send('Советы по предотвращению загрязнения окружающей среды:')
    await ctx.send('1. выбрасывайте мусор раздельно')
    
@bot.command()
async def facts(ctx):
    await ctx.send('Интереные факты об окружающей среде:')
    await ctx.send(random.choice(interesting_facts))

bot.run('ТОКЕН')
