import discord
import time
import random
from discord.ext import commands
start_time = time.time()
owner = 612331900039725131
owner2 = 313173842644303872
owner3 = 403253246849974272

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



class Misc(commands.Cog):
	"""Just random miscellaneous things """
	def __init__(self, bot):
		self.bot = bot



	@commands.Cog.listener()
	async def on_message(self, message):
		bad_words = ["kys", "disabled", "retarded", "jew", "nigger"]
		logchannel = self.bot.get_channel(714887388916220064)
		for word in bad_words:
			if message.author.id == owner:
				break
			elif message.content.count(word.lower()) >= 1:
				channel = message.channel
				embed = discord.Embed(title='Suicide Hotline',
										description='We detected you using harsh words and we would like to provide you with resources that would benefit yourself and others to cleanse yourself!',
										colour=discord.Color.dark_purple())
				embed.add_field(name='Resources', value='US: The National Suicide Prevention Lifeline at 1-800-273-8255\nUK: Call 1850 60 90 91 or call Hopeline 080020068204141 or text 0778620209697\nCanada: Text HOME to 686868 or call 1-833-456-4566 or text 45645 Crisis Services\nAustralia: Lifeline Crisis Support call 13 11 14')
				embed.set_image(
						url='https://cdn.discordapp.com/attachments/684298650876510234/686640943671017475/Screen_Shot_2020-03-09_at_11.25.11_AM.png')
				embed.set_footer(text="We are here for you!")
				embed.set_thumbnail(
						url='https://media.discordapp.net/attachments/638063360860094469/683664808779710498/Screen_Shot_2020-03-01_at_5.19.29_AM.png')
				user = message.author
				await logchannel.send(f"Detected Bad Word from {message.author}")
				try:
					await user.send(embed=embed)
				except:
					pass

	@commands.Cog.listener()
	async def on_message_delete(self, message):
		logchannel = self.bot.get_channel(714887388916220064)
		await logchannel.send(f"Message deleted containing: {message.content} by {message.author.mention}")

	@commands.Cog.listener()
	async def on_member_join(self, member):
		logchannel = self.bot.get_channel(714887388916220064)
		channel = self.bot.get_channel(664772611477078016)
		banlist = [293958507550474240, 
		644328839677476878, 
		581473402813022220, 
		605205303390240768, 
		290038247068008448, 
		440053210120585216, 
		259541896521711616, 
		708630834810191873,
		607433241959464961,
		281361544401518592,
		535471959161569280,
		490628933688098826,
		527568078754676736]
		choices = [f"We've been expecting you **{member.name}**", f"**{member.name}** has arrived! They're retarded!", f"Pssstttt **{member.name}** has joined. Everyone hide!"]
		choice = random.choice(choices)
		nembed = discord.Embed(description=choice, colour=discord.Color.green())
		await channel.send(embed=nembed)
		for idiot in banlist: 
			if member.id == idiot:
				await logchannel.send(f"Prevented {member.mention} from joining the server!")
				await channel.send(f"Prevented {member.mention} from joining server!")
				embed = discord.Embed(description='You are not permitted to join this discord Server! Try again at a later date.', colour=discord.Color.dark_red())
				try:
					await member.send(embed=embed)
					await member.ban(reason="On the blacklist")
				except:
					pass
	



	@commands.Cog.listener()
	async def on_member_remove(self, member):
		channel = self.bot.get_channel(664772611477078016)
		choices = [f"Another libtard has left! This time it was **{member.name}**!", f"**{member.name}** has quit. Party's over.", f"**{member.name}** just left. Probably got banned by Prak."]
		choice = random.choice(choices)
		nembed = discord.Embed(description=choice, colour=discord.Color.red())
		await channel.send(embed=nembed)



	@commands.Cog.listener()
	async def on_ready(self):
		print('Started bot.')
		await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game("Askio can't program"))
		

	@commands.command()
	@commands.has_permissions(add_reactions=True, embed_links=True)
	async def help(self, ctx, *cog):
		"""What Do You Think Sherlock?"""
		try:
			if not cog:
				embed = discord.Embed(title='Help',
									 description="A bot purely made to make my life easier. It can't do much so don't expect much!\nBlame Idkwha#4060 for this awful bot.", colour=discord.Color.dark_purple())
				embed.set_thumbnail(url='https://media.discordapp.net/attachments/638063360860094469/683664808779710498/Screen_Shot_2020-03-01_at_5.19.29_AM.png')
				embed.add_field(name='Links:', value=f'[Source Code](https://www.youtube.com/watch?v=dQw4w9WgXcQn)\n'
								f'[Invite me!](https://discordapp.com/api/oauth2/authorize?client_id=650143724642500640&permissions=8&scope=bot)')
				embed.set_footer(text='Use help <category> to view the commands within that category')
				cogs_desc = ''
				for x in self.bot.cogs:
					cogs_desc += ('{} - {}'.format(x, self.bot.cogs[x].__doc__) + '\n')
				embed.add_field(name='Command Categories:', value=cogs_desc[0:len(cogs_desc) - 1], inline=False)
				cmds_desc = ''
				for y in self.bot.walk_commands():
					if not y.cog_name and not y.hidden:

						cmds_desc += ('{} - {}'.format(y.name, y.help) + '\n')
				await ctx.send('', embed=embed)

			else:
				if len(cog) > 1:
					embed = discord.Embed(title='Error!',
										 description='That is way too many cogs!',
										 color=discord.Color.red())
					await ctx.send('', embed=embed)
				else:
					found = False
					for x in self.bot.cogs:
						for y in cog:
							if x == y:
								embed = discord.Embed(title=cog[0] + ' Command Listing',
													 description=self.bot.cogs[cog[0]].__doc__,
													  color=discord.Colour.dark_purple())
								for c in self.bot.get_cog(y).get_commands():
									if not c.hidden:
										embed.add_field(name=c.name, value=c.help, inline=False)
								found = True
								embed.set_footer(text='Use help <category> to view the commands within that category')
								embed.set_thumbnail(
								url='https://media.discordapp.net/attachments/638063360860094469/683664808779710498/Screen_Shot_2020-03-01_at_5.19.29_AM.png')

					if not found:
						embed = discord.Embed(title='Error!', description='Could not find "' + cog[0] + '" Try another category?',
											 color=discord.Color.red())
					embed.set_footer(text='Use help <category> to view the commands within that category')
					embed.set_thumbnail(
						url='https://media.discordapp.net/attachments/638063360860094469/683664808779710498/Screen_Shot_2020-03-01_at_5.19.29_AM.png')
					await ctx.send('', embed=embed)
		except:
			pass




	@commands.command()
	async def changelog(self, ctx):
		"""Opens the changelog. \n Format: )changelog (Owner Locked)"""
		if ctx.message.author.id == owner:
			embed = discord.Embed(title="Runn 2.5 Changelog", description="This is where I will be keeping track of what I add into the bot. This command is not accessible to everyone, however.", colour=discord.Color.dark_purple())
			embed.set_footer(text='Currently still in beta.')
			embed.add_field(name="2.4", value="Added new user to access admin commands\n Changed Idiot list to prevent everyone from rejoining\n Added name to initx10 & 11\n Added new command due to a request ')molter' which is an alternative to )ban\n Added logging to more moderation commands to prevent abuse\n Added new command role to role a user")
			embed.add_field(name="2.3", value="Removed unnecessary names from initx10 & 11 \n Added new role 'Skipped' \n Added new logging for other commands \n Redid on_message detection \n Added Changelog \n Prevented certain commands from being used on specific people \n Added 2 new commands for admin use \n Added on member join detection to prevent idiots")
			await ctx.send('', embed=embed)



	@commands.command()
	async def ping(self, ctx):
		"""Pings the bot.\nFormat: )ping"""
		await ctx.send(f'Pong! {round(self.bot.latency * 1000)} ms')

	@commands.command()
	async def uptime(self, ctx):
		"""Checks how long the bot has been up for.\nFormat: )uptime"""
		await ctx.send("--- %s seconds ---" % (time.time() - start_time))


def setup(bot):
	bot.add_cog(Misc(bot))




