import discord
import time
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
owner = 403253246849974272
owner2 = 612331900039725131




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
		logchannel = self.bot.get_channel(714887388916220064)
		if user.id == owner:
			return await ctx.send(f"You cannot change {user.mention} nickname!")
		elif user.id == owner2:
			return await ctx.send("You cannot ban this person!")
		else:        
			try:
				await user.edit(nick=nick)
				await ctx.send(f"Changed {user.mention}'s nickname!")
			except discord.Forbidden:
				await ctx.send("Are you attempting to change a users nickname that is higher than the bot?")
		await logchannel.send(f"{ctx.message.author.mention} changed {user.mention}'s nick!")

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount=5):
		"""Clears messages (Must have manage message perms)\nFormat: )clear {int}"""
		await ctx.channel.purge(limit=amount)
		logchannel = self.bot.get_channel(714887388916220064)
		await ctx.send(f'Cleared {amount} messages!')
		time.sleep(2)
		await ctx.channel.purge(limit=1)
		await logchannel.send(f"{ctx.message.author.mention} cleared!")

	@commands.command()
	@commands.has_permissions(kick_members=True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		"""Kicks a user (Must have kick perms)\nFormat: )kick {user} {reason}"""
		logchannel = self.bot.get_channel(714887388916220064)
		if member.id == owner:
			return await ctx.send("You cannot kick this person!")
		elif member.id == owner2:
			return await ctx.send("You cannot kick this person!")
		else:
			try:
				await member.kick(reason=reason)
				await ctx.send('{0} was kicked by {1}!'.format(member.mention, ctx.message.author.mention))
			except discord.Forbidden:
				await ctx.send('Could not kick the user. Are you attempting to kick someone higher than the bot?')
			await logchannel.send(f"{ctx.message.author.mention} kicked {user.mention}!")

	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def ban(self, ctx, user: discord.Member, reason=None):
		"""Bans a user (Must have ban perms)\nFormat: )ban {user} {reason}"""
		logchannel = self.bot.get_channel(714887388916220064)
		if user == ctx.message.author:
			return await ctx.send("You cannot ban yourself!")
		elif user.id == owner:
			return await ctx.send("You cannot ban this person!")
		elif user.id == owner2:
			return await ctx.send("You cannot ban this person!")
		else:
			try:
				await user.ban(reason=reason)
				await ctx.send('{0} was banned by {1}!'.format(user.mention, ctx.message.author.mention))
			except discord.Forbidden:
				await ctx.send("Could not ban the user. Are you attempting to ban someone higher than the bot?")
			
		await logchannel.send(f"{ctx.message.author.mention} banned {user.mention}!")


	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def molter(self ,ctx, user: discord.Member):
		"""")ban but better... \n Format: )molter {user} {reason}"""
		logchannel = self.bot.get_channel(714887388916220064)
		if user == ctx.message.author:
			return await ctx.send("Can't molter yourself man!")
		elif user.id == owner:
			return await ctx.send("You cannot molter this person!")
		elif user.id == owner2:
			return await ctx.send("You cannot molter this person!")
		else:
			embed = discord.Embed(description='Moltered.', colour=discord.Color.dark_purple())
			try:
				await user.send(embed=embed)
			except:
				print(f"Couldn't dm {user} about being moltered!")
			await user.ban(reason="Moltered.")
			await ctx.send(f"{user.mention} got moltered.")
			await logchannel.send(f"{user.mention} was moltered by {ctx.message.author.mention}!")



	@commands.command()
	@commands.has_permissions(ban_members=True)
	async def hackban(self, ctx, user_id: int, *, reason=None):
		"""Bans a user that is outside the server(Must have ban perms)\nFormat: )hackban {userid}"""
		logchannel = self.bot.get_channel(714887388916220064)
		author = ctx.message.author
		guild = author.guild
		try:
			await self.bot.http.ban(user_id, guild.id, 0)
			await ctx.send(f"Banned {user_id}.")
		except discord.NotFound:
			await ctx.send('Could not find user. Invalid userid.')
		except discord.errors.Forbidden:
			await ctx.send('Could not ban the user. Are you attempting to ban someone higher than the bot?.')
		await logchannel.send(f"{ctx.message.author.mention} hackbanned {user_id}!")

	@commands.command(hidden=True)
	async def quit(self, ctx):
		if ctx.message.author.id == owner2:
			await ctx.send("Bot is shutting down. Bye!")
			await self.bot.close()
		elif ctx.message.author is not owner2:
			await ctx.send("Damn you tried man.")


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def mute(self, ctx, user: discord.Member, *, reason=None):
		"""Mutes a user (Must be an Administrator)\nFormat: )mute {User} {Reason}"""
		role = discord.utils.get(ctx.guild.roles, name='Muted')
		logchannel = self.bot.get_channel(714887388916220064)
		if user == ctx.message.author:
			return await ctx.send("You cannot mute yourself!")
		elif role in user.roles:
			await ctx.send("User is already muted.")
		else:
			await mute(ctx, user, reason)
			await logchannel.send(f"{ctx.message.author.mention} muted {user.mention}!")

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unmute(self, ctx, user: discord.Member):
		"""Unmute a user (Must be an Administrator)\nFormat: )unmute {User}"""
		logchannel = self.bot.get_channel(714887388916220064)
		role = discord.utils.get(ctx.guild.roles, name='Muted')
		try:
			await user.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
			await ctx.send(f'{user.mention} has been unmuted!')
		except discord.Forbidden:
			await ctx.send('You do not have the perms to do that command!')
		await logchannel.send(f"{ctx.message.author.mention} unmuted {user.mention}!")


	@commands.command()
	@commands.has_permissions(administrator=True)
	async def block(self, ctx, user: discord.Member):
		"""Blocks a user from the current chat (Must be an Administrator)\nFormat: )block {user}"""
		logchannel = self.bot.get_channel(714887388916220064)
		if user is None:
			return await ctx.send("You must specify a user!")
		elif user.id == owner:
			return await ctx.send("You cannot block this person!")
		elif user.id == owner2:
			return await ctx.send("You cannot block this person!")
		else:
			await ctx.channel.set_permissions(user, send_messages=False)
			await ctx.send(f'{user.mention} has been blocked from sending messages in this channel!')
			await logchannel.send(f"{ctx.message.author.mention} blocked {user.mention}!")

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def unblock(self, ctx, user: discord.Member):
		"""Unblocks a user from the current chat (Must be an Administrator)\nFormat: )unblock {user}"""
		logchannel = self.bot.get_channel(714887388916220064)
		if user is None:
			return await ctx.send("You must specify a user!")
		await ctx.channel.set_permissions(user, send_messages=True)
		await ctx.send(f'{user.mention} has been unblocked from this channel.')
		await logchannel.send(f"{ctx.message.author.mention} unblocked {user.mention}!")


	@commands.command()
	@commands.has_permissions(manage_roles=True)
	async def role(self, ctx, user: discord.Member, *, role):
		""""Gives the user a specific role\nFormat: )role {user} {desired role}"""
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		desired = discord.utils.get(server.roles, name=role)
		if desired is None:
			return await ctx.send("That role is nonexistent!")
		elif desired in user.roles:
			await user.remove_roles(desired)
			await ctx.send(f"Removed {user.mention}'s {role}!")
			await logchannel.send(f"Removed {user.mention}'s {role}!")
		else:
			await user.add_roles(desired)
			await ctx.send(f"Gave {user.mention} {role}!")
			await logchannel.send(f"Gave {user.mention} {role}!")


def setup(bot):
	bot.add_cog(Moderation(bot))
