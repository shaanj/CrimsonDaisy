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
    CrimsonDaisy = discord.Embed(title = "Help", type = "rich", description = "I am Crimson mf Daisy", color = 0xfca103)
    CrimsonDaisy.set_thumbnail(url="https://www.vggts.gdn/where/ssbu/13e%20VGGTS%20SSBU%20Daisy%20icon%20ver%202.png")
    CrimsonDaisy.set_author(name = "Crimson Daisy", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    CrimsonDaisy.add_field(name = "&smash <OPTIONAL @USER>", value = "Smash that mf", inline=False)
    CrimsonDaisy.add_field(name = "&<Smash Character (Daisy)>", value = "Smash Data (Absolute Scale and Ranks)", inline=False)
    CrimsonDaisy.set_footer(text = "For 2nd command, [X] = Rank out of 87.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(embed = CrimsonDaisy)

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


                                        
@client.command(name = 'Mario')            #Mario Command: #1
async def Mario(context):
    Mario = discord.Embed(title = "Donkey Kong (1981)", type = "rich", description = "Dunks on Dunks", color = 0xff0000)
    Mario.set_thumbnail(url="https://ssb.wiki.gallery/images/4/44/Mario_SSBU.png")
    Mario.set_author(name = "#1: Mario", url = "https://open.spotify.com/track/53BIF7mH7UL7yTzOsKIoEw?si=2e2258ae59594ec8", icon_url = "https://ssb.wiki.gallery/images/9/9e/MarioHeadSSBUWebsite.png")
    Mario.add_field(name = "Run Speed", value = "1.76 `[37-40]`", inline=True)
    Mario.add_field(name = "Air Speed", value = "1.208 `[13-17]`", inline=True)
    Mario.add_field(name = "Fall Speed", value = "1.5 `[57-60]`", inline=False)
    Mario.add_field(name = "Weight", value = "98 `[32-35]`", inline=True)
    Mario.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    Mario.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Mario)


@client.command(name = "DK")               #Donkey Kong Command: #2
async def DK(context):
    DK = discord.Embed(title = "Donkey Kong (1981)", type = "rich", description = "Cargo Throw is Fair", color = 0x97572b)
    DK.set_thumbnail(url="https://ssb.wiki.gallery/images/c/c9/Donkey_Kong_SSBU.png")
    DK.set_author(name = "#2: Donkey Kong", url = "https://open.spotify.com/track/05kvH7fHTyjvoZz0dM02sI?si=4d6ff97781814380", icon_url = "https://ssb.wiki.gallery/images/2/21/DonkeyKongHeadSSBUWebsite.png")
    DK.add_field(name = "Run Speed", value = "1.873 `[29]`", inline=True)
    DK.add_field(name = "Air Speed", value = "1.208 `[13-17]`", inline=True)
    DK.add_field(name = "Fall Speed", value = "1.63 `[38-39]`", inline=False)
    DK.add_field(name = "Weight", value = "127 `[3-4]`", inline=True)
    DK.add_field(name = "Weightclass", value = "`Super Heavyweight`", inline=True)
    await context.message.channel.send(embed = DK)


@client.command(name = "Link")             #Link Command: #3
async def Link(context):
    Link = discord.Embed(title = "The Legend of Zelda (1986)", type = "rich", description = "Just Keep Throwing Stuff", color = 0x00ffe8)
    Link.set_thumbnail(url="https://ssb.wiki.gallery/images/8/84/Link_SSBU.png")
    Link.set_author(name = "#3: Link", url = "https://open.spotify.com/track/78ogxEjGLVuQ3RSsYZokAL?si=2039b911326b4d68", icon_url = "https://ssb.wiki.gallery/images/2/2b/LinkHeadSSBUWebsite.png")
    Link.add_field(name = "Run Speed", value = "1.534 `[69]`", inline=True)
    Link.add_field(name = "Air Speed", value = "0.924 `[74-75]`", inline=True)
    Link.add_field(name = "Fall Speed", value = "1.6 `[42-46]`", inline=False)
    Link.add_field(name = "Weight", value = "104 `[21-25]`", inline=True)
    Link.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    await context.message.channel.send(embed = Link)


@client.command(name = "Samus")            #Samus Command: #4
async def Samus(context):
    Samus = discord.Embed(title = "Metroid (1986)", type = "rich", description = "Charge Shot Pressure Exists", color = 0xff9e00)
    Samus.set_thumbnail(url="https://ssb.wiki.gallery/images/0/03/Samus_SSBU.png")
    Samus.set_author(name = "#4: Samus", url = "https://open.spotify.com/track/1fy1z5EROb7b3tGHgc5fba?si=7589d8a106664bb5", icon_url = "https://ssb.wiki.gallery/images/d/d0/SamusHeadSSBUWebsite.png")
    Samus.add_field(name = "Run Speed", value = "1.654 `[50-51]`", inline=True)
    Samus.add_field(name = "Air Speed", value = "1.103 `[34-36]`", inline=True)
    Samus.add_field(name = "Fall Speed", value = "1.33 `[73-74]`", inline=False)
    Samus.add_field(name = "Weight", value = "108 `[9-12]`", inline=True)
    Samus.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    Samus.set_footer(text = "Exact same stats and ranks as Dark Samus \nCan: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = Samus)


@client.command(name = "DarkSamus")        #Dark Samus Command: #5
async def DarkSamus(context):
    DSamus = discord.Embed(title = "Metroid Prime (2002)", type = "rich", description = "'Technically' Better than Samus?", color = 0x5100ff)
    DSamus.set_thumbnail(url="https://ssb.wiki.gallery/images/a/a6/Dark_Samus_SSBU.png")
    DSamus.set_author(name = "#5: Dark Samus", url = "https://open.spotify.com/track/6IyEL4cPFXHWiVbLDdydoi?si=e3c423342fa94046", icon_url = "https://ssb.wiki.gallery/images/2/24/DarkSamusHeadSSBUWebsite.png")
    DSamus.add_field(name = "Run Speed", value = "1.654 `[50-51]`", inline=True)
    DSamus.add_field(name = "Air Speed", value = "1.103 `[34-36]`", inline=True)
    DSamus.add_field(name = "Fall Speed", value = "1.33 `[73-74]`", inline=False)
    DSamus.add_field(name = "Weight", value = "108 `[9-12]`", inline=True)
    DSamus.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    DSamus.set_footer(text = "Exact same stats and ranks as Samus \nCan: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = DSamus)


@client.command(name = "Yoshi")            #Yoshi Command: #6
async def Yoshi(context):
    Yoshi = discord.Embed(title = "Super Mario World (1990)", type = "rich", description = "Every Aerial is Busted", color = 0x31ff00)
    Yoshi.set_thumbnail(url="https://ssb.wiki.gallery/images/8/8d/Yoshi_SSBU.png")
    Yoshi.set_author(name = "#6: Yoshi", url = "https://open.spotify.com/track/2aFF05QA8gkXsX7Vv8UamP?si=0144388bea7a4259", icon_url = "https://ssb.wiki.gallery/images/9/93/YoshiHeadSSBUWebsite.png")
    Yoshi.add_field(name = "Run Speed", value = "2.046 `[19]`", inline=True)
    Yoshi.add_field(name = "Air Speed", value = "1.344 `[1]`", inline=True)
    Yoshi.add_field(name = "Fall Speed", value = "1.29 `[81]`", inline=False)
    Yoshi.add_field(name = "Weight", value = "104 `[21-25]`", inline=True)
    Yoshi.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    Yoshi.set_footer(text = "Fastest air speed in the game")
    await context.message.channel.send(embed = Yoshi)


@client.command(name = "Kirby")            #Kirby Command: #7
async def Kirby(context):
    Kirby = discord.Embed(title = "Kirby's Dream Land (1992)", type = "rich", description = "Neutral B Simps", color = 0xff008e)
    Kirby.set_thumbnail(url="https://ssb.wiki.gallery/images/0/07/Kirby_SSBU.png")
    Kirby.set_author(name = "#7: Kirby", url = "https://open.spotify.com/track/6yaFVOQLUI9RFTV9YVa6pZ?si=51bd337c18244cf1", icon_url = "https://ssb.wiki.gallery/images/1/15/KirbyHeadSSBUWebsite.png")
    Kirby.add_field(name = "Run Speed", value = "1.727 `[42]`", inline=True)
    Kirby.add_field(name = "Air Speed", value = "0.84 `[83]`", inline=True)
    Kirby.add_field(name = "Fall Speed", value = "1.23 `[83]`", inline=False)
    Kirby.add_field(name = "Weight", value = "79 `[77-81]`", inline=True)
    Kirby.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    await context.message.channel.send(embed = Kirby)


@client.command(name = "Fox")              #Fox Command: #8
async def Fox(context):
    Fox = discord.Embed(title = "Star Fox (1993)", type = "rich", description = "Dwayne 'Falls Like a Rock' Johnson", color = 0xc3bbc0)
    Fox.set_thumbnail(url="https://ssb.wiki.gallery/images/2/2f/Fox_SSBU.png")
    Fox.set_author(name = "#8: Fox", url = "https://open.spotify.com/track/22JH2DGnfmUKblTnv6VvdC?si=548ac152f0264363", icon_url = "https://ssb.wiki.gallery/images/c/c9/FoxHeadSSBUWebsite.png")
    Fox.add_field(name = "Run Speed", value = "2.402 `[6]`", inline=True)
    Fox.add_field(name = "Air Speed", value = "1.11 `[33]`", inline=True)
    Fox.add_field(name = "Fall Speed", value = "2.1 `[1]`", inline=False)
    Fox.add_field(name = "Weight", value = "77 `[83]`", inline=True)
    Fox.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    Fox.set_footer(text = "Can: Wall Jump \nHighest fall speed in the game")
    await context.message.channel.send(embed = Fox)


@client.command(name = "Pikachu")          #Pikachu Command: #9
async def Pikachu(context):
    Pikachu = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "You're Going To Have A Bad Time", color = 0xe9ff00)
    Pikachu.set_thumbnail(url="https://ssb.wiki.gallery/images/9/93/Pikachu_SSBU.png")
    Pikachu.set_author(name = "#9: Pikachu", url = "https://open.spotify.com/track/1HALda7HkI64vntdlGSa3X?si=ad73a1ab67394bf8", icon_url = "https://ssb.wiki.gallery/images/5/52/PikachuHeadSSBUWebsite.png")
    Pikachu.add_field(name = "Run Speed", value = "2.039 `[20]`", inline=True)
    Pikachu.add_field(name = "Air Speed", value = "0.957 `[65]`", inline=True)
    Pikachu.add_field(name = "Fall Speed", value = "1.55 `[52-55]`", inline=False)
    Pikachu.add_field(name = "Weight", value = "79 `[77-81]`", inline=True)
    Pikachu.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    Pikachu.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Pikachu)


@client.command(name = "Luigi")            #Luigi Command: #10
async def Luigi(context):
    Luigi = discord.Embed(title = "Mario Bros. (1983)", type = "rich", description = "Discount Waluigi", color = 0x00ff4b)
    Luigi.set_thumbnail(url="https://ssb.wiki.gallery/images/b/bb/Luigi_SSBU.png")
    Luigi.set_author(name = "#10: Luigi", url = "https://open.spotify.com/track/3sJ4smaOLXnHU4TIgE5xNz?si=eeabf5f43eaa40d7", icon_url = "https://ssb.wiki.gallery/images/9/9d/LuigiHeadSSBUWebsite.png")
    Luigi.add_field(name = "Run Speed", value = "1.65 `[52-54]`", inline=True)
    Luigi.add_field(name = "Air Speed", value = "0.77 `[86]`", inline=True)
    Luigi.add_field(name = "Fall Speed", value = "1.32 `[75-76]`", inline=False)
    Luigi.add_field(name = "Weight", value = "97 `[36-38]`", inline=True)
    Luigi.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    await context.message.channel.send(embed = Luigi)


@client.command(name = "Ness")             #Ness Command: #11
async def Ness(context):
    Ness = discord.Embed(title = "EarthBound (1994)", type = "rich", description = "PK Fire Spam Is Trash", color = 0xff0000)
    Ness.set_thumbnail(url="https://ssb.wiki.gallery/images/8/82/Ness_SSBU.png")
    Ness.set_author(name = "#11: Ness", url = "https://open.spotify.com/track/3JlK5EtPgo2cykk5BtIJUo?si=9c782a41638a4749", icon_url = "https://ssb.wiki.gallery/images/d/d5/NessHeadSSBUWebsite.png")
    Ness.add_field(name = "Run Speed", value = "1.609 `[57]`", inline=True)
    Ness.add_field(name = "Air Speed", value = "1.007 `[57]`", inline=True)
    Ness.add_field(name = "Fall Speed", value = "1.31 `[77]`", inline=False)
    Ness.add_field(name = "Weight", value = "94 `[47-50]`", inline=True)
    Ness.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    await context.message.channel.send(embed = Ness)


@client.command(name = "Falcon")           #Captain Falcon Command: #12
async def Falcon(context):
    Falcon = discord.Embed(title = "F-Zero (1990)", type = "rich", description = "Falcon Punch", color = 0x0074ff)
    Falcon.set_thumbnail(url="https://ssb.wiki.gallery/images/d/da/Captain_Falcon_SSBU.png")
    Falcon.set_author(name = "#12: Captain Falcon", url = "https://open.spotify.com/track/6A8OpxPRBP8p4kE3fZEa1Q?si=e94d49541e6b456c", icon_url = "https://ssb.wiki.gallery/images/6/6b/CaptainFalconHeadSSBUWebsite.png")
    Falcon.add_field(name = "Run Speed", value = "2.552 `[2]`", inline=True)
    Falcon.add_field(name = "Air Speed", value = "1.218 `[12]`", inline=True)
    Falcon.add_field(name = "Fall Speed", value = "1.865 `[8]`", inline=False)
    Falcon.add_field(name = "Weight", value = "104 `[21-25]`", inline=True)
    Falcon.add_field(name = "Weightclass", value = "`Heavyweight`", inline=True)
    Falcon.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Falcon)


