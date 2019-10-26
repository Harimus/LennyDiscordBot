import os
import json
import discord
from dotenv import load_dotenv
import random

with open("lenny.json", encoding="utf-8") as fh:
	lenny_parts = json.load(fh)
print(lenny_parts)


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(guild)
    #members = '\n - '.join([member.name for member in guild.members])
    #print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
	print(message.author)
	
	if message.author == client.user:
		return
	if  "Jappie" in str(message.author) or "Getfader" in str(message.author):
		await message.channel.send(random_lenny_face()+"\n" + random_lenny_face()+'\n'+ random_lenny_face())


def random_lenny_face():
	eyes = random.choice(lenny_parts['Eyes'])
	mouth = random.choice(lenny_parts['Mouth'])
	ears = random.choice(lenny_parts['Ears'])
	return  ears[0]+eyes[0]+mouth+eyes[1]+ears[1]



client.run(TOKEN)