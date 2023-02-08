import discord
from config import *

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
	bot.run(convert(list))
run()