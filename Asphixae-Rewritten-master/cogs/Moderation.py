import discord
import time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext.commands import MemberConverter

def get_user(message, user):
    try:
        member = message.mentions[0]
    except:
        member = message.guild.get_member_named(user)
    if not member:
        try:
            member = message.guild.get_member(int(user))
        except ValueError:
            pass
    if not member:
        return None
    return member


async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if role in user.roles:
        await ctx.send("User is already muted.")
    elif role is None:
        try:
            muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
            for channel in ctx.guild.channels:  # removes permission to view and send in the channels
                await channel.set_permissions(muted, send_messages=False,
                                              read_message_history=True,
                                              read_messages=True)
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make a muted role")  # self-explainatory
        await user.add_roles(muted)
        await ctx.send(f"{user} has been muted for {reason}!")
    else:
        await user.add_roles(role)  # adds newly created muted role
        await ctx.send(f"{user} has been muted for {reason}")


class Moderation(commands.Cog):
    """Commands that require escalated privileges."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, user: discord.Member = None, *, nick):
        """Changes a user's nickname (Must have manage nickname perms)\nFormat: )nick {user} {nickname}"""
        if user is None:
            return await ctx.send("You must specify a user!")
        try:
            await user.edit(nick=nick)
            await ctx.send(f"Changed {user}'s nickname!")
        except discord.Forbidden:
            await ctx.send("Are you attempting to change a users nickname that is higher than the bot?")


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=5):
        """Clears messages (Must have manage message perms)\nFormat: )clear {int}"""
        await ctx.channel.purge(limit=amount)
        await ctx.send(f'Cleared {amount} messages!')
        time.sleep(2)
        await ctx.channel.purge(limit=1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks a user (Must have kick perms)\nFormat: )kick {user} {reason}"""
        if member is None:
            return await ctx.send("You must specify a user!")
        try:
            await member.kick(reason=reason)
            await ctx.send('{0} was kicked by {1}!'.format(member, ctx.message.author))
        except discord.Forbidden:
            await ctx.send('Could not kick the user. Are you attempting to kick someone higher than the bot?')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user, reason=None):
        """Bans a user (Must have ban perms)\nFormat: )ban {user} {reason}"""
        user = get_user(ctx.message, user)
        if user is None:
            return await ctx.send("You must specify a user!")
        try:
            await user.ban(reason=reason)
            await ctx.send('{0} was banned by {1}!'.format(user, ctx.message.author))
        except discord.Forbidden:
            await ctx.send("Could not ban the user. Are you attempting to ban someone higher than the bot?")


    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def hackban(self, ctx, user_id: int, *, reason=None):
        """Bans a user that is outside the server(Must have ban perms)\nFormat: )hackban {userid}"""
        author = ctx.message.author
        guild = author.guild
        user = self.bot.get_user(user_id)
        if user is None:
            return await ctx.send("You must specify a userid!")
        elif user is not None:
            ctx.invoke(self.ban, user=user)
        try:
            await self.bot.http.ban(user_id, guild.id, 0)
            await ctx.send(f"Banned {user_id}.")
        except discord.NotFound:
            await ctx.send('Could not find user. Invalid userid.')
        except discord.errors.Forbidden:
            await ctx.send('Could not ban the user. Are you attempting to ban someone higher than the bot?.')

    @commands.command(hidden=True)
    async def quit(self, ctx):
        """Shuts down the bot (Must be Rolen *yikes*)\nFormat: )quit"""
        owner = 612331900039725131
        if ctx.message.author.id == owner:
            print(ctx.message.author.id)
            await ctx.send("Bot is shutting down. Bye!")
            await self.bot.close()
        elif ctx.message.author is not owner:
            print(ctx.message.author.id)
            await ctx.send("Damn you tried man.")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, user: discord.Member, reason=None):
        """Mutes a user (Must be an Administrator)\nFormat: )mute {User} {Reason}"""
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if user is None:
            return await ctx.send("You must specify a user!")
        elif role in user.roles:
            await ctx.send("User is already muted.")
        else:
            try:
                await mute(ctx, user, reason)
            except MissingPermissions:
                await ctx.send('You do not have the permissions to use that command!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, user: discord.Member):
        """Unmute a user (Must be an Administrator)\nFormat: )unmute {User}"""
        if user is None:
            return await ctx.send("You must specify a user!")
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        try:
            await user.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
            await ctx.send(f'{user} has been unmuted!')
        except MissingPermissions:
            await ctx.send('You do not have the perms to do that command!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def block(self, ctx, user: discord.Member):
        """Blocks a user from the current chat (Must be an Administrator)\nFormat: )block {user}"""
        if user is None:
            return await ctx.send("You must specify a user!")
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send('User has been blocked from sending messages in this channel!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblock(self, ctx, user: discord.Member):
        """Unblocks a user from the current chat (Must be an Administrator)\nFormat: )unblock {user}"""
        if user is None:
            return await ctx.send("You must specify a user!")
        await ctx.channel.set_permissions(user, send_messages=True)
        await ctx.send('User has been unblocked from this channel.')


def setup(bot):
    bot.add_cog(Moderation(bot))
