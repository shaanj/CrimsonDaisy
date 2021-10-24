import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

client = commands.Bot(command_prefix='&', help_command=None, case_insensitive = True)

RunSpd = "Run Speed"
AirSpd = "Air Speed"
FallSpd = "Fall Speed"
Weight = "Weight"
Weightclass = "Weightclass"

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")


@client.event
async def on_ready():
    print('Bot is ready.')
    general_channel = client.get_channel(818338932319846414)
    await general_channel.send('Hello Shaan.')
    await client.change_presence(status = discord.Status.online, activity = discord.Game('&help Super Smash Bros. Ultimate'))

@client.command(name = 'help')
async def help(context):
    CrimsonDaisy = discord.Embed(title = "Help", type = "rich", description = "I am Crimson mf Daisy", color = 0xfca103)
    CrimsonDaisy.set_thumbnail(url = "https://www.vggts.gdn/where/ssbu/13e%20VGGTS%20SSBU%20Daisy%20icon%20ver%202.png")
    CrimsonDaisy.set_author(name = "Crimson Daisy", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    CrimsonDaisy.add_field(name = "&smash [Optional @User]", value = "Smash that mf", inline = True)
    CrimsonDaisy.add_field(name = "&Daisy [Smash Character]", value = "Smash Data (Absolute Scale & Ranks)", inline = True)
    CrimsonDaisy.add_field(name = "&Names", value = "Special Fighter Command Names", inline = False)
    CrimsonDaisy.set_footer(text = "[X] = Rank out of 88.\n[X-Y] = More than 1 character has this rank.")
    await context.message.channel.send(embed = CrimsonDaisy)

@client.event
async def on_message(message):
    if message.author == client.user: return

    if "hello" in message.content and "&" not in message.content:
        await message.channel.send("Hello! " + message.author.mention)

    if "smash" in message.content and "&" not in message.content:
        await message.channel.send("I'll smash your dad")

    await client.process_commands(message)


@client.event
async def on_command_error(context, error):
    if isinstance(error, commands.CommandNotFound):
        await context.send("bruh you mf stupid, god damn")


@client.command(name = 'smash')
async def smash(context, user : discord.User = None):
    if not user:
        await context.send("Fire Emblem exists")
    else:
        await context.send("I'm gonna smash " + user.mention)


@client.command(name = 'Names')            #Fighter Names
async def Names(context):
    Names = discord.Embed(title = "Fighter Names", type = "rich", description = "Special Fighter Name Commands", color = 0xff0000)
    Names.set_thumbnail(url = "https://ssb.wiki.gallery/images/4/44/Mario_SSBU.png")
    Names.set_author(name = "The Names", url = "https://open.spotify.com/track/53BIF7mH7UL7yTzOsKIoEw?si=2e2258ae59594ec8", icon_url = "https://ssb.wiki.gallery/images/9/9e/MarioHeadSSBUWebsite.png")
    Names.add_field(name = "Bayonetta", value = "`bayo`", inline = True)
    Names.add_field(name = "Bowser Jr.", value = "`bowserjr`", inline = True)
    Names.add_field(name = "Captain Falcon", value = "`falcon`", inline = True)
    Names.add_field(name = "Dark Pit", value = "`darkpit`", inline = True)
    Names.add_field(name = "Dark Samus", value = "`darksamus`", inline = True)
    Names.add_field(name = "Diddy Kong", value = "`diddy`", inline = True)
    Names.add_field(name = "Donkey Kong", value = "`dk`", inline = True)
    Names.add_field(name = "Dr. Mario", value = "`doc`", inline = True)
    Names.add_field(name = "Duck Hunt", value = "`duckhunt`", inline = True)
    Names.add_field(name = "Ganondorf", value = "`ganon`", inline = True)
    Names.add_field(name = "Mr. Game and Watch", value = "`gnw`", inline = True)
    Names.add_field(name = "Ice Climbers", value = "`icies`", inline = True)
    Names.add_field(name = "Jigglypuff", value = "`puff`", inline = True)
    Names.add_field(name = "King Dedede", value = "`ddd`", inline = True)
    Names.add_field(name = "King K. Rool", value = "`krool`", inline = True)
    Names.add_field(name = "Little Mac", value = "`mac`", inline = True)
    Names.add_field(name = "Meta Knight", value = "`mk`", inline = True)
    Names.add_field(name = "Pac-Man", value = "`pacman`", inline = True)
    Names.add_field(name = "Piranha Plant", value = "`plant`", inline = True)
    Names.add_field(name = "Pokemon Trainer", value = "`squirtle`, `ivysaur`, `charizard`", inline = True)
    Names.add_field(name = "Rosalina & Luma", value = "`rosa`", inline = True)
    Names.add_field(name = "Toon Link", value = "`toonlink`", inline = True)
    Names.add_field(name = "Wii Fit Trainer", value = "`wiifit`", inline = True)
    Names.add_field(name = "Young Link", value = "`younglink`", inline = True)
    Names.add_field(name = "Zero Suit Samus", value = "`zss`", inline = True)
    Names.set_footer(text = "For All Other Fighters, Use Their Regular Names.\nDaisy = &Daisy, Ivysaur = &Ivysaur")
    await context.message.channel.send(embed = Names)








@client.command(name = 'Mario')            #Mario Command: #1       FIRST ROW STARTS HERE
async def Mario(context):
    Mario = discord.Embed(title = "Donkey Kong (1981)", type = "rich", description = "Dunks on Dunks", color = 0xff0000)
    Mario.set_thumbnail(url = "https://ssb.wiki.gallery/images/4/44/Mario_SSBU.png")
    Mario.set_author(name = "#1: Mario", url = "https://open.spotify.com/track/53BIF7mH7UL7yTzOsKIoEw?si=2e2258ae59594ec8", icon_url = "https://ssb.wiki.gallery/images/9/9e/MarioHeadSSBUWebsite.png")
    Mario.add_field(name = RunSpd, value = "1.76 `[37-40]`", inline = True)
    Mario.add_field(name = AirSpd, value = "1.208 `[13-17]`", inline = True)
    Mario.add_field(name = FallSpd, value = "1.5 `[57-60]`", inline = False)
    Mario.add_field(name = Weight, value = "98 `[32-35]`", inline = True)
    Mario.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Mario.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Mario)


@client.command(name = "DK")               #Donkey Kong Command: #2
async def DK(context):
    DK = discord.Embed(title = "Donkey Kong (1981)", type = "rich", description = "Expand Dong", color = 0x97572b)
    DK.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/c9/Donkey_Kong_SSBU.png")
    DK.set_author(name = "#2: Donkey Kong", url = "https://open.spotify.com/track/05kvH7fHTyjvoZz0dM02sI?si=4d6ff97781814380", icon_url = "https://ssb.wiki.gallery/images/2/21/DonkeyKongHeadSSBUWebsite.png")
    DK.add_field(name = RunSpd, value = "1.873 `[29]`", inline = True)
    DK.add_field(name = AirSpd, value = "1.208 `[13-17]`", inline = True)
    DK.add_field(name = FallSpd, value = "1.63 `[38-39]`", inline = False)
    DK.add_field(name = Weight, value = "127 `[3-4]`", inline = True)
    DK.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    await context.message.channel.send(embed = DK)


@client.command(name = "Link")             #Link Command: #3
async def Link(context):
    Link = discord.Embed(title = "The Legend of Zelda (1986)", type = "rich", description = "Just Keep Throwing Stuff", color = 0x00ffe8)
    Link.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/84/Link_SSBU.png")
    Link.set_author(name = "#3: Link", url = "https://open.spotify.com/track/78ogxEjGLVuQ3RSsYZokAL?si=2039b911326b4d68", icon_url = "https://ssb.wiki.gallery/images/2/2b/LinkHeadSSBUWebsite.png")
    Link.add_field(name = RunSpd, value = "1.534 `[69]`", inline = True)
    Link.add_field(name = AirSpd, value = "0.924 `[74-75]`", inline = True)
    Link.add_field(name = FallSpd, value = "1.6 `[42-46]`", inline = False)
    Link.add_field(name = Weight, value = "104 `[21-25]`", inline = True)
    Link.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Link)


