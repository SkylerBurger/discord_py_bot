import os

from discord.ext import commands
import environ

env = environ.Env()
env.read_env()
BOT_TOKEN = env('BOT_TOKEN')

bot = commands.Bot(command_prefix='/')

for file in os.listdir('./cogs'):
    if file.endswith('.py'):
        bot.load_extension(f'cogs.{file[:-3]}')
        print(f'Loaded cog: {file[:-3]}')

bot.run(BOT_TOKEN)
