import discord
from config import *
from content import *
import random
def run():
	bot = discord.Client(command_prefix = '!', intents = discord.Intents.all())
	@bot.event
	async def on_ready():
		print(f"{bot.user} is now running")
	@bot.event
	async def on_message(message):
		if message.author == bot.user:
			return
		if message.content.lower() == "hello":
			await message.channel.send("Hey")
		if message.content == "!randomjoke":
			i = random.randint(0,99)
			text = jokes[i]
			embed = discord.Embed(title='Here is a random joke', description=f'{text}', color=discord.Color.blue())
			embed.set_footer(text = "Hope you enjoyed the joke")
			await message.channel.send(embed=embed)
	bot.run(convert(list))
run()