@client.command(name = "Samus")            #Samus Command: #4
async def Samus(context):
    Samus = discord.Embed(title = "Metroid (1986)", type = "rich", description = "Charge Shot Pressure Exists", color = 0xff9e00)
    Samus.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/03/Samus_SSBU.png")
    Samus.set_author(name = "#4: Samus", url = "https://open.spotify.com/track/1fy1z5EROb7b3tGHgc5fba?si=7589d8a106664bb5", icon_url = "https://ssb.wiki.gallery/images/d/d0/SamusHeadSSBUWebsite.png")
    Samus.add_field(name = RunSpd, value = "1.654 `[50-51]`", inline = True)
    Samus.add_field(name = AirSpd, value = "1.103 `[34-36]`", inline = True)
    Samus.add_field(name = FallSpd, value = "1.33 `[73-74]`", inline = False)
    Samus.add_field(name = Weight, value = "108 `[9-12]`", inline = True)
    Samus.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    Samus.set_footer(text = "Exact same stats and ranks as Dark Samus \nCan: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = Samus)


@client.command(name = "DarkSamus")        #Dark Samus Command: #5
async def DarkSamus(context):
    DSamus = discord.Embed(title = "Metroid Prime (2002)", type = "rich", description = "'Technically' Better than Samus?", color = 0x5100ff)
    DSamus.set_thumbnail(url = "https://ssb.wiki.gallery/images/a/a6/Dark_Samus_SSBU.png")
    DSamus.set_author(name = "#5: Dark Samus", url = "https://open.spotify.com/track/6IyEL4cPFXHWiVbLDdydoi?si=e3c423342fa94046", icon_url = "https://ssb.wiki.gallery/images/2/24/DarkSamusHeadSSBUWebsite.png")
    DSamus.add_field(name = RunSpd, value = "1.654 `[50-51]`", inline = True)
    DSamus.add_field(name = AirSpd, value = "1.103 `[34-36]`", inline = True)
    DSamus.add_field(name = FallSpd, value = "1.33 `[73-74]`", inline = False)
    DSamus.add_field(name = Weight, value = "108 `[9-12]`", inline = True)
    DSamus.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    DSamus.set_footer(text = "Exact same stats and ranks as Samus \nCan: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = DSamus)


@client.command(name = "Yoshi")            #Yoshi Command: #6
async def Yoshi(context):
    Yoshi = discord.Embed(title = "Super Mario World (1990)", type = "rich", description = "Tax Evasion", color = 0x31ff00)
    Yoshi.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/8d/Yoshi_SSBU.png")
    Yoshi.set_author(name = "#6: Yoshi", url = "https://open.spotify.com/track/2aFF05QA8gkXsX7Vv8UamP?si=0144388bea7a4259", icon_url = "https://ssb.wiki.gallery/images/9/93/YoshiHeadSSBUWebsite.png")
    Yoshi.add_field(name = RunSpd, value = "2.046 `[19]`", inline = True)
    Yoshi.add_field(name = AirSpd, value = "1.344 `[1]`", inline = True)
    Yoshi.add_field(name = FallSpd, value = "1.29 `[81]`", inline = False)
    Yoshi.add_field(name = Weight, value = "104 `[21-25]`", inline = True)
    Yoshi.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    Yoshi.set_footer(text = "Fastest air speed in the game")
    await context.message.channel.send(embed = Yoshi)


@client.command(name = "Kirby")            #Kirby Command: #7
async def Kirby(context):
    Kirby = discord.Embed(title = "Kirby's Dream Land (1992)", type = "rich", description = "Neutral B Simps", color = 0xff008e)
    Kirby.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/07/Kirby_SSBU.png")
    Kirby.set_author(name = "#7: Kirby", url = "https://open.spotify.com/track/6yaFVOQLUI9RFTV9YVa6pZ?si=51bd337c18244cf1", icon_url = "https://ssb.wiki.gallery/images/1/15/KirbyHeadSSBUWebsite.png")
    Kirby.add_field(name = RunSpd, value = "1.727 `[42]`", inline = True)
    Kirby.add_field(name = AirSpd, value = "0.84 `[83]`", inline = True)
    Kirby.add_field(name = FallSpd, value = "1.23 `[83]`", inline = False)
    Kirby.add_field(name = Weight, value = "79 `[77-81]`", inline = True)
    Kirby.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    await context.message.channel.send(embed = Kirby)


@client.command(name = "Fox")              #Fox Command: #8
async def Fox(context):
    Fox = discord.Embed(title = "Star Fox (1993)", type = "rich", description = "Dwayne 'Falls Like a Rock' Johnson", color = 0xc3bbc0)
    Fox.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/2f/Fox_SSBU.png")
    Fox.set_author(name = "#8: Fox", url = "https://open.spotify.com/track/22JH2DGnfmUKblTnv6VvdC?si=548ac152f0264363", icon_url = "https://ssb.wiki.gallery/images/c/c9/FoxHeadSSBUWebsite.png")
    Fox.add_field(name = RunSpd, value = "2.402 `[6]`", inline = True)
    Fox.add_field(name = AirSpd, value = "1.11 `[33]`", inline = True)
    Fox.add_field(name = FallSpd, value = "2.1 `[1]`", inline = False)
    Fox.add_field(name = Weight, value = "77 `[83]`", inline = True)
    Fox.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    Fox.set_footer(text = "Can: Wall Jump \nHighest fall speed in the game")
    await context.message.channel.send(embed = Fox)


@client.command(name = "Pikachu")          #Pikachu Command: #9
async def Pikachu(context):
    Pikachu = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "You're Going To Have A Bad Time", color = 0xe9ff00)
    Pikachu.set_thumbnail(url = "https://ssb.wiki.gallery/images/9/93/Pikachu_SSBU.png")
    Pikachu.set_author(name = "#9: Pikachu", url = "https://open.spotify.com/track/1HALda7HkI64vntdlGSa3X?si=ad73a1ab67394bf8", icon_url = "https://ssb.wiki.gallery/images/5/52/PikachuHeadSSBUWebsite.png")
    Pikachu.add_field(name = RunSpd, value = "2.039 `[20]`", inline = True)
    Pikachu.add_field(name = AirSpd, value = "0.957 `[65]`", inline = True)
    Pikachu.add_field(name = FallSpd, value = "1.55 `[52-55]`", inline = False)
    Pikachu.add_field(name = Weight, value = "79 `[77-81]`", inline = True)
    Pikachu.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    Pikachu.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Pikachu)


@client.command(name = "Luigi")            #Luigi Command: #10
async def Luigi(context):
    Luigi = discord.Embed(title = "Mario Bros. (1983)", type = "rich", description = "Discount Waluigi", color = 0x00ff4b)
    Luigi.set_thumbnail(url = "https://ssb.wiki.gallery/images/b/bb/Luigi_SSBU.png")
    Luigi.set_author(name = "#10: Luigi", url = "https://open.spotify.com/track/3sJ4smaOLXnHU4TIgE5xNz?si=eeabf5f43eaa40d7", icon_url = "https://ssb.wiki.gallery/images/9/9d/LuigiHeadSSBUWebsite.png")
    Luigi.add_field(name = RunSpd, value = "1.65 `[52-54]`", inline = True)
    Luigi.add_field(name = AirSpd, value = "0.77 `[86]`", inline = True)
    Luigi.add_field(name = FallSpd, value = "1.32 `[75-76]`", inline = False)
    Luigi.add_field(name = Weight, value = "97 `[36-38]`", inline = True)
    Luigi.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = Luigi)


@client.command(name = "Ness")             #Ness Command: #11
async def Ness(context):
    Ness = discord.Embed(title = "EarthBound (1994)", type = "rich", description = "PK Fire Spam Is Trash", color = 0xff0000)
    Ness.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/82/Ness_SSBU.png")
    Ness.set_author(name = "#11: Ness", url = "https://open.spotify.com/track/3JlK5EtPgo2cykk5BtIJUo?si=9c782a41638a4749", icon_url = "https://ssb.wiki.gallery/images/d/d5/NessHeadSSBUWebsite.png")
    Ness.add_field(name = RunSpd, value = "1.609 `[57]`", inline = True)
    Ness.add_field(name = AirSpd, value = "1.007 `[57]`", inline = True)
    Ness.add_field(name = FallSpd, value = "1.31 `[77]`", inline = False)
    Ness.add_field(name = Weight, value = "94 `[47-50]`", inline = True)
    Ness.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = Ness)


@client.command(name = "Falcon")           #Captain Falcon Command: #12
async def Falcon(context):
    Falcon = discord.Embed(title = "F-Zero (1990)", type = "rich", description = "Falcon Punch", color = 0x0074ff)
    Falcon.set_thumbnail(url = "https://ssb.wiki.gallery/images/d/da/Captain_Falcon_SSBU.png")
    Falcon.set_author(name = "#12: Captain Falcon", url = "https://open.spotify.com/track/6A8OpxPRBP8p4kE3fZEa1Q?si=e94d49541e6b456c", icon_url = "https://ssb.wiki.gallery/images/6/6b/CaptainFalconHeadSSBUWebsite.png")
    Falcon.add_field(name = RunSpd, value = "2.552 `[2]`", inline = True)
    Falcon.add_field(name = AirSpd, value = "1.218 `[12]`", inline = True)
    Falcon.add_field(name = FallSpd, value = "1.865 `[8]`", inline = False)
    Falcon.add_field(name = Weight, value = "104 `[21-25]`", inline = True)
    Falcon.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    Falcon.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Falcon)


@client.command(name = "Puff")             #Jigglypuff Command: #13
async def Puff(context):
    Puff = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "HungryBox", color = 0xf89fff)
    Puff.set_thumbnail(url = "https://ssb.wiki.gallery/images/6/6a/Jigglypuff_SSBU.png")
    Puff.set_author(name = "#13: Jigglypuff", url = "https://open.spotify.com/track/1WPMIgPIBsY0oMhWOTfXXQ?si=ad0090dc8f9b4a72", icon_url = "https://ssb.wiki.gallery/images/9/90/JigglypuffHeadSSBUWebsite.png")
    Puff.add_field(name = RunSpd, value = "1.271 `[85]`", inline = True)
    Puff.add_field(name = AirSpd, value = "1.332 `[2]`", inline = True)
    Puff.add_field(name = FallSpd, value = "0.98 `[87]`", inline = False)
    Puff.add_field(name = Weight, value = "68 `[88]`", inline = True)
    Puff.add_field(name = Weightclass, value = "`Balloonweight`", inline = True)
    Puff.set_footer(text = "Slowest fall speed (floatiest) in the game")
    await context.message.channel.send(embed = Puff)








@client.command(name = 'Peach')            #Peach Command: #14      SECOND ROW STARTS HERE
async def Peach(context):
    Peach = discord.Embed(title = "Super Mario Bros. (1985)", type = "rich", description = "Overrated, Float Cancels Still OP", color = 0xff008b)
    Peach.set_thumbnail(url = "https://ssb.wiki.gallery/images/7/74/Peach_SSBU.png")
    Peach.set_author(name = "#14: Peach", url = "https://open.spotify.com/track/126jlTTSRGaZ5WX8e4Tv7M?si=1de226102cb44eba", icon_url = "https://ssb.wiki.gallery/images/1/14/PeachHeadSSBUWebsite.png")
    Peach.add_field(name = RunSpd, value = "1.595 `[60-64]`", inline = True)
    Peach.add_field(name = AirSpd, value = "1.029 `[48-50]`", inline = True)
    Peach.add_field(name = FallSpd, value = "1.19 `[85-86]`", inline = False)
    Peach.add_field(name = Weight, value = "89 `[63-64]`", inline = True)
    Peach.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    Peach.set_footer(text = "Exact same stats and ranks as Daisy")
    await context.message.channel.send(embed = Peach)


@client.command(name = 'Daisy')            #Daisy Command: #15
async def Daisy(context):
    Daisy = discord.Embed(title = "Super Mario Land (1989)", type = "rich", description = "My Main, Float Cancels OP", color = 0xfca103)
    Daisy.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/21/Daisy_SSBU.png")
    Daisy.set_author(name = "#15: Daisy", url = "https://open.spotify.com/track/63ZMWm1RPYgK6pQbzkK100?si=fc1c1f0b08b448f5", icon_url = "https://ssb.wiki.gallery/images/2/2d/DaisyHeadSSBUWebsite.png")
    Daisy.add_field(name = RunSpd, value = "1.595 `[60-64]`", inline = True)
    Daisy.add_field(name = AirSpd, value = "1.029 `[48-50]`", inline = True)
    Daisy.add_field(name = FallSpd, value = "1.19 `[85-86]`", inline = False)
    Daisy.add_field(name = Weight, value = "89 `[63-64]`", inline = True)
    Daisy.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    Daisy.set_footer(text = "Exact same stats and ranks as Peach")
    await context.message.channel.send(embed = Daisy)


@client.command(name = 'Bowser')           #Bowser Command: #16
async def Bowser(context):
    Bowser = discord.Embed(title = "Super Mario Bros. (1985)", type = "rich", description = "Always Dies 200+ Percent", color = 0xed9600)
    Bowser.set_thumbnail(url = "https://ssb.wiki.gallery/images/4/49/Bowser_SSBU.png")
    Bowser.set_author(name = "#16: Bowser", url = "https://open.spotify.com/track/7C5irIYGVe9xHfJX0Dt5Lf?si=6ea98b3dde0d4fb7", icon_url = "https://ssb.wiki.gallery/images/0/0b/BowserHeadSSBUWebsite.png")
    Bowser.add_field(name = RunSpd, value = "1.971 `[22]`", inline = True)
    Bowser.add_field(name = AirSpd, value = "1.155 `[20-25]`", inline = True)
    Bowser.add_field(name = FallSpd, value = "1.77 `[20-21]`", inline = False)
    Bowser.add_field(name = Weight, value = "135 `[1]`", inline = True)
    Bowser.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    Bowser.set_footer(text = "Heaviest character in the game")
    await context.message.channel.send(embed = Bowser)


