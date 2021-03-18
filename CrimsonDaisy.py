import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix='#', help_command=None, case_insensitive = True)

@client.event
async def on_ready():
    print('Bot is ready.')
    general_channel = client.get_channel(818338932319846414)
    await general_channel.send('Hello Shaan.')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('#help Super Smash Bros. Ultimate'))

@client.command(name = 'help')
async def help(context):
    file = discord.File("Images/DaisyIcon.png", filename = "image.png")
    CrimsonDaisy = discord.Embed(title = "Help", type = "rich", description = "I am Crimson mf Daisy", color = 0xfca103)
    CrimsonDaisy.set_thumbnail(url="attachment://image.png")
    CrimsonDaisy.set_author(name = "Crimson Daisy", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    CrimsonDaisy.add_field(name = "#smash <OPTIONAL @USER>", value = "Smash that mf", inline=False)
    CrimsonDaisy.add_field(name = "#<Smash Character (Daisy)>", value = "Smash Data (Absolute Scale and Ranks)", inline=False)
    CrimsonDaisy.set_footer(text = "Degen Daisy Main")
    await context.message.channel.send(file = file, embed = CrimsonDaisy)

@client.event
async def on_message(message):
    if message.author == client.user: return

    if "hello" in message.content:
        await message.channel.send("Hello! " + message.author.mention)

    if "smash" in message.content and "#" not in message.content:
        await message.channel.send("I'll smash your dad")

    await client.process_commands(message)

@client.command(name = 'smash')
async def smash(context, user : discord.User = None):
    if not user:
        await context.send("Fire Emblem exists")
    else:
        await context.send("I'm gonna smash " + user.mention)



@client.command(name = 'Mario')         #Mario Command: #1
async def Mario(context):
    file = discord.File("Images/MarioImage.png", filename = "image.png")
    Mario = discord.Embed(title = "Donkey Kong (1981)", type = "rich", description = "Do Not Sit in Shield!", color = 0xff0000)
    Mario.set_thumbnail(url="attachment://image.png")
    Mario.set_author(name = "#1: Mario", url = "https://open.spotify.com/track/53BIF7mH7UL7yTzOsKIoEw?si=2e2258ae59594ec8", icon_url = "https://ssb.wiki.gallery/images/9/9e/MarioHeadSSBUWebsite.png")
    Mario.add_field(name = "Run Speed", value = "1.76 `[37-40]`", inline=True)
    Mario.add_field(name = "Air Speed", value = "1.208 `[13-17]`", inline=True)
    Mario.add_field(name = "Fall Speed", value = "1.5 `[57-60]`", inline=False)
    Mario.add_field(name = "Weight", value = "98 `[32-35]`", inline=True)
    Mario.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    Mario.set_footer(text = "[X] = Rank out of 87.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(file = file, embed = Mario)


@client.command(name = "DK")            #DK Command: #2
async def DK(context):
    file = discord.File("Images/DKImage.png", filename = "image.png")
    DK = discord.Embed(title = "Donkey Kong (1981)", type = "rich", description = "Combo Food", color = 0x97572b)
    DK.set_thumbnail(url="attachment://image.png")
    DK.set_author(name = "#2: Donkey Kong", url = "https://open.spotify.com/track/05kvH7fHTyjvoZz0dM02sI?si=4d6ff97781814380", icon_url = "https://ssb.wiki.gallery/images/2/21/DonkeyKongHeadSSBUWebsite.png")
    DK.add_field(name = "Run Speed", value = "1.873 `[29]`", inline=True)
    DK.add_field(name = "Air Speed", value = "1.208 `[13-17]`", inline=True)
    DK.add_field(name = "Fall Speed", value = "1.63 `[38-39]`", inline=False)
    DK.add_field(name = "Weight", value = "127 `[3-4]`", inline=True)
    DK.add_field(name = "Weightclass", value = "`Super Heavyweight`", inline=True)
    DK.set_footer(text = "[X] = Rank out of 87.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(file = file, embed = DK)

@client.command(name = 'Peach')         #Peach Command: #14
async def Peach(context):
    file = discord.File("Images/PeachImage.png", filename = "image.png")
    Peach = discord.Embed(title = "Super Mario Bros. (1985)", type = "rich", description = "Overrated, Float Cancels Still OP", color = 0xff008b)
    Peach.set_thumbnail(url="attachment://image.png")
    Peach.set_author(name = "#14: Peach", url = "https://open.spotify.com/track/126jlTTSRGaZ5WX8e4Tv7M?si=1de226102cb44eba", icon_url = "https://ssb.wiki.gallery/images/1/14/PeachHeadSSBUWebsite.png")
    Peach.add_field(name = "Run Speed", value = "1.595 `[60-64]`", inline=True)
    Peach.add_field(name = "Air Speed", value = "1.029 `[48-50]`", inline=True)
    Peach.add_field(name = "Fall Speed", value = "1.19 `[85-86]`", inline=False)
    Peach.add_field(name = "Weight", value = "89 `[63-64]`", inline=True)
    Peach.add_field(name = "Weightclass", value = "`Lightweight`", inline=True)
    Peach.set_footer(text = "[X] = Rank out of 87.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(file = file, embed = Peach)


@client.command(name = 'Daisy')         #Daisy Command: #15
async def Daisy(context):
    file = discord.File("Images/DaisyImage.png", filename = "image.png")
    Daisy = discord.Embed(title = "Super Mario Land (1989)", type = "rich", description = "My Main, Float Cancels OP", color = 0xfca103)
    Daisy.set_thumbnail(url="attachment://image.png")
    Daisy.set_author(name = "#15: Daisy", url = "https://open.spotify.com/track/63ZMWm1RPYgK6pQbzkK100?si=fc1c1f0b08b448f5", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    Daisy.add_field(name = "Run Speed", value = "1.595 `[60-64]`", inline=True)
    Daisy.add_field(name = "Air Speed", value = "1.029 `[48-50]`", inline=True)
    Daisy.add_field(name = "Fall Speed", value = "1.19 `[85-86]`", inline=False)
    Daisy.add_field(name = "Weight", value = "89 `[63-64]`", inline=True)
    Daisy.add_field(name = "Weightclass", value = "`Lightweight`", inline=True)
    Daisy.set_footer(text = "[X] = Rank out of 87.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(file = file, embed = Daisy)

client.run('ODE4MzM4NDYxNjQyNzg0NzY4.YEWnFQ.rOkL3TSSF9EDQpL7zsNUc035nj8')