@client.command(name = "Puff")             #Jigglypuff Command: #13
async def Puff(context):
    Puff = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "HungryBox", color = 0xf89fff)
    Puff.set_thumbnail(url="https://ssb.wiki.gallery/images/6/6a/Jigglypuff_SSBU.png")
    Puff.set_author(name = "#13: Jigglypuff", url = "https://open.spotify.com/track/1WPMIgPIBsY0oMhWOTfXXQ?si=ad0090dc8f9b4a72", icon_url = "https://ssb.wiki.gallery/images/9/90/JigglypuffHeadSSBUWebsite.png")
    Puff.add_field(name = "Run Speed", value = "1.271 `[85]`", inline=True)
    Puff.add_field(name = "Air Speed", value = "1.332 `[2]`", inline=True)
    Puff.add_field(name = "Fall Speed", value = "0.98 `[87]`", inline=False)
    Puff.add_field(name = "Weight", value = "68 `[86]`", inline=True)
    Puff.add_field(name = "Weightclass", value = "`Balloonweight`", inline=True)
    Puff.set_footer(text = "Slowest fall speed (floatiest) in the game")
    await context.message.channel.send(embed = Puff)








@client.command(name = 'Peach')            #Peach Command: #14
async def Peach(context):
    Peach = discord.Embed(title = "Super Mario Bros. (1985)", type = "rich", description = "Overrated, Float Cancels Still OP", color = 0xff008b)
    Peach.set_thumbnail(url="https://ssb.wiki.gallery/images/7/74/Peach_SSBU.png")
    Peach.set_author(name = "#14: Peach", url = "https://open.spotify.com/track/126jlTTSRGaZ5WX8e4Tv7M?si=1de226102cb44eba", icon_url = "https://ssb.wiki.gallery/images/1/14/PeachHeadSSBUWebsite.png")
    Peach.add_field(name = "Run Speed", value = "1.595 `[60-64]`", inline=True)
    Peach.add_field(name = "Air Speed", value = "1.029 `[48-50]`", inline=True)
    Peach.add_field(name = "Fall Speed", value = "1.19 `[85-86]`", inline=False)
    Peach.add_field(name = "Weight", value = "89 `[63-64]`", inline=True)
    Peach.add_field(name = "Weightclass", value = "`Lightweight`", inline=True)
    Peach.set_footer(text = "Exact same stats and ranks as Daisy")
    await context.message.channel.send(embed = Peach)