@client.command(name = 'Icies')            #Ice Climbers Command: #17
async def Icies(context):
    Icies = discord.Embed(title = "Ice Climber (1985)", type = "rich", description = "Nana Hard Carries", color = 0x2082f0)
    Icies.set_thumbnail(url = "https://ssb.wiki.gallery/images/1/12/Ice_Climbers_SSBU.png")
    Icies.set_author(name = "#17: Ice Climbers", url = "https://open.spotify.com/track/0I29UjYWT3zIjPLqB6h5GV?si=e871653946244d26", icon_url = "https://ssb.wiki.gallery/images/0/0c/IceClimbersHeadSSBUWebsite.png")
    Icies.add_field(name = RunSpd, value = "1.53 `[70]`", inline = True)
    Icies.add_field(name = AirSpd, value = "0.83 `[84-85]`", inline = True)
    Icies.add_field(name = FallSpd, value = "1.3 `[78-80]`", inline = False)
    Icies.add_field(name = Weight, value = "92 `[52-57]`", inline = True)
    Icies.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = Icies)


@client.command(name = 'Sheik')            #Sheik Command: #18
async def Sheik(context):
    Sheik = discord.Embed(title = "The Legend of Zelda: Ocarina of Time (1998)", type = "rich", description = "Gutted From Smash 4", color = 0xb57be2)
    Sheik.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/00/Sheik_SSBU.png")
    Sheik.set_author(name = "#18: Sheik", url = "https://open.spotify.com/track/4OhdW1oEYxLKLsOrznmC0s?si=6ec46041acf44bf7", icon_url = "https://ssb.wiki.gallery/images/1/1e/SheikHeadSSBUWebsite.png")
    Sheik.add_field(name = RunSpd, value = "2.42 `[4]`", inline = True)
    Sheik.add_field(name = AirSpd, value = "1.155 `[20-25]`", inline = True)
    Sheik.add_field(name = FallSpd, value = "1.75 `[24-25]`", inline = False)
    Sheik.add_field(name = Weight, value = "78 `[82]`", inline = True)
    Sheik.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    Sheik.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = Sheik)


@client.command(name = 'Zelda')            #Zelda Command: #19
async def Zelda(context):
    Zelda = discord.Embed(title = "The Legend of Zelda (1986)", type = "rich", description = "Phantom Mechanics", color = 0xdd92ee)
    Zelda.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/c8/Zelda_SSBU.png")
    Zelda.set_author(name = "#19: Zelda", url = "https://open.spotify.com/track/2TlSTYsyVP3ZOEaA81bnBc?si=0444ae37db524ba1", icon_url = "https://ssb.wiki.gallery/images/c/c8/ZeldaHeadSSBUWebsite.png")
    Zelda.add_field(name = RunSpd, value = "1.43 `[78-79]`", inline = True)
    Zelda.add_field(name = AirSpd, value = "1.092 `[39-40]`", inline = True)
    Zelda.add_field(name = FallSpd, value = "1.35 `[69-72]`", inline = False)
    Zelda.add_field(name = Weight, value = "85 `[71]`", inline = True)
    Zelda.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    await context.message.channel.send(embed = Zelda)


@client.command(name = 'Doc')              #Dr. Mario Command: #20
async def Doc(context):
    Doc = discord.Embed(title = "Dr. Mario (1990)", type = "rich", description = "Back Throw Yeets People", color = 0x60979e)
    Doc.set_thumbnail(url = "https://ssb.wiki.gallery/images/3/3f/Dr._Mario_SSBU.png")
    Doc.set_author(name = "#20: Dr. Mario", url = "https://open.spotify.com/track/1zAecnWOvzfFuAEIyUfZs5?si=8e34c9d823a846bd", icon_url = "https://ssb.wiki.gallery/images/c/c8/DrMarioHeadSSBUWebsite.png")
    Doc.add_field(name = RunSpd, value = "1.397792 `[80]`", inline = True)
    Doc.add_field(name = AirSpd, value = "0.9238784 `[76]`", inline = True)
    Doc.add_field(name = FallSpd, value = "1.5 `[57-60]`", inline = False)
    Doc.add_field(name = Weight, value = "98 `[32-35]`", inline = True)
    Doc.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Doc.set_footer(text = "Can: Wall Jump \nI can't believe that those are his actual stats!")
    await context.message.channel.send(embed = Doc)


@client.command(name = 'Pichu')            #Pichu Command: #21
async def Pichu(context):
    Pichu = discord.Embed(title = "Pokemon Gold and Silver (1999)", type = "rich", description = "Dumb Yellow Rat", color = 0xf8ff00)
    Pichu.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/c1/Pichu_SSBU.png")
    Pichu.set_author(name = "#21: Pichu", url = "https://open.spotify.com/track/0Qaavj6icd6p3BAnwGEtG9?si=63f8b729549548cd", icon_url = "https://ssb.wiki.gallery/images/5/50/PichuHeadSSBUWebsite.png")
    Pichu.add_field(name = RunSpd, value = "1.892 `[28]`", inline = True)
    Pichu.add_field(name = AirSpd, value = "1.029 `[48-50]`", inline = True)
    Pichu.add_field(name = FallSpd, value = "1.9 `[6]`", inline = False)
    Pichu.add_field(name = Weight, value = "62 `[87]`", inline = True)
    Pichu.add_field(name = Weightclass, value = "`Balloonweight`", inline = True)
    Pichu.set_footer(text = "Can: Wall Jump \nLightest character in the game")
    await context.message.channel.send(embed = Pichu)


@client.command(name = 'Falco')            #Falco Command: #22
async def Falco(context):
    Falco = discord.Embed(title = "Star Fox (1993)", type = "rich", description = "That Ain't Falco", color = 0x0074ff)
    Falco.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/80/Falco_SSBU.png")
    Falco.set_author(name = "#22: Falco", url = "https://open.spotify.com/track/3ME5GLvAN1FroRF4qFNXjW?si=7c5b0dfdb9b847a1", icon_url = "https://ssb.wiki.gallery/images/6/6e/FalcoHeadSSBUWebsite.png")
    Falco.add_field(name = RunSpd, value = "1.619 `[55]`", inline = True)
    Falco.add_field(name = AirSpd, value = "0.977 `[63]`", inline = True)
    Falco.add_field(name = FallSpd, value = "1.8 `[13-18]`", inline = False)
    Falco.add_field(name = Weight, value = "82 `[72-73]`", inline = True)
    Falco.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    Falco.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Falco)


@client.command(name = 'Marth')            #Marth Command: #23
async def Marth(context):
    Marth = discord.Embed(title = "Fire Emblem: Shadow Dragon and the Blade of Light (1990)", type = "rich", description = "Just The Tip", color = 0x0074ff)
    Marth.set_thumbnail(url = "https://ssb.wiki.gallery/images/e/e9/Marth_SSBU.png")
    Marth.set_author(name = "#23: Marth", url = "https://open.spotify.com/track/2Cn5v5xb9WqnxqPrEFwUjS?si=475aa9eb4b4b4256", icon_url = "https://ssb.wiki.gallery/images/a/ae/MarthHeadSSBUWebsite.png")
    Marth.add_field(name = RunSpd, value = "1.964 `[23-24]`", inline = True)
    Marth.add_field(name = AirSpd, value = "1.071 `[41-42]`", inline = True)
    Marth.add_field(name = FallSpd, value = "1.58 `[47-50]`", inline = False)
    Marth.add_field(name = Weight, value = "90 `[60-62]`", inline = True)
    Marth.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Marth.set_footer(text = "Exact same stats and rank as Lucina \nOnly difference: Tip of the sword is stronger")
    await context.message.channel.send(embed = Marth)


@client.command(name = 'Lucina')           #Lucina Command: #24
async def Lucina(context):
    Lucina = discord.Embed(title = "Fire Emblem Awakening (2012)", type = "rich", description = "Real Marth, Too Safe", color = 0x0152b3)
    Lucina.set_thumbnail(url = "https://ssb.wiki.gallery/images/d/dc/Lucina_SSBU.png")
    Lucina.set_author(name = "#24: Lucina", url = "https://open.spotify.com/track/1EV465Il8JJQlwJQQmXCn6?si=dd845cd0c7154354", icon_url = "https://ssb.wiki.gallery/images/d/d8/LucinaHeadSSBUWebsite.png")
    Lucina.add_field(name = RunSpd, value = "1.964 `[23-24]`", inline = True)
    Lucina.add_field(name = AirSpd, value = "1.071 `[41-42]`", inline = True)
    Lucina.add_field(name = FallSpd, value = "1.58 `[47-50]`", inline = False)
    Lucina.add_field(name = Weight, value = "90 `[60-62]`", inline = True)
    Lucina.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Lucina.set_footer(text = "Exact same stats and rank as Marth \nOnly difference: All parts of the sword are strong")
    await context.message.channel.send(embed = Lucina)


@client.command(name = 'YoungLink')        #Young Link Command: #25
async def YoungLink(context):
    YLink = discord.Embed(title = "The Legend of Zelda: Ocarina of Time (1998)", type = "rich", description = "The Most Annoying Link", color = 0x00ff4b)
    YLink.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/8a/Young_Link_SSBU.png")
    YLink.set_author(name = "#25: Young Link", url = "https://open.spotify.com/track/4eA9VHcNALbJh4cLcCWHWs?si=a3901eab68d54ee2", icon_url = "https://ssb.wiki.gallery/images/c/c0/YoungLinkHeadSSBUWebsite.png")
    YLink.add_field(name = RunSpd, value = "1.749 `[41]`", inline = True)
    YLink.add_field(name = AirSpd, value = "0.966 `[64]`", inline = True)
    YLink.add_field(name = FallSpd, value = "1.8 `[13-18]`", inline = False)
    YLink.add_field(name = Weight, value = "88 `[65-67]`", inline = True)
    YLink.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    YLink.set_footer(text = "Can: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = YLink)


@client.command(name = 'Ganon')        #Ganondorf Command: #26
async def Ganon(context):
    Ganon = discord.Embed(title = "The Legend of Zelda: Ocarina of Time (1998)", type = "rich", description = "The King of Disrespect", color = 0x5400b8)
    Ganon.set_thumbnail(url = "https://ssb.wiki.gallery/images/9/91/Ganondorf_SSBU.png")
    Ganon.set_author(name = "#26: Ganondorf", url = "https://open.spotify.com/track/7kWqgvTLq4pb5nGqtwJREJ?si=ebd635b0f04445e5", icon_url = "https://ssb.wiki.gallery/images/b/b6/GanondorfHeadSSBUWebsite.png")
    Ganon.add_field(name = RunSpd, value = "1.34 `[84]`", inline = True)
    Ganon.add_field(name = AirSpd, value = "0.83 `[84-85]`", inline = True)
    Ganon.add_field(name = FallSpd, value = "1.65 `[32-37]`", inline = False)
    Ganon.add_field(name = Weight, value = "118 `[5]`", inline = True)
    Ganon.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    await context.message.channel.send(embed = Ganon)








@client.command(name = 'Mewtwo')           #Mewtwo Command: #27     THIRD ROW STARTS HERE
async def Mewtwo(context):
    Mew = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "Hitbox Includes Tail", color = 0x9252df)
    Mew.set_thumbnail(url = "https://ssb.wiki.gallery/images/d/de/Mewtwo_SSBU.png")
    Mew.set_author(name = "#27: Mewtwo", url = "https://open.spotify.com/track/0zjEZTXsL4vMTMffx2gHdT?si=4103581b7747481a", icon_url = "https://ssb.wiki.gallery/images/7/7e/MewtwoHeadSSBUWebsite.png")
    Mew.add_field(name = RunSpd, value = "2.255 `[9]`", inline = True)
    Mew.add_field(name = AirSpd, value = "1.313 `[3]`", inline = True)
    Mew.add_field(name = FallSpd, value = "1.55 `[52-55]`", inline = False)
    Mew.add_field(name = Weight, value = "79 `[77-81]`", inline = True)
    Mew.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    Mew.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Mew)


