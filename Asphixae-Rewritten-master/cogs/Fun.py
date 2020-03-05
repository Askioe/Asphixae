import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Fun(commands.Cog):
    """Fun stuff"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ball(self, ctx):
        """Something for ball kek\nFormat: )ball"""
        await ctx.send('Do the mistress thing :3')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *, raw):
        """Tells the bot to say exactly what you want it to say(Requires Administrator)\nFormat: )say {context} """
        await ctx.send(raw)

def setup(bot):
    bot.add_cog(Fun(bot))
