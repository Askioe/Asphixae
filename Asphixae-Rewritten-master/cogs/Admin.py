import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


#    @commands.command(hidden=True):
#    async def initx12(self, ctx):
#        owner = 612331900039725131
#        server = ctx.guild
#       if ctx.message.author.id == owner:
            
#      elif ctx.message.author is not owner:
#           print(f"{ctx.message.author} attempted to initiate initx12 without being administrator.")




class Admin(commands.Cog):
    """Administrative commands restricted."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def returnlogs(self, ctx):
        owner = 612331900039725131
        server = ctx.guild
        if ctx.message.author.id == owner:
            print("This is a fake command!")
        else:
            await ctx.send("You are not privileged to do so!")

    @commands.command(hidden=True)
    async def aban(self, ctx, user: discord.Member, reason=None):
        owner = 612331900039725131
        server = ctx.guild
        if ctx.message.author.id == owner:
            try:
                await user.ban(reason=reason)
                await ctx.send('{0} was banned by {1}!'.format(user.mention, ctx.message.author.mention))
            except discord.Forbidden:
                await ctx.send("Could not ban the user. Are you attempting to ban someone higher than the bot?")
    

    @commands.command(hidden=True)
    async def akick(self, ctx, user: discord.Member, reason=None):
        owner = 612331900039725131
        server = ctx.guild
        if ctx.message.author.id == owner:
            try:
                await user.kick(reason=reason)
                await ctx.send('{0} was kicked by {1}!'.format(user.mention, ctx.message.author.mention))
            except discord.Forbidden:
                await ctx.send("Could not kick the user. Are you attempting to ban someone higher than the bot?")

    @commands.command(hidden=True)
    async def aclear(self, ctx, amount=5):
        owner = 612331900039725131
        if ctx.message.author.id == owner:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'Cleared {amount} messages!')
            time.sleep(2)
            await ctx.channel.purge(limit=1)



    


def setup(bot):
    bot.add_cog(Admin(bot))