@client.command(name = 'Roy')              #Roy Command: #28
async def Roy(context):
    Roy = discord.Embed(title = "Super Smash Bros. Melee (2001)", type = "rich", description = "It's Our Boy", color = 0xfe3c00)
    Roy.set_thumbnail(url = "https://ssb.wiki.gallery/images/9/9d/Roy_SSBU.png")
    Roy.set_author(name = "#28: Roy", url = "https://open.spotify.com/track/6ULjiHPx9dy3Ec3C3gjI4z?si=3deda948ed0e4784", icon_url = "https://ssb.wiki.gallery/images/2/22/RoyHeadSSBUWebsite.png")
    Roy.add_field(name = RunSpd, value = "2.145 `[14-15]`", inline = True)
    Roy.add_field(name = AirSpd, value = "1.302 `[4-5]`", inline = True)
    Roy.add_field(name = FallSpd, value = "1.8 `[13-18]`", inline = False)
    Roy.add_field(name = Weight, value = "95 `[43-46]`", inline = True)
    Roy.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Roy.set_footer(text = "Exact same stats and ranks as Chrom \nOnly difference: Inside of the sword is strong")
    await context.message.channel.send(embed = Roy)


@client.command(name = 'Chrom')            #Chrom Command: #29 
async def Chrom(context):
    Chrom = discord.Embed(title = "Fire Emblem Awawkening (2012)", type = "rich", description = "Google Chrome", color = 0x507bcb)
    Chrom.set_thumbnail(url = "https://ssb.wiki.gallery/images/5/57/Chrom_SSBU.png")
    Chrom.set_author(name = "#29: Chrom", url = "https://open.spotify.com/track/7GUdZH0lYiOlfBsWrhMwHp?si=d99653e97e9d4df5", icon_url = "https://ssb.wiki.gallery/images/7/70/ChromHeadSSBUWebsite.png")
    Chrom.add_field(name = RunSpd, value = "2.145 `[14-15]`", inline = True)
    Chrom.add_field(name = AirSpd, value = "1.302 `[4-5]`", inline = True)
    Chrom.add_field(name = FallSpd, value = "1.8 `[13-18]`", inline = False)
    Chrom.add_field(name = Weight, value = "95 `[43-46]`", inline = True)
    Chrom.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Chrom.set_footer(text = "Exact same stats and ranks as Roy \nOnly difference: All parts of the sword are strong")
    await context.message.channel.send(embed = Chrom)


@client.command(name = 'GnW')              #Mr. Game & Watch Command: #30 
async def GnW(context):
    GnW = discord.Embed(title = "Ball (1980)", type = "rich", description = "Judgement 9 = Skill", color = 0x000000)
    GnW.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/cb/Mr._Game_%26_Watch_SSBU.png")
    GnW.set_author(name = "#30: Mr. Game & Watch", url = "https://open.spotify.com/track/5MkWm3BoOIe4rXXQenM8Kw?si=9f821866898e4119", icon_url = "https://ssb.wiki.gallery/images/1/15/MrGame%26WatchHeadSSBUWebsite.png")
    GnW.add_field(name = RunSpd, value = "1.679 `[47]`", inline = True)
    GnW.add_field(name = AirSpd, value = "1.176 `[18]`", inline = True)
    GnW.add_field(name = FallSpd, value = "1.24 `[82]`", inline = False)
    GnW.add_field(name = Weight, value = "75 `[84-85]`", inline = True)
    GnW.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    await context.message.channel.send(embed = GnW)


@client.command(name = 'MK')               #Meta Knight Command: #31 
async def MetaKnight(context):
    Meta = discord.Embed(title = "Kirby's Adventure (1993)", type = "rich", description = "Every Special Is A Recovery", color = 0x5f3ed4)
    Meta.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/00/Meta_Knight_SSBU.png")
    Meta.set_author(name = "#31: Meta Knight", url = "https://open.spotify.com/track/1ROnBLZnitJpZOnzD4wiAe?si=0d881b7da2104d49", icon_url = "https://ssb.wiki.gallery/images/3/3d/MetaKnightHeadSSBUWebsite.png")
    Meta.add_field(name = RunSpd, value = "2.09 `[16]`", inline = True)
    Meta.add_field(name = AirSpd, value = "1.04 `[47]`", inline = True)
    Meta.add_field(name = FallSpd, value = "1.66 `[31]`", inline = False)
    Meta.add_field(name = Weight, value = "80 `[75-76]`", inline = True)
    Meta.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    await context.message.channel.send(embed = Meta)


@client.command(name = 'Pit')              #Pit Command: #32 
async def Pit(context):
    Pit = discord.Embed(title = "Kid Icarus (1986)", type = "rich", description = "Can't Read", color = 0xdcd6ef)
    Pit.set_thumbnail(url = "https://ssb.wiki.gallery/images/3/38/Pit_SSBU.png")
    Pit.set_author(name = "#32: Pit", url = "https://open.spotify.com/track/7HIb4JqJTon9MH8CcEBYE1?si=f410a2607d9a446c", icon_url = "https://ssb.wiki.gallery/images/d/d7/PitHeadSSBUWebsite.png")
    Pit.add_field(name = RunSpd, value = "1.828 `[32-33]`", inline = True)
    Pit.add_field(name = AirSpd, value = "0.935 `[71-72]`", inline = True)
    Pit.add_field(name = FallSpd, value = "1.48 `[61-63]`", inline = False)
    Pit.add_field(name = Weight, value = "96 `[39-42]`", inline = True)
    Pit.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Pit.set_footer(text = "Exact same stats and ranks as Dark Pit \nDifferences: Arrows(Less Damage & Can Be Curved) and Side B(Launches Upwards)")
    await context.message.channel.send(embed = Pit)


@client.command(name = 'DarkPit')          #Dark Pit Command: #33 
async def DarkPit(context):
    DPit = discord.Embed(title = "Kid Icarus (1986)", type = "rich", description = "Can't Read", color = 0x361e41)
    DPit.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/09/Dark_Pit_SSBU.png")
    DPit.set_author(name = "#33: Dark Pit", url = "https://open.spotify.com/track/1Nv8YeKrXdR7max6eeZ3SC?si=0b339fa96e8c4e0a", icon_url = "https://ssb.wiki.gallery/images/8/8b/DarkPitHeadSSBUWebsite.png")
    DPit.add_field(name = RunSpd, value = "1.828 `[32-33]`", inline = True)
    DPit.add_field(name = AirSpd, value = "0.935 `[71-72]`", inline = True)
    DPit.add_field(name = FallSpd, value = "1.48 `[61-63]`", inline = False)
    DPit.add_field(name = Weight, value = "96 `[39-42]`", inline = True)
    DPit.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    DPit.set_footer(text = "Exact same stats and ranks as Pit \nDifferences: Arrows(More Damage & Can't Be Curved) and Side B(Launches Horizontally)")
    await context.message.channel.send(embed = DPit)


@client.command(name = 'ZSS')              #Zero Suit Samus Command: #34 
async def ZSS(context):
    ZSS = discord.Embed(title = "Metroid: Zero Mission (2004)", type = "rich", description = "Cammy In Disguise", color = 0x1699ef)
    ZSS.set_thumbnail(url = "https://ssb.wiki.gallery/images/f/f0/Zero_Suit_Samus_SSBU.png")
    ZSS.set_author(name = "#34: Zero Suit Samus", url = "https://open.spotify.com/track/0SXJaYvoMCidaNUAnoAv1K?si=1f2a9553b7e242dc", icon_url = "https://ssb.wiki.gallery/images/5/5a/ZeroSuitSamusHeadSSBUWebsite.png")
    ZSS.add_field(name = RunSpd, value = "2.31 `[7]`", inline = True)
    ZSS.add_field(name = AirSpd, value = "1.26 `[9]`", inline = True)
    ZSS.add_field(name = FallSpd, value = "1.7 `[27-28]`", inline = False)
    ZSS.add_field(name = Weight, value = "80 `[75-76]`", inline = True)
    ZSS.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    ZSS.set_footer(text = "Can: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = ZSS)


@client.command(name = 'Wario')            #Wario Command: #35 
async def Wario(context):
    Wario = discord.Embed(title = "Super Mario Land 2: 6 Golden Coins (1992)", type = "rich", description = "Degen Reddit Mod", color = 0xdfd31f)
    Wario.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/04/Wario_SSBU.png")
    Wario.set_author(name = "#35: Wario", url = "https://open.spotify.com/track/1VeBDwRuEqDNBORurkmzYs?si=4e33b071358e44cd", icon_url = "https://ssb.wiki.gallery/images/7/7f/WarioHeadSSBUWebsite.png")
    Wario.add_field(name = RunSpd, value = "1.65 `[52-54]`", inline = True)
    Wario.add_field(name = AirSpd, value = "1.271 `[8]`", inline = True)
    Wario.add_field(name = FallSpd, value = "1.61 `[41]`", inline = False)
    Wario.add_field(name = Weight, value = "107 `[13-17]`", inline = True)
    Wario.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Wario)


@client.command(name = 'Snake')            #Snake Command: #36 
async def Snake(context):
    Snake = discord.Embed(title = "Metal Gear (1987)", type = "rich", description = "Manliest Character In The Game" , color = 0x597c8c)
    Snake.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/02/Snake_SSBU.png")
    Snake.set_author(name = "#36: Snake", url = "https://open.spotify.com/track/6LD1Xsy4pZcljgjdqwJQTT?si=a5b5b3a1445244b5", icon_url = "https://ssb.wiki.gallery/images/9/9f/SnakeHeadSSBUWebsite.png")
    Snake.add_field(name = RunSpd, value = "1.595 `[60-64]`", inline = True)
    Snake.add_field(name = AirSpd, value = "0.987 `[61-62]`", inline = True)
    Snake.add_field(name = FallSpd, value = "1.73 `[26]`", inline = False)
    Snake.add_field(name = Weight, value = "106 `[18-20]`", inline = True)
    Snake.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Snake)


