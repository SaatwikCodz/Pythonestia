import discord
from config import *
from content import *
import random
from bs4 import BeautifulSoup
import requests
def scrape(u):
	response = requests.get(u)
	soup = BeautifulSoup(response.content, 'html.parser')
	title_element = soup.find('title')
	title = title_element.text.strip()

# Find the element that contains the number of views
	views_element = soup.find('span', {'class': 'view-count'})
	print(views_element)
	views = views_element.text.strip()

# Find the element that contains the number of likes
	likes_element = soup.find('button', {'title': 'I like this'})
	likes = likes_element.text.strip()
	l = []
	l.append(title)
	l.append(views)
	l.append(likes)
	return l
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
		if message.content == '!randomvideo':	
			text = videos[random.randint(0,50)]
			list = scrape(text)
			title = list[0]
			views = list[1]
			likes = list[2]
			e = discord.Embed(title="Here is a random video", description = f"{text}")
			e.add_field(name="Title", value="{title}")
			e.add_field(name="Views", value="{views}")
			e.add_field(name="Likes", value="{likes}")
			await message.channel.send(embed = e)
		if message.content == "!randomjoke":
			i = random.randint(0,99)
			text = jokes[i]
			embed = discord.Embed(title='Here is a random joke', description=f'{text}', color=discord.Color.blue())
			embed.set_footer(text = "Hope you enjoyed the joke")
			await message.channel.send(embed=embed)
	bot.run(convert(list))
run()