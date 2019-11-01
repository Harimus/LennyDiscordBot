import os
import json
import discord
from dotenv import load_dotenv
import random
from discord import opus

print(opus.is_loaded())
#opus.load_opus('C:\\Users\Dan\\opus\\libopus-0.dll')


with open("lenny.json", encoding="utf-8") as fh:
    lenny_parts = json.load(fh)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

VC = None
Asource = discord.FFmpegPCMAudio(executable="C:\\Users\\Dan\\ffmpeg-4.2.1-win64-static\\bin\\ffmpeg.exe", source='test.mp3')
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(guild)


# members = '\n - '.join([member.name for member in guild.members])
# print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
    global VC
    if message.author == client.user:
        await message.author.edit(nick=random_lenny_face())
        return
    guild = message.guild
    content = str(message.content).split()
    print(guild)
    bois = guild.members
    newnick = random_lenny_face()
    print(content)
    if "Jappie" in str(message.author):
        if str(message.content) == "$slave":
            voice_channel = message.author.voice.channel
            VC = await voice_channel.connect(timeout=10)
        if str(message.content) == "$die":
            await VC.disconnect()
        if str(message.content) == "$play":
            if VC is not None:
                if not VC.is_playing():
                   VC.play(Asource, after=None)

    if "$setnickname" in content[0]:
        if len(content) > 1:
            if "all" in content[1]:
                roles = content[2]
                if roles in "@everyone":
                    return
                for boi in bois:
                    bois_role = str(boi.top_role)
                    print(f'boi {boi.name} and {bois_role}')
                    if str(bois_role) == "@everyone":
                        continue
                    if roles in bois_role:
                        newnick = random_lenny_face()
                        await message.channel.send(f'This nigga {boi.name} is a {roles}, and from now on is: {newnick} ')
                        await boi.edit(nick=newnick)
                return
            for dude in content[1:]:
                boi = guild.get_member_named(dude)
                if boi is None:
                    return
                print(boi.name)
                if dude in boi.name:
                    await message.channel.send(f'This nigga {boi.name} is from now on: {newnick} ')
                    await boi.edit(nick=newnick)
            return
        else:
            await message.author.edit(nick=random_lenny_face())
            return
    if "Jappie" in str(message.author) or "Getfader" in str(message.author):
        await message.channel.send(random_lenny_face())
    if "Qewk" in str(message.author):
        await message.channel.send(random_lenny_face() + " Stupid nigga")

    if "Yownie" in str(message.author):
        await message.channel.send(random_lenny_face() + " Stupid hoe")

    if "Fhelita" in str(message.author):
        await message.channel.send("( ͠° ͟ʖ °): Käften Jonas")


@client.event
async def on_voice_state_update(member, before, after):
    global VC
    if "Jappie" in member.name:
        print(member)
        print('-------------')
        print(before)
        print('-------------')
        print(after)
        print('-------------')
        master_channel = after.channel
        if master_channel is None:
            VC.disconnect()
        VC = await master_channel.connect(timeout=10)
    else:
        return




def random_lenny_face():
    eyes = random.choice(lenny_parts['Eyes'])
    mouth = random.choice(lenny_parts['Mouth'])
    ears = random.choice(lenny_parts['Ears'])
    return ears[0] + eyes[0] + mouth + eyes[1] + ears[1]


client.run(TOKEN)