@client.command(name = 'Ike')              #Ike Command: #37 
async def Ike(context):
    Ike = discord.Embed(title = "Fire Emblem: Path of Radiance (2005)", type = "rich", description = "He Fights For His Friends" , color = 0xd8512e)
    Ike.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/86/Ike_SSBU.png")
    Ike.set_author(name = "#37: Ike", url = "https://open.spotify.com/track/0RbeHcWAC742U1RVH66B93?si=a0f594946d2c4a75", icon_url = "https://ssb.wiki.gallery/images/2/25/IkeHeadSSBUWebsite.png")
    Ike.add_field(name = RunSpd, value = "1.507 `[73]`", inline = True)
    Ike.add_field(name = AirSpd, value = "1.134 `[27-29]`", inline = True)
    Ike.add_field(name = FallSpd, value = "1.65 `[32-37]`", inline = False)
    Ike.add_field(name = Weight, value = "107 `[13-17]`", inline = True)
    Ike.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Ike)


@client.command(name = 'Squirtle')         #Squirtle Command: #38 
async def Squirtle(context):
    Squirtle = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "Best Kanto Starter?" , color = 0x00eaff)
    Squirtle.set_thumbnail(url = "https://ssb.wiki.gallery/images/7/79/Squirtle_SSBU.png")
    Squirtle.set_author(name = "#38: Squirtle", url = "https://open.spotify.com/track/2MJzgL1j77ytyPeQopJzvq?si=61fd84b80f404b9a", icon_url = "https://ssb.wiki.gallery/images/4/40/SquirtleHeadSSBU.png")
    Squirtle.add_field(name = RunSpd, value = "1.76 `[37-40]`", inline = True)
    Squirtle.add_field(name = AirSpd, value = "1.01 `[55-56]`", inline = True)
    Squirtle.add_field(name = FallSpd, value = "1.35 `[69-72]`", inline = False)
    Squirtle.add_field(name = Weight, value = "75 `[84-85]`", inline = True)
    Squirtle.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    Squirtle.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = Squirtle)


@client.command(name = 'Ivysaur')          #Ivysaur Command: #39 
async def Ivysaur(context):
    Ivysaur = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "Legit Broken Hitboxes" , color = 0x0bf212)
    Ivysaur.set_thumbnail(url = "https://ssb.wiki.gallery/images/5/52/Ivysaur_SSBU.png")
    Ivysaur.set_author(name = "#39: Ivysaur", url = "https://open.spotify.com/track/3DwJdDoj2z26wLwqinGWbm?si=f3194e240d574a05", icon_url = "https://ssb.wiki.gallery/images/b/b4/IvysaurHeadSSBU.png")
    Ivysaur.add_field(name = RunSpd, value = "1.595 `[60-64]`", inline = True)
    Ivysaur.add_field(name = AirSpd, value = "0.998 `[60]`", inline = True)
    Ivysaur.add_field(name = FallSpd, value = "1.38 `[66-67]`", inline = False)
    Ivysaur.add_field(name = Weight, value = "96 `[39-42]`", inline = True)
    Ivysaur.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Ivysaur.set_footer(text = "Can: Tether Recovery")
    await context.message.channel.send(embed = Ivysaur)


@client.command(name = 'Charizard')        #Charizard Command: #40 
async def Charizard(context):
    Charizard = discord.Embed(title = "Pokemon Red and Green (1996)", type = "rich", description = "2nd Most Overrated Pokemon Of All Time" , color = 0xff5b00)
    Charizard.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/21/Charizard_SSBU.png")
    Charizard.set_author(name = "#40: Charizard", url = "https://open.spotify.com/track/31ZjAWmN33w98gbGcBphBR?si=4f6daa5ffbb14b52", icon_url = "https://ssb.wiki.gallery/images/c/c9/CharizardHeadSSBU.png")
    Charizard.add_field(name = RunSpd, value = "2.2 `[10-11]`", inline = True)
    Charizard.add_field(name = AirSpd, value = "1.103 `[34-36]`", inline = True)
    Charizard.add_field(name = FallSpd, value = "1.52 `[56]`", inline = False)
    Charizard.add_field(name = Weight, value = "116 `[6-7]`", inline = True)
    Charizard.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    await context.message.channel.send(embed = Charizard)


@client.command(name = 'Diddy')            #Diddy Kong Command: #41 
async def Diddy(context):
    Diddy = discord.Embed(title = "Donkey Kong Country (1994)", type = "rich", description = "Small Dong" , color = 0xbe6d41)
    Diddy.set_thumbnail(url = "https://ssb.wiki.gallery/images/a/a7/Diddy_Kong_SSBU.png")
    Diddy.set_author(name = "#41: Diddy Kong", url = "https://open.spotify.com/track/5D8KCS9aMIAoiTXfu1KGaU?si=626b7573cb5c41aa", icon_url = "https://ssb.wiki.gallery/images/5/5d/DiddyKongHeadSSBUWebsite.png")
    Diddy.add_field(name = RunSpd, value = "2.006 `[21]`", inline = True)
    Diddy.add_field(name = AirSpd, value = "0.924 `[74-75]`", inline = True)
    Diddy.add_field(name = FallSpd, value = "1.75 `[24-25]`", inline = False)
    Diddy.add_field(name = Weight, value = "90 `[60-62]`", inline = True)
    Diddy.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Diddy.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = Diddy)







@client.command(name = 'Lucas')            #Lucas Command: #42      FOURTH ROW STARTS HERE
async def Lucas(context):
    Lucas = discord.Embed(title = "Mother 3 (2006)", type = "rich", description = "Literally Came Out Of Nowhere" , color = 0xd6e040)
    Lucas.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/81/Lucas_SSBU.png")
    Lucas.set_author(name = "#42: Lucas", url = "https://open.spotify.com/track/7AbL6K0dECbyDgZ0Sjs1yA?si=c9fc7857311243c1", icon_url = "https://ssb.wiki.gallery/images/3/31/LucasHeadSSBUWebsite.png")
    Lucas.add_field(name = RunSpd, value = "1.65 `[52-54]`", inline = True)
    Lucas.add_field(name = AirSpd, value = "1.155 `[20-25]`", inline = True)
    Lucas.add_field(name = FallSpd, value = "1.37 `[68]`", inline = False)
    Lucas.add_field(name = Weight, value = "94 `[47-50]`", inline = True)
    Lucas.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Lucas.set_footer(text = "Can: Tether Recovery")
    await context.message.channel.send(embed = Lucas)


@client.command(name = 'Sonic')            #Sonic Command: #43      
async def Sonic(context):
    Sonic = discord.Embed(title = "Sonic The Hedgehog (1991)", type = "rich", description = "Sonic '06 Speaks For Itself" , color = 0x006dff)
    Sonic.set_thumbnail(url = "https://ssb.wiki.gallery/images/b/ba/Sonic_SSBU.png")
    Sonic.set_author(name = "#43: Sonic", url = "https://open.spotify.com/track/4BRWDjTnycZMZMkKV6jbSY?si=19ed93cedfa04d85", icon_url = "https://ssb.wiki.gallery/images/b/b7/SonicHeadSSBUWebsite.png")
    Sonic.add_field(name = RunSpd, value = "3.85 `[1]`", inline = True)
    Sonic.add_field(name = AirSpd, value = "1.208 `[13-17]`", inline = True)
    Sonic.add_field(name = FallSpd, value = "1.65 `[32-37]`", inline = False)
    Sonic.add_field(name = Weight, value = "86 `[69-70]`", inline = True)
    Sonic.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    Sonic.set_footer(text = "Can: Wall Jump \nFastest run speed in the game")
    await context.message.channel.send(embed = Sonic)


@client.command(name = 'DDD')              #King Dedede Command: #44      
async def DDD(context):
    DDD = discord.Embed(title = "Kirby's Dreamland (1992)", type = "rich", description = "Crouch Is A Meme" , color = 0xffc600)
    DDD.set_thumbnail(url = "https://ssb.wiki.gallery/images/f/f5/King_Dedede_SSBU.png")
    DDD.set_author(name = "#44: King Dedede", url = "https://open.spotify.com/track/2BCkI5vkyvOdfYcLKIlfyr?si=b3abcb69279d4533", icon_url = "https://ssb.wiki.gallery/images/f/fe/KingDededeHeadSSBUWebsite.png")
    DDD.add_field(name = RunSpd, value = "1.496 `[74]`", inline = True)
    DDD.add_field(name = AirSpd, value = "0.735 `[87]`", inline = True)
    DDD.add_field(name = FallSpd, value = "1.95 `[2-4]`", inline = False)
    DDD.add_field(name = Weight, value = "127 `[3-4]`", inline = True)
    DDD.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    DDD.set_footer(text = "Slowest air speed in the game")
    await context.message.channel.send(embed = DDD)


@client.command(name = 'Olimar')           #Olimar Command: #45      
async def Olimar(context):
    Olimar = discord.Embed(title = "Pikmin (2001)", type = "rich", description = "Too Many Disjoints" , color = 0xbcc570)
    Olimar.set_thumbnail(url = "https://ssb.wiki.gallery/images/b/b3/Olimar_SSBU.png")
    Olimar.set_author(name = "#45: Olimar", url = "https://open.spotify.com/track/1fedeOT7omu0QGz6Hr6CqE?si=43519620387543f4", icon_url = "https://ssb.wiki.gallery/images/9/97/OlimarHeadSSBUWebsite.png")
    Olimar.add_field(name = RunSpd, value = "1.617 `[56]`", inline = True)
    Olimar.add_field(name = AirSpd, value = "0.861 `[80]`", inline = True)
    Olimar.add_field(name = FallSpd, value = "1.35 `[69-72]`", inline = False)
    Olimar.add_field(name = Weight, value = "79 `[77-81]`", inline = True)
    Olimar.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    await context.message.channel.send(embed = Olimar)


@client.command(name = 'Lucario')          #Lucario Command: #46      
async def Lucario(context):
    Lucario = discord.Embed(title = "Pokemon Diamond and Pearl (2006)", type = "rich", description = "Sinnoh Best Region" , color = 0x3a5786)
    Lucario.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/08/Lucario_SSBU.png")
    Lucario.set_author(name = "#46: Lucario", url = "https://open.spotify.com/track/02NdDkU7wD1pjoy5u9kT7X?si=a748371951454986", icon_url = "https://ssb.wiki.gallery/images/2/20/LucarioHeadSSBUWebsite.png")
    Lucario.add_field(name = RunSpd, value = "1.705 `[46]`", inline = True)
    Lucario.add_field(name = AirSpd, value = "1.281 `[6-7]`", inline = True)
    Lucario.add_field(name = FallSpd, value = "1.68 `[29-30]`", inline = False)
    Lucario.add_field(name = Weight, value = "92 `[52-57]`", inline = True)
    Lucario.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Lucario.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = Lucario)


