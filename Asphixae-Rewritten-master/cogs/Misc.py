import discord
import time
from discord.ext import commands
start_time = time.time()


class Misc(commands.Cog):
	"""Just random miscellaneous things """
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		bad_words = ["kys", "autism", "autistic", "crippled", "handicapped", "disabled", "retarded", "jew", "nigger", "nigga"]
		for word in bad_words:
			if message.content.count(word.lower()) >= 1:
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
				print(f"detected badword! By {user} at {time.time}")
				await user.send(embed=embed)




	@commands.Cog.listener()
	async def on_ready(self):
		print('Started bot.')
		await self.bot.change_presence(status=discord.Status.idle, activity=discord.Game('Prefix is ). Trying to do GUESS work'))
		

	@commands.command()
	@commands.has_permissions(add_reactions=True, embed_links=True)
	async def help(self, ctx, *cog):
		"""What Do You Think Sherlock?"""
		try:
			if not cog:
				embed = discord.Embed(title='Help',
									 description='A bot purely made to make my life easier. It does not have much but I can teach it a few things!\nBlame Idkwha#4060 for this awful bot.', colour=discord.Color.dark_purple())
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
				await ctx.message.add_reaction(emoji='✉')
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
	async def ping(self, ctx):
		"""Pings the bot.\nFormat: )ping"""
		await ctx.send(f'Pong! {round(self.bot.latency * 1000)} ms')

	@commands.command()
	async def uptime(self, ctx):
		"""Checks how long the bot has been up for.\nFormat: )uptime"""
		await ctx.send("--- %s seconds ---" % (time.time() - start_time))

	@commands.command()
	async def info(self, ctx):
		"""Just some general information of the bot\nFormat: )info"""
		embed = discord.Embed(title='What was the purpose of this?', description='Idk lel', colour=discord.Color.dark_purple())
		embed.add_field(name='Just why?', value=f'why the fuck not [here is a fucking cat piss off](https://imgur.com/r/cats)')
		embed.set_thumbnail(
			url='https://media.discordapp.net/attachments/638063360860094469/683664808779710498/Screen_Shot_2020-03-01_at_5.19.29_AM.png')
		await ctx.send(embed=embed)
def setup(bot):
	bot.add_cog(Misc(bot))




