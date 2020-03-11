import discord
import os
import time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

bot = commands.Bot(command_prefix=')', case_insensitive=True)
bot.remove_command('help')

@bot.command(hidden=True)
async def load(ctx, extension):
    """None of your business"""
    owner = 612331900039725131
    if ctx.message.author.id == owner:
        try:
            bot.load_extension(f'cogs.{extension}')
            await ctx.send(f'Loaded {extension}!')
        except:
            await ctx.send('Failed to load due to already being loaded.')
    elif ctx.message.author is not owner:
        await ctx.send("Damn you tried man.")

@bot.command(hidden=True)
async def unload(ctx, extension):
    """None of your business"""
    owner = 612331900039725131
    if ctx.message.author.id == owner:
        try:
            bot.unload_extension(f'cogs.{extension}')
            await ctx.send(f'Unloaded {extension}!')
        except:
            await ctx.send('Failed to unload due to already being unloaded.')
    elif ctx.message.author is not owner:
        await ctx.send("Damn you tried man.")
@bot.command(hidden=True)
async def reload(ctx, extension):
    """None of your business"""
    owner = 612331900039725131
    if ctx.message.author.id == owner:
        if extension.lower() == "all":
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    bot.unload_extension(f'cogs.{filename[:-3]}')
                    time.sleep(.1)
                    bot.load_extension(f'cogs.{filename[:-3]}')
                    await ctx.send(f'Reloaded {filename[:-3]}!')
        try:
            bot.unload_extension(f'cogs.{extension}')
            time.sleep(.1)
            bot.load_extension(f'cogs.{extension}')
            await ctx.send(f'Reloaded {extension}!')
        except ValueError:
            await ctx.send(f'Could not reload {extension} due to lack of existence')
    elif ctx.message.author is not owner:
        await ctx.send("Damn you tried man.")


for filename in os.listdir('./cogs'):
     if filename.endswith('.py'):
         bot.load_extension(f'cogs.{filename[:-3]}')


bot.run('Hah good try')