@client.command(name = 'Daisy')            #Daisy Command: #15
async def Daisy(context):
    Daisy = discord.Embed(title = "Super Mario Land (1989)", type = "rich", description = "My Main, Float Cancels OP", color = 0xfca103)
    Daisy.set_thumbnail(url="https://ssb.wiki.gallery/images/2/21/Daisy_SSBU.png")
    Daisy.set_author(name = "#15: Daisy", url = "https://open.spotify.com/track/63ZMWm1RPYgK6pQbzkK100?si=fc1c1f0b08b448f5", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    Daisy.add_field(name = "Run Speed", value = "1.595 `[60-64]`", inline=True)
    Daisy.add_field(name = "Air Speed", value = "1.029 `[48-50]`", inline=True)
    Daisy.add_field(name = "Fall Speed", value = "1.19 `[85-86]`", inline=False)
    Daisy.add_field(name = "Weight", value = "89 `[63-64]`", inline=True)
    Daisy.add_field(name = "Weightclass", value = "`Lightweight`", inline=True)
    Daisy.set_footer(text = "Exact same stats and ranks as Peach")
    await context.message.channel.send(embed = Daisy)


@client.command(name = 'Bowser')           #Bowser Command: #16
async def Bowser(context):
    Bowser = discord.Embed(title = "Super Mario Bros. (1985)", type = "rich", description = "Always Dies 200+ Percent", color = 0xed9600)
    Bowser.set_thumbnail(url="https://ssb.wiki.gallery/images/4/49/Bowser_SSBU.png")
    Bowser.set_author(name = "#16: Bowser", url = "https://open.spotify.com/track/7C5irIYGVe9xHfJX0Dt5Lf?si=6ea98b3dde0d4fb7", icon_url = "https://ssb.wiki.gallery/images/0/0b/BowserHeadSSBUWebsite.png")
    Bowser.add_field(name = "Run Speed", value = "1.971 `[22]`", inline=True)
    Bowser.add_field(name = "Air Speed", value = "1.155 `[20-25]`", inline=True)
    Bowser.add_field(name = "Fall Speed", value = "1.77 `[20-21]`", inline=False)
    Bowser.add_field(name = "Weight", value = "135 `[1]`", inline=True)
    Bowser.add_field(name = "Weightclass", value = "`Super Heavyweight`", inline=True)
    Bowser.set_footer(text = "Heaviest character in the game")
    await context.message.channel.send(embed = Bowser)


@client.command(name = 'Icies')            #Ice Climbers Command: #17
async def Icies(context):
    Icies = discord.Embed(title = "Ice Climber (1985)", type = "rich", description = "Nana Hard Carries", color = 0x2082f0)
    Icies.set_thumbnail(url="https://ssb.wiki.gallery/images/1/12/Ice_Climbers_SSBU.png")
    Icies.set_author(name = "#17: Ice Climbers", url = "https://open.spotify.com/track/0I29UjYWT3zIjPLqB6h5GV?si=e871653946244d26", icon_url = "https://ssb.wiki.gallery/images/0/0c/IceClimbersHeadSSBUWebsite.png")
    Icies.add_field(name = "Run Speed", value = "1.53 `[70]`", inline=True)
    Icies.add_field(name = "Air Speed", value = "0.83 `[84-85]`", inline=True)
    Icies.add_field(name = "Fall Speed", value = "1.3 `[78-80]`", inline=False)
    Icies.add_field(name = "Weight", value = "92 `[52-57]`", inline=True)
    Icies.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    await context.message.channel.send(embed = Icies)


@client.command(name = 'Sheik')            #Sheik Command: #18
async def Sheik(context):
    Sheik = discord.Embed(title = "The Legend of Zelda: Ocarina of Time (1998)", type = "rich", description = "Gutted From Smash 4", color = 0xb57be2)
    Sheik.set_thumbnail(url="https://ssb.wiki.gallery/images/0/00/Sheik_SSBU.png")
    Sheik.set_author(name = "#18: Sheik", url = "https://open.spotify.com/track/4OhdW1oEYxLKLsOrznmC0s?si=6ec46041acf44bf7", icon_url = "https://ssb.wiki.gallery/images/1/1e/SheikHeadSSBUWebsite.png")
    Sheik.add_field(name = "Run Speed", value = "2.42 `[4]`", inline=True)
    Sheik.add_field(name = "Air Speed", value = "1.155 `[20-25]`", inline=True)
    Sheik.add_field(name = "Fall Speed", value = "1.75 `[24-25]`", inline=False)
    Sheik.add_field(name = "Weight", value = "78 `[82]`", inline=True)
    Sheik.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    Sheik.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = Sheik)


