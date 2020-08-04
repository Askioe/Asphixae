import discord
import string
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class Physics(commands.Cog):
    """Physics thing"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def confirm(self, ctx, *, raw):
        """Confirms answers.\nFormat: )confirm {Question Number} {Letter answer} {correct/wrong}"""
        answers = [instance.strip().split(' ') for instance in raw.split(',')]
        for instance in answers:
            if "correct" in instance:
                try:
                    await self.bot.get_channel(683561547460902913).send(instance)
                except:
                    await ctx.send("This isn't the right server.")
            elif "wrong" in instance:
                try:
                    await self.bot.get_channel(683568448840007682).send(instance)
                except:
                    await ctx.send("This isn't the right server.")
            elif not "correct" or "wrong" in instance:
                await ctx.send("You did not properly format it.")

        await ctx.send("Successfully submitted answer(s).")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def StartTest(self, ctx, *, raw):
        """Starts testing session and allows you to confirm answers. (Must be an Administrator)\nFormat: )StartTest"""
        try:
            await self.bot.get_channel(683561547460902913).send(f'Testing has started for {raw}.')
            await self.bot.get_channel(683568448840007682).send(f'Testing has started for {raw}.')
        except:
            await ctx.send('You need to specify which test it is.')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def StopTest(self, ctx):
        """Disables testing session and disables confirm answers. (Must be an Administrator)\nFormat: )StopTest"""
        await ctx.send("Testing session has been finished.")


def setup(bot):
    bot.add_cog(Physics(bot))
