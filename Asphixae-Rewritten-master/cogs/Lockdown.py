import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Lockdown(commands.Cog):
    """Lockdown commands meant for moderation and require elevated privileges."""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def lockdown(self, ctx, *roles: discord.Role):
        """Locksdown the server. (Must be an Administrator)\nFormat: )lockdown"""
        for role in roles:
            perms = discord.PermissionOverwrite(send_messages=False)
            await ctx.edit_channel_permissions(channel=ctx.channel, target=roles, overwrite=perms)    
        await ctx.send('Channel is locked down. Do )unlock to unlock the channel.')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unlock(self, ctx, *roles: discord.Role):
        """Unlocks the server. (Must be an Administrator)\nFormat: )unlock"""
        for role in roles:
            perms = discord.PermissionOverwrite(send_messages=True)
            await ctx.edit_channel_permissions(channel=ctx.channel, target=roles, overwrite=perms)
        await ctx.send('Channel is unlocked.')
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)


    
def setup(bot):
    bot.add_cog(Lockdown(bot))