@client.command(name = 'Zelda')            #Zelda Command: #19
async def Zelda(context):
    Zelda = discord.Embed(title = "The Legend of Zelda (1986)", type = "rich", description = "Phantom Mechanics", color = 0xdd92ee)
    Zelda.set_thumbnail(url="https://ssb.wiki.gallery/images/c/c8/Zelda_SSBU.png")
    Zelda.set_author(name = "#19: Zelda", url = "https://open.spotify.com/track/2TlSTYsyVP3ZOEaA81bnBc?si=0444ae37db524ba1", icon_url = "https://ssb.wiki.gallery/images/c/c8/ZeldaHeadSSBUWebsite.png")
    Zelda.add_field(name = "Run Speed", value = "1.43 `[78-79]`", inline=True)
    Zelda.add_field(name = "Air Speed", value = "1.092 `[39-40]`", inline=True)
    Zelda.add_field(name = "Fall Speed", value = "1.35 `[69-72]`", inline=False)
    Zelda.add_field(name = "Weight", value = "85 `[71]`", inline=True)
    Zelda.add_field(name = "Weightclass", value = "`Lightweight`", inline=True)
    await context.message.channel.send(embed = Zelda)


@client.command(name = 'Doc')         #Dr. Mario Command: #20
async def Doc(context):
    Doc = discord.Embed(title = "Dr. Mario (1990)", type = "rich", description = "Back Throw Yeets People", color = 0x60979e)
    Doc.set_thumbnail(url="https://ssb.wiki.gallery/images/3/3f/Dr._Mario_SSBU.png")
    Doc.set_author(name = "#20: Dr. Mario", url = "https://open.spotify.com/track/1zAecnWOvzfFuAEIyUfZs5?si=8e34c9d823a846bd", icon_url = "https://ssb.wiki.gallery/images/c/c8/DrMarioHeadSSBUWebsite.png")
    Doc.add_field(name = "Run Speed", value = "1.397792 `[80]`", inline=True)
    Doc.add_field(name = "Air Speed", value = "0.9238784 `[76]`", inline=True)
    Doc.add_field(name = "Fall Speed", value = "1.5 `[57-60]`", inline=False)
    Doc.add_field(name = "Weight", value = "98 `[32-35]`", inline=True)
    Doc.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    Doc.set_footer(text = "Can: Wall Jump \nI can't believe that those are his actual stats!")
    await context.message.channel.send(embed = Doc)