@client.command(name = 'Rob')              #ROB Command: #47      
async def Rob(context):
    Rob = discord.Embed(title = "Stack-Up (1985)", type = "rich", description = "Not Even A Character" , color = 0x94a5c1)
    Rob.set_thumbnail(url = "https://ssb.wiki.gallery/images/6/60/R.O.B._SSBU.png")
    Rob.set_author(name = "#47: R.O.B", url = "https://open.spotify.com/track/3iTHPIRqTgXgjUrfXIYIn1?si=1c3a56fa8b9f4fca", icon_url = "https://ssb.wiki.gallery/images/b/be/ROBHeadSSBUWebsite.png")
    Rob.add_field(name = RunSpd, value = "1.725 `[43]`", inline = True)
    Rob.add_field(name = AirSpd, value = "1.134 `[27-29]`", inline = True)
    Rob.add_field(name = FallSpd, value = "1.6 `[42-46]`", inline = False)
    Rob.add_field(name = Weight, value = "106 `[18-20]`", inline = True)
    Rob.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Rob)


@client.command(name = 'ToonLink')         #Toon Link Command: #48      
async def toonlink(context):
    tlink = discord.Embed(title = "The Legend of Zelda: Four Swords (2002)", type = "rich", description = "The Worst Link" , color = 0x0fed6c)
    tlink.set_thumbnail(url = "https://ssb.wiki.gallery/images/5/56/Toon_Link_SSBU.png")
    tlink.set_author(name = "#48: Toon Link", url = "https://open.spotify.com/track/565IoIuSM389HhAp8U69qf?si=0ac09e60d01e480c", icon_url = "https://ssb.wiki.gallery/images/b/bf/ToonLinkHeadSSBUWebsite.png")
    tlink.add_field(name = RunSpd, value = "1.906 `[27]`", inline = True)
    tlink.add_field(name = AirSpd, value = "1.05 `[43-46]`", inline = True)
    tlink.add_field(name = FallSpd, value = "1.38 `[66-67]`", inline = False)
    tlink.add_field(name = Weight, value = "91 `[58-59]`", inline = True)
    tlink.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    tlink.set_footer(text = "Can: Wall Jump, Tether Recovery")
    await context.message.channel.send(embed = tlink)


@client.command(name = 'Wolf')             #Wolf Command: #49      
async def Wolf(context):
    Wolf = discord.Embed(title = "Star Fox 64 (1997)", type = "rich", description = "Blaster Spam Is Cursed" , color = 0x7b1abd)
    Wolf.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/8a/Wolf_SSBU.png")
    Wolf.set_author(name = "#49: Wolf", url = "https://open.spotify.com/track/24Hub6h8LGBfn0mcPFn2wx?si=db92a6f9fc5c4df6", icon_url = "https://ssb.wiki.gallery/images/0/06/WolfHeadSSBUWebsite.png")
    Wolf.add_field(name = RunSpd, value = "1.54 `[68]`", inline = True)
    Wolf.add_field(name = AirSpd, value = "1.281 `[6-7]`", inline = True)
    Wolf.add_field(name = FallSpd, value = "1.8 `[13-18]`", inline = False)
    Wolf.add_field(name = Weight, value = "92 `[52-57]`", inline = True)
    Wolf.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Wolf.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Wolf)


@client.command(name = 'Villager')         #Villager Command: #50      
async def Villager(context):
    Vill = discord.Embed(title = "Doubutsu no Mori (2001)", type = "rich", description = "That's A Murder Face" , color = 0xd05757)
    Vill.set_thumbnail(url = "https://ssb.wiki.gallery/images/a/ac/Villager_SSBU.png")
    Vill.set_author(name = "#50: Villager", url = "https://open.spotify.com/track/5fegEkQy2FKJfqOKTrnTLW?si=3977e37231264665", icon_url = "https://ssb.wiki.gallery/images/f/f9/VillagerHeadSSBUWebsite.png")
    Vill.add_field(name = RunSpd, value = "1.397 `[81]`", inline = True)
    Vill.add_field(name = AirSpd, value = "0.987 `[61-62]`", inline = True)
    Vill.add_field(name = FallSpd, value = "1.32 `[75-76]`", inline = False)
    Vill.add_field(name = Weight, value = "92 `[52-57]`", inline = True)
    Vill.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Vill.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Vill)


@client.command(name = 'Megaman')         #Megaman Command: #51      
async def Megaman(context):
    Mega = discord.Embed(title = "Mega Man (1987)", type = "rich", description = "Super Fighting Robot" , color = 0x00a7ff)
    Mega.set_thumbnail(url = "https://ssb.wiki.gallery/images/4/46/Mega_Man_SSBU.png")
    Mega.set_author(name = "#51: Megaman", url = "https://open.spotify.com/track/6iKu0q1ix7YogUSe4oNN30?si=d8a469a572a948a0", icon_url = "https://ssb.wiki.gallery/images/2/26/MegaManHeadSSBUWebsite.png")
    Mega.add_field(name = RunSpd, value = "1.602 `[58]`", inline = True)
    Mega.add_field(name = AirSpd, value = "1.155 `[20-25]`", inline = True)
    Mega.add_field(name = FallSpd, value = "1.8 `[13-18]`", inline = False)
    Mega.add_field(name = Weight, value = "102 `[28]`", inline = True)
    Mega.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    Mega.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Mega)


@client.command(name = 'WiiFit')           #Wii Fit Trainer Command: #52      
async def WiiFit(context):
    Wii = discord.Embed(title = "Wii Fit (2007)", type = "rich", description = "Meme Character" , color = 0x00a7ff)
    Wii.set_thumbnail(url = "https://ssb.wiki.gallery/images/f/ff/Wii_Fit_Trainer_SSBU.png")
    Wii.set_author(name = "#52: Wii Fit Trainer", url = "https://open.spotify.com/track/4GLcSCuaUEZ9NmuROdIl9d?si=b02bf8735bdd4b62", icon_url = "https://ssb.wiki.gallery/images/f/fc/WiiFitTrainerHeadSSBUWebsite.png")
    Wii.add_field(name = RunSpd, value = "1.866 `[30]`", inline = True)
    Wii.add_field(name = AirSpd, value = "1.019 `[52-54]`", inline = True)
    Wii.add_field(name = FallSpd, value = "1.3 `[78-80]`", inline = False)
    Wii.add_field(name = Weight, value = "96 `[39-42]`", inline = True)
    Wii.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Wii.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Wii)


@client.command(name = 'Rosa')             #Rosalina & Luma Command: #53      
async def Rosa(context):
    Rosa = discord.Embed(title = "Super Mario Galaxy (2007)", type = "rich", description = "Luma's Cracked" , color = 0x00a7ff)
    Rosa.set_thumbnail(url = "https://ssb.wiki.gallery/images/1/16/Rosalina_%26_Luma_SSBU.png")
    Rosa.set_author(name = "#53: Rosalina & Luma", url = "https://open.spotify.com/track/7ptzEZfGLMLUhhgfw5ZsoT?si=952d593d22654cc2", icon_url = "https://ssb.wiki.gallery/images/6/63/RosalinaHeadSSBUWebsite.png")
    Rosa.add_field(name = RunSpd, value = "1.795 `[35]`", inline = True)
    Rosa.add_field(name = AirSpd, value = "1.05 `[43-46]`", inline = True)
    Rosa.add_field(name = FallSpd, value = "1.2 `[84]`", inline = False)
    Rosa.add_field(name = Weight, value = "82 `[72-73]`", inline = True)
    Rosa.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    await context.message.channel.send(embed = Rosa)


@client.command(name = 'Mac')              #Little Mac Command: #54      
async def Mac(context):
    Mac = discord.Embed(title = "Punch-Out!! (1987)", type = "rich", description = "Air Game 10/10" , color = 0x2aa96e)
    Mac.set_thumbnail(url = "https://ssb.wiki.gallery/images/5/53/Little_Mac_SSBU.png")
    Mac.set_author(name = "#54: Little Mac", url = "https://open.spotify.com/track/0FR1i0jsRol6lNDsI8wYbd?si=b9bd22989b1d4c6e", icon_url = "https://ssb.wiki.gallery/images/8/87/LittleMacHeadSSBUWebsite.png")
    Mac.add_field(name = RunSpd, value = "2.464 `[3]`", inline = True)
    Mac.add_field(name = AirSpd, value = "1.208 `[13-17]`", inline = True)
    Mac.add_field(name = FallSpd, value = "1.95 `[2-4]`", inline = False)
    Mac.add_field(name = Weight, value = "87 `[68]`", inline = True)
    Mac.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    Mac.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Mac)







@client.command(name = 'Greninja')         #Greninja Command: #55       FIFTH ROW STARTS HERE
async def Greninja(context):
    Greninja = discord.Embed(title = "Pokemon X and Y (2013)", type = "rich", description = "I've Met Elu Tran" , color = 0x089ffd)
    Greninja.set_thumbnail(url = "https://ssb.wiki.gallery/images/d/da/Greninja_SSBU.png")
    Greninja.set_author(name = "#55: Greninja", url = "https://open.spotify.com/track/3RZL40u2LHNb0uOAVUV0R9?si=d239ab2bf0004d64", icon_url = "https://ssb.wiki.gallery/images/7/79/GreninjaHeadSSBUWebsite.png")
    Greninja.add_field(name = RunSpd, value = "2.288 `[8]`", inline = True)
    Greninja.add_field(name = AirSpd, value = "1.239 `[10]`", inline = True)
    Greninja.add_field(name = FallSpd, value = "1.85 `[9-11]`", inline = False)
    Greninja.add_field(name = Weight, value = "88 `[65-67]`", inline = True)
    Greninja.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    Greninja.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = Greninja)


@client.command(name = 'Palutena')         #Palutena Command: #56     
async def Palutena(context):
    Palutena = discord.Embed(title = "Kid Icarus (1986)", type = "rich", description = "Nairplane" , color = 0x81e0b1)
    Palutena.set_thumbnail(url = "https://ssb.wiki.gallery/images/6/6b/Palutena_SSBU.png")
    Palutena.set_author(name = "#56: Palutena", url = "https://open.spotify.com/track/2bJ0c1U8JiLyd7HcURB4oY?si=55f5826738974190", icon_url = "https://ssb.wiki.gallery/images/d/d7/PalutenaHeadSSBUWebsite.png")
    Palutena.add_field(name = RunSpd, value = "2.077 `[17]`", inline = True)
    Palutena.add_field(name = AirSpd, value = "1 `[58-59]`", inline = True)
    Palutena.add_field(name = FallSpd, value = "1.55 `[52-55]`", inline = False)
    Palutena.add_field(name = Weight, value = "91 `[58-59]`", inline = True)
    Palutena.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = Palutena)


