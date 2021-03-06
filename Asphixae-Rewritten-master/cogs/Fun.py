import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions



class Fun(commands.Cog):
    """Fun stuff"""
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, raw):
        """Tells the bot to say exactly what you want it to say(Requires Administrator)\nFormat: )say {context} """
        await ctx.send(raw)

    @commands.command()
    async def coinflip(self, ctx):
        """Just a coinflip.\nFormat: )coinflip"""
        sides = ["Heads", "Tails"]
        choice = random.choice(sides)
        await ctx.send(choice)



def setup(bot):
    bot.add_cog(Fun(bot))