@client.command(name = 'Pichu')            #Pichu Command: #21
async def Pichu(context):
    Pichu = discord.Embed(title = "Pokemon Gold and Silver (1999)", type = "rich", description = "Dumb Yellow Rat", color = 0xf8ff00)
    Pichu.set_thumbnail(url="https://ssb.wiki.gallery/images/c/c1/Pichu_SSBU.png")
    Pichu.set_author(name = "#21: Pichu", url = "https://open.spotify.com/track/0Qaavj6icd6p3BAnwGEtG9?si=63f8b729549548cd", icon_url = "https://ssb.wiki.gallery/images/5/50/PichuHeadSSBUWebsite.png")
    Pichu.add_field(name = "Run Speed", value = "1.892 `[28]`", inline=True)
    Pichu.add_field(name = "Air Speed", value = "1.029 `[48-50]`", inline=True)
    Pichu.add_field(name = "Fall Speed", value = "1.9 `[6]`", inline=False)
    Pichu.add_field(name = "Weight", value = "62 `[87]`", inline=True)
    Pichu.add_field(name = "Weightclass", value = "`Balloonweight`", inline=True)
    Pichu.set_footer(text = "Can: Wall Jump \nLightest character in the game")
    await context.message.channel.send(embed = Pichu)


@client.command(name = 'Falco')            #Falco Command: #22
async def Falco(context):
    Falco = discord.Embed(title = "Star Fox (1993)", type = "rich", description = "That Ain't Falco", color = 0x0074ff)
    Falco.set_thumbnail(url="https://ssb.wiki.gallery/images/8/80/Falco_SSBU.png")
    Falco.set_author(name = "#22: Falco", url = "https://open.spotify.com/track/3ME5GLvAN1FroRF4qFNXjW?si=7c5b0dfdb9b847a1", icon_url = "https://ssb.wiki.gallery/images/6/6e/FalcoHeadSSBUWebsite.png")
    Falco.add_field(name = "Run Speed", value = "1.619 `[55]`", inline=True)
    Falco.add_field(name = "Air Speed", value = "0.977 `[63]`", inline=True)
    Falco.add_field(name = "Fall Speed", value = "1.8 `[13-18]`", inline=False)
    Falco.add_field(name = "Weight", value = "82 `[72-73]`", inline=True)
    Falco.add_field(name = "Weightclass", value = "`Featherweight`", inline=True)
    Falco.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Falco)


