import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix='&', help_command=None, case_insensitive = True)

@client.event
async def on_ready():
    print('Bot is ready.')
    general_channel = client.get_channel(818338932319846414)
    await general_channel.send('Hello Shaan.')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('&help Super Smash Bros. Ultimate'))

@client.command(name = 'help')
async def help(context):
    file = discord.File("Images/DaisyIcon.png", filename = "image.png")
    CrimsonDaisy = discord.Embed(title = "Help", type = "rich", description = "I am Crimson mf Daisy", color = 0xfca103)
    CrimsonDaisy.set_thumbnail(url="attachment://image.png")
    CrimsonDaisy.set_author(name = "Crimson Daisy", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    CrimsonDaisy.add_field(name = "&smash <OPTIONAL @USER>", value = "Smash that mf", inline=False)
    CrimsonDaisy.add_field(name = "&<Smash Character (Daisy)>", value = "Smash Data (Absolute Scale and Ranks)", inline=False)
    CrimsonDaisy.set_footer(text = "For 2nd command, [X] = Rank out of 87.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(file = file, embed = CrimsonDaisy)

@client.event
async def on_message(message):
    if message.author == client.user: return

    if "hello" in message.content:
        await message.channel.send("Hello! " + message.author.mention)

    if "smash" in message.content and "&" not in message.content:
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
    Mario.set_footer(text = "Can: Wall Jump")
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
    await context.message.channel.send(file = file, embed = DK)


@client.command(name = "Link")            #Link Command: #3
async def Link(context):
    file = discord.File("Images/LinkImage.png", filename = "image.png")
    Link = discord.Embed(title = "The Legend of Zelda (1986)", type = "rich", description = "Spams from Specials", color = 0x00ffe8)
    Link.set_thumbnail(url="attachment://image.png")
    Link.set_author(name = "#3: Link", url = "https://open.spotify.com/track/78ogxEjGLVuQ3RSsYZokAL?si=2039b911326b4d68", icon_url = "https://ssb.wiki.gallery/images/2/2b/LinkHeadSSBUWebsite.png")
    Link.add_field(name = "Run Speed", value = "1.534 `[69]`", inline=True)
    Link.add_field(name = "Air Speed", value = "0.924 `[74-75]`", inline=True)
    Link.add_field(name = "Fall Speed", value = "1.6 `[42-46]`", inline=False)
    Link.add_field(name = "Weight", value = "104 `[21-25]`", inline=True)
    Link.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    await context.message.channel.send(file = file, embed = Link)


@client.command(name = "Samus")            #Samus Command: #4
async def Samus(context):
    file = discord.File("Images/SamusImage.png", filename = "image.png")
    Samus = discord.Embed(title = "Metroid (1986)", type = "rich", description = "Charge Shot Pressure Exists", color = 0xff9e00)
    Samus.set_thumbnail(url="attachment://image.png")
    Samus.set_author(name = "#4: Samus", url = "https://open.spotify.com/track/1fy1z5EROb7b3tGHgc5fba?si=7589d8a106664bb5", icon_url = "https://ssb.wiki.gallery/images/d/d0/SamusHeadSSBUWebsite.png")
    Samus.add_field(name = "Run Speed", value = "1.654 `[50-51]`", inline=True)
    Samus.add_field(name = "Air Speed", value = "1.103 `[34-36]`", inline=True)
    Samus.add_field(name = "Fall Speed", value = "1.33 `[73-74]`", inline=False)
    Samus.add_field(name = "Weight", value = "108 `[9-12]`", inline=True)
    Samus.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    Samus.set_footer(text = "Exact same stats as Dark Samus \nCan: Wall Jump, Tether Recovery")
    await context.message.channel.send(file = file, embed = Samus)


@client.command(name = "DarkSamus")            #Dark Samus Command: #5
async def DarkSamus(context):
    file = discord.File("Images/DarkSamusImage.png", filename = "image.png")
    DSamus = discord.Embed(title = "Metroid Prime (2002)", type = "rich", description = "'Technically' Better than Samus?", color = 0x5100ff)
    DSamus.set_thumbnail(url="attachment://image.png")
    DSamus.set_author(name = "#5: Dark Samus", url = "https://open.spotify.com/track/6IyEL4cPFXHWiVbLDdydoi?si=e3c423342fa94046", icon_url = "https://ssb.wiki.gallery/images/2/24/DarkSamusHeadSSBUWebsite.png")
    DSamus.add_field(name = "Run Speed", value = "1.654 `[50-51]`", inline=True)
    DSamus.add_field(name = "Air Speed", value = "1.103 `[34-36]`", inline=True)
    DSamus.add_field(name = "Fall Speed", value = "1.33 `[73-74]`", inline=False)
    DSamus.add_field(name = "Weight", value = "108 `[9-12]`", inline=True)
    DSamus.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    DSamus.set_footer(text = "Exact same stats and ranks as Samus \nCan: Wall Jump, Tether Recovery")
    await context.message.channel.send(file = file, embed = DSamus)


@client.command(name = "Yoshi")            #Yoshi Command: #6
async def Yoshi(context):
    file = discord.File("Images/YoshiImage.png", filename = "image.png")
    Yoshi = discord.Embed(title = "Super Mario World (1990)", type = "rich", description = "Every Aerial is Busted", color = 0x31ff00)
    Yoshi.set_thumbnail(url="attachment://image.png")
    Yoshi.set_author(name = "#6: Yoshi", url = "https://open.spotify.com/track/2aFF05QA8gkXsX7Vv8UamP?si=0144388bea7a4259", icon_url = "https://ssb.wiki.gallery/images/9/93/YoshiHeadSSBUWebsite.png")
    Yoshi.add_field(name = "Run Speed", value = "2.046 `[19]`", inline=True)
    Yoshi.add_field(name = "Air Speed", value = "1.344 `[1]`", inline=True)
    Yoshi.add_field(name = "Fall Speed", value = "1.29 `[81]`", inline=False)
    Yoshi.add_field(name = "Weight", value = "104 `[21-25]`", inline=True)
    Yoshi.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    Yoshi.set_footer(text = "Fastest air speed in the game")
    await context.message.channel.send(file = file, embed = Yoshi)


@client.command(name = "Kirby")            #Kirby Command: #7
async def Kirby(context):
    file = discord.File("Images/KirbyImage.png", filename = "image.png")
    Kirby = discord.Embed(title = "Kirby's Dream Land (1992)", type = "rich", description = "Neutral B Simps", color = 0xff008e)
    Kirby.set_thumbnail(url="attachment://image.png")
    Kirby.set_author(name = "#7: Kirby", url = "https://open.spotify.com/track/6yaFVOQLUI9RFTV9YVa6pZ?si=51bd337c18244cf1", icon_url = "https://ssb.wiki.gallery/images/1/15/KirbyHeadSSBUWebsite.png")
    Kirby.add_field(name = "Run Speed", value = "1.727 `[42]`", inline=True)
    Kirby.add_field(name = "Air Speed", value = "0.84 `[83]`", inline=True)
    Kirby.add_field(name = "Fall Speed", value = "1.23 `[83]`", inline=False)
    Kirby.add_field(name = "Weight", value = "79 `[77-81]`", inline=True)
    Kirby.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    await context.message.channel.send(file = file, embed = Kirby)


@client.command(name = "Fox")            #Fox Command: #8
async def Fox(context):
    file = discord.File("Images/FoxImage.png", filename = "image.png")
    Fox = discord.Embed(title = "Star Fox (1993)", type = "rich", description = "Literally falls like a rock", color = 0xc3bbc0)
    Fox.set_thumbnail(url="attachment://image.png")
    Fox.set_author(name = "#8: Fox", url = "https://open.spotify.com/track/22JH2DGnfmUKblTnv6VvdC?si=548ac152f0264363", icon_url = "https://ssb.wiki.gallery/images/c/c9/FoxHeadSSBUWebsite.png")
    Fox.add_field(name = "Run Speed", value = "2.402 `[6]`", inline=True)
    Fox.add_field(name = "Air Speed", value = "1.11 `[33]`", inline=True)
    Fox.add_field(name = "Fall Speed", value = "2.1 `[1]`", inline=False)
    Fox.add_field(name = "Weight", value = "77 `[83]`", inline=True)
    Fox.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    Fox.set_footer(text = "Can: Wall Jump \nHighest fall speed in the game")
    await context.message.channel.send(file = file, embed = Fox)


@client.command(name = "Pikachu")            #Pikachu Command: #9
async def Pikachu(context):
    file = discord.File("Images/PikachuImage.png", filename = "image.png")
    Pikachu = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "I hate this character", color = 0xe9ff00)
    Pikachu.set_thumbnail(url="attachment://image.png")
    Pikachu.set_author(name = "#9: Pikachu", url = "https://open.spotify.com/track/1HALda7HkI64vntdlGSa3X?si=ad73a1ab67394bf8", icon_url = "https://ssb.wiki.gallery/images/5/52/PikachuHeadSSBUWebsite.png")
    Pikachu.add_field(name = "Run Speed", value = "2.039 `[20]`", inline=True)
    Pikachu.add_field(name = "Air Speed", value = "0.957 `[65]`", inline=True)
    Pikachu.add_field(name = "Fall Speed", value = "1.55 `[52-55]`", inline=False)
    Pikachu.add_field(name = "Weight", value = "79 `[77-81]`", inline=True)
    Pikachu.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    Pikachu.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(file = file, embed = Pikachu)


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
    Peach.set_footer(text = "Exact same stats and ranks as Daisy")
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
    Daisy.set_footer(text = "Exact same stats and ranks as Peach")
    await context.message.channel.send(file = file, embed = Daisy)

client.run('ODE4MzM4NDYxNjQyNzg0NzY4.YEWnFQ.rOkL3TSSF9EDQpL7zsNUc035nj8')