@client.command(name = 'Pacman')         #Pac-Man Command: #57     
async def Pacman(context):
    Pacman = discord.Embed(title = "Pac-Man (1980)", type = "rich", description = "Unpredictable Cheese" , color = 0xf8ff00)
    Pacman.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/03/Pac-Man_SSBU.png")
    Pacman.set_author(name = "#57: Pac-Man", url = "https://open.spotify.com/track/5Jt6qtZfj0YSHfFBJUyviK?si=f343a0f5780647f2", icon_url = "https://ssb.wiki.gallery/images/3/3d/Pac-ManHeadSSBUWebsite.png")
    Pacman.add_field(name = RunSpd, value = "1.672 `[48-49]`", inline = True)
    Pacman.add_field(name = AirSpd, value = "1.092 `[39-40]`", inline = True)
    Pacman.add_field(name = FallSpd, value = "1.35 `[69-72]`", inline = False)
    Pacman.add_field(name = Weight, value = "95 `[43-46]`", inline = True)
    Pacman.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Pacman.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = Pacman)


@client.command(name = 'Robin')            #Robin Command: #58    
async def Robin(context):
    Robin = discord.Embed(title = "Fire Emblem Awakening (2012)", type = "rich", description = "Tomes, How Original" , color = 0x928f19)
    Robin.set_thumbnail(url = "https://ssb.wiki.gallery/images/8/82/Robin_SSBU.png")
    Robin.set_author(name = "#58: Robin", url = "https://open.spotify.com/track/699CaeyBkVTO87psMq3Yzw?si=91fb5d1a20bd4c9c", icon_url = "https://ssb.wiki.gallery/images/4/43/RobinHeadSSBUWebsite.png")
    Robin.add_field(name = RunSpd, value = "1.265 `[86]`", inline = True)
    Robin.add_field(name = AirSpd, value = "1.05 `[43-46]`", inline = True)
    Robin.add_field(name = FallSpd, value = "1.5 `[57-60]`", inline = False)
    Robin.add_field(name = Weight, value = "95 `[43-46]`", inline = True)
    Robin.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = Robin)


@client.command(name = 'Shulk')            #Shulk Command: #59    
async def Shulk(context):
    Shulk = discord.Embed(title = "Xenoblade Chronicles (2010)", type = "rich", description = "Melia > Fiora" , color = 0xff4700)
    Shulk.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/0f/Shulk_SSBU.png")
    Shulk.set_author(name = "#59: Shulk", url = "https://open.spotify.com/track/428HQh9G3bvjLcv6a2yWDY?si=675eceb833c740f6", icon_url = "https://ssb.wiki.gallery/images/b/bf/ShulkHeadSSBUWebsite.png")
    Shulk.add_field(name = RunSpd, value = "1.672 `[48-49]`", inline = True)
    Shulk.add_field(name = AirSpd, value = "1.113 `[32]`", inline = True)
    Shulk.add_field(name = FallSpd, value = "1.58 `[47-50]`", inline = False)
    Shulk.add_field(name = Weight, value = "97 `[36-38]`", inline = True)
    Shulk.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = Shulk)


@client.command(name = 'BowserJr')         #Bowser Jr. Command: #60    
async def BowserJr(context):
    Jr = discord.Embed(title = "Super Mario Sunshine (2002)", type = "rich", description = "The Real Roy" , color = 0x0fdf8f)
    Jr.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/2b/Bowser_Jr._SSBU.png")
    Jr.set_author(name = "#60: Bowser Jr.", url = "https://open.spotify.com/track/6euyBF9W9EvBwoTVM1gS5N?si=ce0be307bb324f08", icon_url = "https://ssb.wiki.gallery/images/3/3e/BowserJrHeadSSBUWebsite.png")
    Jr.add_field(name = RunSpd, value = "1.566 `[66]`", inline = True)
    Jr.add_field(name = AirSpd, value = "1.134 `[27-29]`", inline = True)
    Jr.add_field(name = FallSpd, value = "1.65 `[32-37]`", inline = False)
    Jr.add_field(name = Weight, value = "108 `[9-12]`", inline = True)
    Jr.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Jr)




@client.command(name = 'Duckhunt')         #Duck Hunt Command: #61  THE ABOVE RANKS ARE WRONG, FIX THEM LATER    
async def Duckhunt(context):
    duck = discord.Embed(title = "Duck Hunt (1984)", type = "rich", description = "Exploitable Recovery" , color = 0x9c3838)
    duck.set_thumbnail(url = "https://ssb.wiki.gallery/images/d/d8/Duck_Hunt_SSBU.png")
    duck.set_author(name = "#61: Duck Hunt", url = "https://open.spotify.com/track/4LConvV84tce9nv0EDh0eK?si=1b2933a1d17c4398", icon_url = "https://ssb.wiki.gallery/images/3/38/DuckHuntHeadSSBUWebsite.png")
    duck.add_field(name = RunSpd, value = "1.793 `[36]`", inline = True)
    duck.add_field(name = AirSpd, value = "1.155 `[20-25]`", inline = True)
    duck.add_field(name = FallSpd, value = "1.65 `[33-38]`", inline = False)
    duck.add_field(name = Weight, value = "86 `[70-71]`", inline = True)
    duck.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    duck.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = duck)


@client.command(name = 'Ryu')              #Ryu Command: #62    
async def Ryu(context):
    ryu = discord.Embed(title = "Street Fighter (1987)", type = "rich", description = "Akuma > Ryu" , color = 0x8fa8ae)
    ryu.set_thumbnail(url = "https://ssb.wiki.gallery/images/6/61/Ryu_SSBU.png")
    ryu.set_author(name = "#62: Ryu", url = "https://open.spotify.com/track/6UjaIJCoHvLUzIDZegPZPn?si=4d1ffcbcf8454eec", icon_url = "https://ssb.wiki.gallery/images/2/20/RyuHeadSSBUWebsite.png")
    ryu.add_field(name = RunSpd, value = "1.6 `[59]`", inline = True)
    ryu.add_field(name = AirSpd, value = "1.12 `[30-31]`", inline = True)
    ryu.add_field(name = FallSpd, value = "1.6 `[43-47]`", inline = False)
    ryu.add_field(name = Weight, value = "103 `[27-28]`", inline = True)
    ryu.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    ryu.set_footer(text = "Despite being very similar, Ryu runs slower than Ken.")
    await context.message.channel.send(embed = ryu)


@client.command(name = 'Ken')              #Ken Command: #63    
async def Ken(context):
    ken = discord.Embed(title = "Street Fighter (1987)", type = "rich", description = "He's Red, But He's Not Marth" , color = 0xff0000)
    ken.set_thumbnail(url = "https://ssb.wiki.gallery/images/f/f6/Ken_SSBU.png")
    ken.set_author(name = "#63: Ken", url = "https://open.spotify.com/track/2h9meI3ugFtFaopmmJNJX0?si=d36f99bf07e14b28", icon_url = "https://ssb.wiki.gallery/images/e/ef/KenHeadSSBUWebsite.png")
    ken.add_field(name = RunSpd, value = "1.76 `[37-40]`", inline = True)
    ken.add_field(name = AirSpd, value = "1.12 `[30-31]`", inline = True)
    ken.add_field(name = FallSpd, value = "1.6 `[43-47]`", inline = False)
    ken.add_field(name = Weight, value = "103 `[27-28]`", inline = True)
    ken.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    ken.set_footer(text = "Despite being very similar, Ken runs faster than Ryu.")
    await context.message.channel.send(embed = ken)


@client.command(name = 'Cloud')            #Cloud Command: #64    
async def Cloud(context):
    cloud = discord.Embed(title = "Final Fantasy VII (1997)", type = "rich", description = "Can't Disrespect The FF Series" , color = 0x272220)
    cloud.set_thumbnail(url = "https://ssb.wiki.gallery/images/e/e7/Cloud-Alt1_SSBU.png")
    cloud.set_author(name = "#64: Cloud", url = "https://open.spotify.com/track/76hjP6yrfypRpf82vhNGnr?si=2423534a8baa44f4", icon_url = "https://ssb.wiki.gallery/images/c/cb/CloudHeadSSBUWebsite.png")
    cloud.add_field(name = RunSpd, value = "2.167 `[13]`", inline = True)
    cloud.add_field(name = AirSpd, value = "1.155 `[20-25]`", inline = True)
    cloud.add_field(name = FallSpd, value = "1.68 `[30-31]`", inline = False)
    cloud.add_field(name = Weight, value = "100 `[31-32]`", inline = True)
    cloud.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    cloud.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = cloud)


@client.command(name = 'Corrin')           #Corrin Command: #65    
async def Corrin(context):
    corn = discord.Embed(title = "Fire Emblem Fates (2015)", type = "rich", description = "Hot Take: Camilla Is Bad" , color = 0xae9e99)
    corn.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/c4/Corrin_SSBU.png")
    corn.set_author(name = "#65: Corrin", url = "https://open.spotify.com/track/5SYruzE3eWWXG8K6sJnbH0?si=bd7b8858ae6a4fa2", icon_url = "https://ssb.wiki.gallery/images/6/6a/CorrinHeadSSBUWebsite.png")
    corn.add_field(name = RunSpd, value = "1.595 `[60-64]`", inline = True)
    corn.add_field(name = AirSpd, value = "1.019 `[52-54]`", inline = True)
    corn.add_field(name = FallSpd, value = "1.65 `[33-38]`", inline = False)
    corn.add_field(name = Weight, value = "98 `[33-36]`", inline = True)
    corn.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    await context.message.channel.send(embed = corn)


@client.command(name = 'Bayo')        #Bayonetta Command: #66    
async def Bayo(context):
    bayo = discord.Embed(title = "Bayonetta (2009)", type = "rich", description = "Her Gameplay Does Not Fit Smash" , color = 0x000000)
    bayo.set_thumbnail(url = "https://ssb.wiki.gallery/images/7/7c/Bayonetta_SSBU.png")
    bayo.set_author(name = "#66: Bayonetta", url = "https://open.spotify.com/track/3Qm1GqTk8lh8lSbhe0D0Vt?si=f468b2627e224e2f", icon_url = "https://ssb.wiki.gallery/images/2/27/BayonettaHeadSSBUWebsite.png")
    bayo.add_field(name = RunSpd, value = "1.76 `[37-40]`", inline = True)
    bayo.add_field(name = AirSpd, value = "1.019 `[52-54]`", inline = True)
    bayo.add_field(name = FallSpd, value = "1.77 `[20-21]`", inline = False)
    bayo.add_field(name = Weight, value = "81 `[75]`", inline = True)
    bayo.add_field(name = Weightclass, value = "`Featherweight`", inline = True)
    bayo.set_footer(text = "Can: Wall Jump, Wall Cling")
    await context.message.channel.send(embed = bayo)