@client.command(name = 'Marth')            #Marth Command: #23
async def Marth(context):
    Marth = discord.Embed(title = "Fire Emblem: Shadow Dragon and the Blade of Light (1993)", type = "rich", description = "Just The Tip", color = 0x0074ff)
    Marth.set_thumbnail(url="https://ssb.wiki.gallery/images/e/e9/Marth_SSBU.png")
    Marth.set_author(name = "#23: Marth", url = "https://open.spotify.com/track/2Cn5v5xb9WqnxqPrEFwUjS?si=475aa9eb4b4b4256", icon_url = "https://ssb.wiki.gallery/images/a/ae/MarthHeadSSBUWebsite.png")
    Marth.add_field(name = "Run Speed", value = "1.964 `[23-24]`", inline=True)
    Marth.add_field(name = "Air Speed", value = "1.071 `[41-42]`", inline=True)
    Marth.add_field(name = "Fall Speed", value = "1.58 `[47-50]`", inline=False)
    Marth.add_field(name = "Weight", value = "90 `[60-62]`", inline=True)
    Marth.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    Marth.set_footer(text = "Exact same stats and rank as Lucina \nOnly difference: Tip of the sword is stronger")
    await context.message.channel.send(embed = Marth)


@client.command(name = 'Lucina')           #Lucina Command: #24
async def Lucina(context):
    Lucina = discord.Embed(title = "Fire Emblem Awakening (2012)", type = "rich", description = "Real Marth, Too Safe", color = 0x0152b3)
    Lucina.set_thumbnail(url="https://ssb.wiki.gallery/images/d/dc/Lucina_SSBU.png")
    Lucina.set_author(name = "#24: Lucina", url = "https://open.spotify.com/track/1EV465Il8JJQlwJQQmXCn6?si=dd845cd0c7154354", icon_url = "https://ssb.wiki.gallery/images/d/d8/LucinaHeadSSBUWebsite.png")
    Lucina.add_field(name = "Run Speed", value = "1.964 `[23-24]`", inline=True)
    Lucina.add_field(name = "Air Speed", value = "1.071 `[41-42]`", inline=True)
    Lucina.add_field(name = "Fall Speed", value = "1.58 `[47-50]`", inline=False)
    Lucina.add_field(name = "Weight", value = "90 `[60-62]`", inline=True)
    Lucina.add_field(name = "Weightclass", value = "`Middleweight`", inline=True)
    Lucina.set_footer(text = "Exact same stats and rank as Marth \nOnly difference: All parts of the sword are strong")
    await context.message.channel.send(embed = Lucina)