@client.command(name = 'Inkling')          #Inkling Command: #67    
async def Inkling(context):
    ink = discord.Embed(title = "Splatoon (2015)", type = "rich", description = "Roller = Dead" , color = 0xff8700)
    ink.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/2e/Inkling_SSBU.png")
    ink.set_author(name = "#67: Inkling", url = "https://open.spotify.com/track/27eNesnp13438IaVE4kI82?si=81bf9c78c6154612", icon_url = "https://ssb.wiki.gallery/images/0/04/InklingHeadSSBUWebsite.png")
    ink.add_field(name = RunSpd, value = "1.925 `[25]`", inline = True)
    ink.add_field(name = AirSpd, value = "1.208 `[13-17]`", inline = True)
    ink.add_field(name = FallSpd, value = "1.58 `[48-51]`", inline = False)
    ink.add_field(name = Weight, value = "94 `[48-51]`", inline = True)
    ink.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    ink.set_footer(text = "Can: Wall Jump")
    await context.message.channel.send(embed = ink)






@client.command(name = 'Ridley')           #Ridley Command: #68    SIXTH ROW STARTS HERE
async def Ridley(context):
    rid = discord.Embed(title = "Metroid (1986)", type = "rich", description = "Too Large For Smash" , color = 0xab47f5)
    rid.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/27/Ridley_SSBU.png")
    rid.set_author(name = "#68: Ridley", url = "https://open.spotify.com/track/4XpuWpTK8vsrA5JZiFsMHz?si=f5175af1b36f405e", icon_url = "https://ssb.wiki.gallery/images/7/7c/RidleyHeadSSBUWebsite.png")
    rid.add_field(name = RunSpd, value = "2.2 `[10-11]`", inline = True)
    rid.add_field(name = AirSpd, value = "1.05 `[43-46]`", inline = True)
    rid.add_field(name = FallSpd, value = "1.78 `[19]`", inline = False)
    rid.add_field(name = Weight, value = "107 `[14-18]`", inline = True)
    rid.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = rid)


@client.command(name = 'Simon')            #Simon Command: #69    
async def Simon(context):
    simon = discord.Embed(title = "Castlevania (1986)", type = "rich", description = "Overhyped" , color = 0xa89db0)
    simon.set_thumbnail(url = "https://ssb.wiki.gallery/images/9/95/Simon_SSBU.png")
    simon.set_author(name = "#69: Simon", url = "https://open.spotify.com/track/4HXzm6IXEvVbfzEADMAVng?si=fd04aba3800f49ab", icon_url = "https://ssb.wiki.gallery/images/5/52/SimonHeadSSBUWebsite.png")
    simon.add_field(name = RunSpd, value = "1.52 `[72-73]`", inline = True)
    simon.add_field(name = AirSpd, value = "0.94 `[69-70]`", inline = True)
    simon.add_field(name = FallSpd, value = "1.85 `[9-11]`", inline = False)
    simon.add_field(name = Weight, value = "107 `[14-18]`", inline = True)
    simon.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    simon.set_footer(text = "Exact same stats and ranks as Richter\nCan: Tether Recovery")
    await context.message.channel.send(embed = simon)


@client.command(name = 'Richter')          #Richter Command: #70    
async def Richter(context):
    richter = discord.Embed(title = "Castlevania: Rondo of Blood (1993)", type = "rich", description = "Worst Clone Ever Made" , color = 0x1c299a)
    richter.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/c2/Richter_SSBU.png")
    richter.set_author(name = "#70: Richter", url = "https://open.spotify.com/track/7jzUgYVnL1fHdj8wexTkYV?si=c46631c6cc15463e", icon_url = "https://ssb.wiki.gallery/images/a/ab/RichterHeadSSBUWebsite.png")
    richter.add_field(name = RunSpd, value = "1.52 `[72-73]`", inline = True)
    richter.add_field(name = AirSpd, value = "0.94 `[69-70]`", inline = True)
    richter.add_field(name = FallSpd, value = "1.85 `[9-11]`", inline = False)
    richter.add_field(name = Weight, value = "107 `[14-18]`", inline = True)
    richter.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    richter.set_footer(text = "Exact same stats and ranks as Richter\nCan: Tether Recovery")
    await context.message.channel.send(embed = richter)


@client.command(name = 'Krool')            #King K. Rool Command: #71    
async def Krool(context):
    King = discord.Embed(title = "Donkey Kong Country (1994)", type = "rich", description = "BuStEd HeAvY?" , color = 0x07ab13)
    King.set_thumbnail(url = "https://ssb.wiki.gallery/images/b/b6/King_K._Rool_SSBU.png")
    King.set_author(name = "#71: King K. Rool", url = "https://open.spotify.com/track/3qZAMhNqJGiUrMGvkyautR?si=0e17e9cfa317486d", icon_url = "https://ssb.wiki.gallery/images/3/35/KingKRoolHeadSSBUWebsite.png")
    King.add_field(name = RunSpd, value = "1.485 `[76]`", inline = True)
    King.add_field(name = AirSpd, value = "0.945 `[68]`", inline = True)
    King.add_field(name = FallSpd, value = "1.7 `[27-29]`", inline = False)
    King.add_field(name = Weight, value = "133 `[2]`", inline = True)
    King.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    await context.message.channel.send(embed = King)


@client.command(name = 'Isabelle')         #Isabelle Command: #72    
async def Isabelle(context):
    Isa = discord.Embed(title = "Animal Crossing: New Leaf (2012)", type = "rich", description = "Rod Mechanics" , color = 0xecef18)
    Isa.set_thumbnail(url = "https://ssb.wiki.gallery/images/2/2b/Isabelle_SSBU.png")
    Isa.set_author(name = "#72: Isabelle", url = "https://open.spotify.com/track/5KG2Fv3gQBpFKHgNY3qMaG?si=80421c68b28b4eb8", icon_url = "https://ssb.wiki.gallery/images/2/2e/IsabelleHeadSSBUWebsite.png")
    Isa.add_field(name = RunSpd, value = "1.48 `[77]`", inline = True)
    Isa.add_field(name = AirSpd, value = "1.02 `[51]`", inline = True)
    Isa.add_field(name = FallSpd, value = "1.3 `[79-81]`", inline = False)
    Isa.add_field(name = Weight, value = "88 `[66-68]`", inline = True)
    Isa.add_field(name = Weightclass, value = "`Lightweight`", inline = True)
    Isa.set_footer(text = "Can: Tether Recovery")
    await context.message.channel.send(embed = Isa)


@client.command(name = 'Incineroar')       #Incineroar Command: #73    
async def Incineroar(context):
    Roar = discord.Embed(title = "Pokemon Sun and Moon (2016)", type = "rich", description = "Don't Press Shield" , color = 0xe0524a)
    Roar.set_thumbnail(url = "https://ssb.wiki.gallery/images/c/c4/Incineroar_SSBU.png")
    Roar.set_author(name = "#73: Incineroar", url = "https://open.spotify.com/track/0t8enIfj5nKlj1tqh57iKp?si=8d4a90653da24ca8", icon_url = "https://ssb.wiki.gallery/images/e/e3/IncineroarHeadSSBUWebsite.png")
    Roar.add_field(name = RunSpd, value = "1.18 `[88]`", inline = True)
    Roar.add_field(name = AirSpd, value = "0.88 `[80]`", inline = True)
    Roar.add_field(name = FallSpd, value = "1.76 `[22-23]`", inline = False)
    Roar.add_field(name = Weight, value = "116 `[6-7]`", inline = True)
    Roar.add_field(name = Weightclass, value = "`Super Heavyweight`", inline = True)
    Roar.set_footer(text = "Slowest run speed in the game")
    await context.message.channel.send(embed = Roar)


@client.command(name = 'Plant')            #Piranha Plant Command: #74    
async def Plant(context):
    Gang = discord.Embed(title = "Super Mario Bros. (1985)", type = "rich", description = "Plant Gang" , color = 0x23d13f)
    Gang.set_thumbnail(url = "https://ssb.wiki.gallery/images/f/f0/Piranha_Plant_SSBU.png")
    Gang.set_author(name = "#74: Piranha Plant", url = "https://open.spotify.com/track/7HgjBaplhOX93Ji1bPVUOi?si=24ab331345564ac1", icon_url = "https://ssb.wiki.gallery/images/c/cf/PiranhaPlantHeadSSBUWebsite.png")
    Gang.add_field(name = RunSpd, value = "1.72 `[44-45]`", inline = True)
    Gang.add_field(name = AirSpd, value = "1 `[58-59]`", inline = True)
    Gang.add_field(name = FallSpd, value = "1.95 `[2-4]`", inline = False)
    Gang.add_field(name = Weight, value = "112 `[9]`", inline = True)
    Gang.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Gang)


@client.command(name = 'Joker')            #Joker Command: #75    
async def Joker(context):
    Joker = discord.Embed(title = "Persona 5 (2016)", type = "rich", description = "Yu Narukami Is Better" , color = 0x170803)
    Joker.set_thumbnail(url = "https://ssb.wiki.gallery/images/5/5c/Joker_SSBU.png")
    Joker.set_author(name = "#75: Joker", url = "https://open.spotify.com/track/4PlpK3tDrcPlSYdnXMdQB6?si=b7029acf1b974ec0", icon_url = "https://ssb.wiki.gallery/images/6/63/JokerHeadSSBUWebsite.png")
    Joker.add_field(name = RunSpd, value = "2.06 `[18]`", inline = True)
    Joker.add_field(name = AirSpd, value = "1.1 `[37-38]`", inline = True)
    Joker.add_field(name = FallSpd, value = "1.63 `[39-40]`", inline = False)
    Joker.add_field(name = Weight, value = "93 `[52]`", inline = True)
    Joker.add_field(name = Weightclass, value = "`Middleweight`", inline = True)
    Joker.set_footer(text = "Can: Tether Recovery, Wall Jump")
    await context.message.channel.send(embed = Joker)


@client.command(name = 'Hero')             #Hero Command: #76    
async def Hero(context):
    Hero = discord.Embed(title = "Dragon Quest (1986)", type = "rich", description = "So Many Better RPGs Exist" , color = 0x93817a)
    Hero.set_thumbnail(url = "https://ssb.wiki.gallery/images/0/07/Hero_SSBU.png")
    Hero.set_author(name = "#76: Hero", url = "https://open.spotify.com/track/1dTGrrrrluoDAdNVRMpmKd?si=6486ac4233184f73", icon_url = "https://ssb.wiki.gallery/images/1/1e/HeroHeadSSBUWebsite.png")
    Hero.add_field(name = RunSpd, value = "1.84 `[34]`", inline = True)
    Hero.add_field(name = AirSpd, value = "1.01 `[55-56]`", inline = True)
    Hero.add_field(name = FallSpd, value = "1.57 `[52]`", inline = False)
    Hero.add_field(name = Weight, value = "101 `[30]`", inline = True)
    Hero.add_field(name = Weightclass, value = "`Heavyweight`", inline = True)
    await context.message.channel.send(embed = Hero)




client.run(TOKEN) 