@client.command(name = 'YoungLink')        #Young Link Command: #25
async def YoungLink(context):
    YLink = discord.Embed(title = "The Legend of Zelda: Ocarina of Time (1998)", type = "rich", description = "The Most Annoying Link", color = 0x00ff4b)
    YLink.set_thumbnail(url="https://ssb.wiki.gallery/images/8/8a/Young_Link_SSBU.png")
    YLink.set_author(name = "#25: Young Link", url = "https://open.spotify.com/track/4eA9VHcNALbJh4cLcCWHWs?si=a3901eab68d54ee2", icon_url = "https://ssb.wiki.gallery/images/c/c0/YoungLinkHeadSSBUWebsite.png")
    YLink.add_field(name = "Run Speed", value = "1.749 `[41]`", inline=True)
    YLink.add_field(name = "Air Speed", value = "0.966 `[64]`", inline=True)
    YLink.add_field(name = "Fall Speed", value = "1.8 `[13-18]`", inline=False)
    YLink.add_field(name = "Weight", value = "88 `[65-67]`", inline=True)
    YLink.add_field(name = "Weightclass", value = "`Lightweight`", inline=True)
    YLink.set_footer(text = "Can: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = YLink)


@client.command(name = 'Ganondorf')        #Ganondorf Command: #26
async def Ganondorf(context):
    Ganon = discord.Embed(title = "The Legend of Zelda: Ocarina of Time (1998)", type = "rich", description = "The King of Disrespect", color = 0x5400b8)
    Ganon.set_thumbnail(url="https://ssb.wiki.gallery/images/9/91/Ganondorf_SSBU.png")
    Ganon.set_author(name = "#26: Ganondorf", url = "https://open.spotify.com/track/7kWqgvTLq4pb5nGqtwJREJ?si=ebd635b0f04445e5", icon_url = "https://ssb.wiki.gallery/images/b/b6/GanondorfHeadSSBUWebsite.png")
    Ganon.add_field(name = "Run Speed", value = "1.34 `[84]`", inline=True)
    Ganon.add_field(name = "Air Speed", value = "0.83 `[84-85]`", inline=True)
    Ganon.add_field(name = "Fall Speed", value = "1.65 `[32-37]`", inline=False)
    Ganon.add_field(name = "Weight", value = "118 `[5]`", inline=True)
    Ganon.add_field(name = "Weightclass", value = "`Super Heavyweight`", inline=True)
    await context.message.channel.send(embed = Ganon)










client.run('ODE4MzM4NDYxNjQyNzg0NzY4.YEWnFQ.rOkL3TSSF9EDQpL7zsNUc035nj8')