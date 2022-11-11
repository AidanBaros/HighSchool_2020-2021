#CUBE DISCORD BOT V1.2.1
#Python V3.9.1
#Discord.py V1.6.0
#V1.0.0 finished 2/12/2021
#-------------------------------------------------
import os
import time
import discord
import asyncio 
import discord.utils
from BotTokens import *
from discord import user
from discord.utils import get
from dotenv import load_dotenv
from discord_components import *
from discord.ext import commands
from discord.message import Message
from discord.ext.commands.core import command
from pretty_help import PrettyHelp, DefaultMenu
from discord.ext.commands.errors import MessageNotFound
from discord.ext.commands import has_permissions, MissingPermissions
#---------
load_dotenv()
TOKEN = MAIN
BotVerson = 'V1.3.1'
ROLEc = 'Cubeular'
ROLEm = 'Muted'
ROLE9 = '9th Grader'
ROLE10 = '10th Grader'
ROLE11 = '11th Grader'
ROLE12 = '12th Grader'
WT = "War Thunder"
COD = "COD"
CSGO = "CounterStrike"
AL = "Apex Legends"
LOL = "League of Legends"
RSS = "Rainbow Six Siege"
SSB = "Super Smash Bros"
O = "Overwatch"
BF1 = "BattleField"
M = "Minecraft"
D = "Doom"
V = "Valorant"
DCP = "Developer Changelog Ping"
#----------
intents = discord.Intents.default()
intents.members = True
intents.presences = True
client = discord.Client(intents=intents)
client = discord.Client
bot = commands.Bot(command_prefix='?', intents = intents)
bot.remove_command('help')
DiscordComponents(bot)
#-------------------------------------------------
ending_note = f"Running CUBEBOT {BotVerson}"
nav = DefaultMenu()
color = discord.Color.dark_gold()
bot.help_command = PrettyHelp(active_time=120, 
color=color, 
ending_note=ending_note, 
index_title="Commands",
show_index=True, 
sort_commands=False
)
#-------------------------------------------------
@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="joins") 
    embed = discord.Embed(title = 'User Has Joined the Server:sunglasses:', description = f'\n{member} has joined us!' + f'\n\nRunning CUBEBOT {BotVerson}', color = 0xC0C0C0)
    await channel.send(embed = embed)
    role = get(member.guild.roles, name=ROLEc)
    await member.add_roles(role)
    await member.send(f'    Hi {member.name}, welcome to the CUBE Discord server!\n'
    ''' 
        For list of commands do ?help
        Please go the the Who's-Who channel and put your real name for safety reasons.
        Rules:''') 

    await member.send(
    '''(1)Your Account: 

    1. Inappropriate or offensive avatars, usernames, and statuses are prohibited. 
    2. Self-advertising through usernames or statuses is not permitted.
    3. Staff are hereby granted the right to change nicknames if and only if said username or status violates rules(s) (1) or (2) of this section, or rule (1) of Section (3).
    4. Any user may only hold one account on this server. If we suspect that a user has a secondary account, immediate action will be taken. 
    
    (2)Server Rules: 

    1. Discrimination, racist or otherwise offensive jokes, and/or hate speech through text, images, or videos will not be tolerated. 
    2. Insults, threats, excessive pinging, or any offensive content targeted at specific members is strictly not allowed. 
    3. DDOS, raid, or other such threats will not be tolerated. 
    4. Please post content in correct channels. 
    4a. Self-promotions are only allowed in #advertising channel. 
    5. Do not ask staff to become a moderator, all moderator applications are closed.
    6. Impersonating staff members, including similar avatars and nicknames is not allowed.
    7. Political opinions, including links, images, videos, avatars, nicknames, and statuses will not be tolerated. This is a school server.
    8. Please Direct Message me or an Admin with complaints about staff/server policies.
    9. Do not leak Direct Messages, locked chats, or sensitive information about this server. 
    
    (3)Content:

    1. NSFW content, text, avatars, or usernames/nicknames of any kind is strictly prohibited. 
    2. Discussing/promoting illegal activity will not be tolerated. 
    3. Staff reserves the right to remove any content for any reason at any time. 
    4. Plagiarism, spam, and copypasta are all forbidden.''')

    await member.send('''Punishment System: 

    Tier One - Warning 
     -Violating Section(1); rule (2). 
     -Violating Section (2); rule(s) (4/4a), (5), (6), or (8). 

    Tier Two - Mute
     -Violating Section(2); rule(s) (1), (2), (3), or (7). 
     -Violating Section(3); rule(s) (2) or (4).
     -Repeated violations (<2) of the rules outlined in Tier One.

    Tier Three - Kick/Role Removal
     -Violating Section(1); rule (1).
     -Violating Section(2); rule (9).
     -Repeated violations (<4) of the rules outlined in Tier One. 
     -Repeated violations (<2) of the rules outlined in Tier Two. 

    Tier Four - Ban
     -Violating Section(1); rule (4)
     -Violating Section(3); rule (1)
     -Repeated violations (<5) of the rules outlined in Tier One. 
     -Repeated violations (<3) of the rules outlined in Tier Two. 
     -Repeated violations (<1) of the rules outlined in Tier Three.
    ''')
#----------
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print("")
    print('Servers connected to:')
    for guild in bot.guilds:
        print(guild.name)
        print(guild.id)
        print("")
    print('------')
    await bot.change_presence(activity=discord.Game(f'CUBEBOT Build {BotVerson} \n Github==> https://github.com/KINGOODAN/Discord-Bot'))
#----------
@bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name="joins") 
    embed = discord.Embed(title = 'User Has Left the Server:ghost: ', description = f'\n{member} has left us. Hope they rejoin later!' + f'\n\nRunning CUBEBOT {BotVerson}', color = 0xC0C0C0)
    await channel.send(embed = embed)
#----------
@bot.event
async def on_command_error(ctx, error):
    await ctx.send(f"An error occured: {str(error)}")
#-------------------------------------------------
class Announcements(commands.Cog, description="These are the commands to make announcements."):
    #----------
    @commands.command(pass_context = True)
    @commands.has_any_role('Moderator', 'Admin')
    async def Sa(self,ctx,*,arg):
        '''An announcement command for staff.'''
        channel = discord.utils.get(ctx.guild.channels, name="announcements")
        await ctx.message.delete()
        await channel.send('||@everyone||' + ' ' + '\n**Staff Announcement**' + '\n' + arg + f'\n\nRunning CUBEBOT {BotVerson}')
    #----------
    @commands.command()
    @commands.has_role('Developer')
    async def Changelog(self,ctx,arg1): 
        '''This is the change log command that gives developers the ability to send out the change log.'''
        d = get(ctx.guild.roles, name="Developer Changelog Ping")
        channel = discord.utils.get(ctx.guild.channels, name="bot-changelog")
        await ctx.message.delete()
        await channel.send (f"||{d.mention}|| \n\n **Bot Update!** \n Version {BotVerson} \n\n {arg1}" + f'\n\nRunning CUBEBOT {BotVerson}')
#-------------------------------------------------
class Suggest_Report(commands.Cog, description="Theses are commands to make suggestions or report things."):
    #----------
    @commands.command(pass_context = True)
    async def bugreport(self,ctx,*,arg):
        '''A command that allows you to report bug with the bot.'''
        channel = discord.utils.get(ctx.guild.channels, name="bug-report-output")
        embed = discord.Embed(title = 'Bug Report', description = f'\n\n{arg}' + f'\n\n Bug Report initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        await channel.send(embed=embed)
        await ctx.send("Your report has been logged!")
    #----------
    @commands.command(pass_context = True)
    async def botsuggest(self,ctx,*,arg):
        '''A command that lets you make suggestions about the bot.'''
        channel = discord.utils.get(ctx.guild.channels, name="server-suggestions")
        embed = discord.Embed(title = 'Bot Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
    #----------
    @commands.command(pass_context = True)
    async def serversuggest(self,ctx,*,arg):
        '''A command that lets you make suggestions about the server.'''
        channel = discord.utils.get(ctx.guild.channels, name="server-suggestions")
        embed = discord.Embed(title = 'Server Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
    #----------
    @commands.command(pass_context = True)
    async def gamesuggest(self,ctx,*,arg):
        '''A command that lets suggest games to add the the lftroles command.'''
        channel = discord.utils.get(ctx.guild.channels, name="game-suggestions")
        embed = discord.Embed(title = 'Game Suggestion', description = f'\n\n**{arg}**' + f'\n\n Poll initiated by {ctx.message.author}'+ f'\n\nRunning CUBEBOT {BotVerson}')
        msg = await channel.send(embed=embed)
        emoji = ('⏫')
        emoji2 = ('⏬')
        await msg.add_reaction(emoji)
        await msg.add_reaction(emoji2)
#-------------------------------------------------
class Miscellaneous(commands.Cog, description="These are Miscellaneous commands."):
    #----------
    @commands.command(pass_context = True)
    async def memberlist(self,ctx):
        '''A command that gives a list of all the members on the server.'''
        member = '\n  '.join([member.name for member in ctx.guild.members])
        embed = discord.Embed(title = 'Members:', description = f'{member}' + f'\n\nRunning CUBEBOT {BotVerson}',color = 0xC0C0C0)
        await ctx.send (embed = embed)
    #----------
    @commands.command(pass_context = True)
    async def hello(self,ctx): 
        '''A fun command that say Hello.'''
        await ctx.send(f'Hello {ctx.message.author.mention}!')
    #----------
    @commands.command(pass_context = True)
    async def hi(self,ctx): 
        '''A fun command that say Hi.'''
        await ctx.send(f'Hi {ctx.message.author.mention}!')
#-------------------------------------------------
class Roles(commands.Cog, description="These are all the commands that you use to get roles."):
    #----------
    @commands.command(name="graderoles", aliases=["GradeRoles", "graderole"], pass_context = True)
    async def graderoles(self,ctx):
        """This command will bring up buttons which you can select and they will give you a grade role. A grade role gives you access to channels that are specific to that grade. Once you have a grade role you can not have a second one so make sure you select the correct role."""
        #----------
        mainembed = discord.Embed(title = "Grade Roles", description = "\n\n Here you can select a reaction and it will give you the corresponding role." + f"\n\nRunning CUBEBOT {BotVerson}")
        alreadyhave = discord.Embed(title = "You Already Have A Grade Role", description = "\n\n You already have a grade role so this command won't work for you. If you have the wrong grade please contact an admin to get it fixed." + f"\n\nRunning CUBEBOT {BotVerson}")
        ninethembed = discord.Embed(title = "9th Grade Role", description = f"\n\n {ctx.message.author.mention} you now have the {ROLE9} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
        tenthembed = discord.Embed(title = "10th Grade Role", description = f"\n\n {ctx.message.author.mention} you now have the {ROLE10} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
        eleventhembed = discord.Embed(title = "11th Grade Role", description = f"\n\n {ctx.message.author.mention} you now have the {ROLE11} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
        twelfthembed = discord.Embed(title = "12th Grade Role", description = f"\n\n {ctx.message.author.mention} you now have the {ROLE12} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
        role9 = discord.utils.find(lambda r: r.name == f'{ROLE9}', ctx.message.guild.roles)
        role10 = discord.utils.find(lambda r: r.name == f'{ROLE10}', ctx.message.guild.roles)
        role11 = discord.utils.find(lambda r: r.name == f'{ROLE11}', ctx.message.guild.roles)
        role12 = discord.utils.find(lambda r: r.name == f'{ROLE12}', ctx.message.guild.roles)
        gr = await ctx.send(embed=mainembed, 
        components = [[Button(style = 2, label = "9th"), 
        Button(style = 2, label = "10th"), 
        Button(style = 2, label = "11th"), 
        Button(style = 2, label = "12th")]]
        )
        #----------
        async def ninthgrade():
            if role9 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role10 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role11 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role12 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            else:
                await gr.edit (embed=ninethembed)
                await ctx.message.author.add_roles(role9)
        #----------
        async def tenthgrade():
            if role9 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role10 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role11 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role12 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            else:
                await gr.edit (embed=tenthembed)
                await ctx.message.author.add_roles(role10)
        #----------
        async def eleventhgrade():
            if role9 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role10 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role11 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role12 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            else:
                await gr.edit (embed=eleventhembed)
                await ctx.message.author.add_roles(role11)
        #----------
        async def twelfthgrade():
            if role9 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role10 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role11 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            elif role12 in ctx.message.author.roles:
                await gr.edit(embed=alreadyhave)
            else:
                await gr.edit (embed=twelfthembed)
                await ctx.message.author.add_roles(role12)
        #----------
        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel
        #----------
        try:
            res = await bot.wait_for("button_click", check=check, timeout=60)
            user = res.component.label
            if user=="9th":
                await ninthgrade()
            if user=="10th":
                await tenthgrade()
            if user=="11th":
                await eleventhgrade()
            if user=="12th":
                await twelfthgrade()
        except TimeoutError:
            pass
    #----------
    @commands.command(name="lftroles",aliases=["LFTRoles", "lftrole"] , pass_context = True)
    async def lftroles(self,ctx):
        """This command brings up buttons that you can click that will give you the corresponding role. These roles are here to make it easier to find people to play video games with."""
        embed1 = discord.Embed(title = "LFTRoles", description = "\n\n Here you can select the games that you play giving you the corresponding role making it easier for others to contact you." + f"\n\nRunning CUBEBOT {BotVerson}")
        components = [
            [Button(style = 2, label = "WarThunder"), Button(style = 2, label = "CallOfDuty"), Button(style = 2, label = "CounterStrike"), Button(style = 2, label = "ApexLegends")],
            [Button(style = 2, label = "LeagueofLegends"), Button(style = 2, label = "SuperSmashBros"), Button(style = 2, label = "RainbowSixSiege"), Button(style = 2, label = "Overwatch")],
            [Button(style = 2, label = "BattleField"), Button(style = 2, label = "Minecraft"), Button(style = 2, label = "Doom"), Button(style = 2, label = "Valorant")]
            ] 
        lftr = await ctx.send (embed = embed1, components = components)
        alreadyhave = discord.Embed(title = "You Already Have This Role", description = "\n\n You already have this role." + f"\n\nRunning CUBEBOT {BotVerson}")
        rolewt = get(ctx.guild.roles, name = f"{WT}")
        rolecod = get(ctx.guild.roles, name = f"{COD}")
        rolecsgo = get(ctx.guild.roles, name = f"{CSGO}")
        roleal = get(ctx.guild.roles, name = f"{AL}")
        rolelol = get(ctx.guild.roles, name = f"{LOL}")
        rolessb = get(ctx.guild.roles, name = f"{SSB}")
        rolerss = get(ctx.guild.roles, name = f"{RSS}")
        roleo = get(ctx.guild.roles, name = f"{O}")
        rolebf = get(ctx.guild.roles, name = f"{BF1}")
        rolem = get(ctx.guild.roles, name = f"{M}")
        roled = get(ctx.guild.roles, name = f"{D}")
        rolev = get(ctx.guild.roles, name = f"{V}")
        while True:
            #----------
            async def WarThunder():
                if rolewt in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolewt not in ctx.message.author.roles:
                    embedwt = discord.Embed(title = "WarThunder", description = f"{ctx.message.author.mention} you now have the {WT} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedwt) 
                    await ctx.message.author.add_roles(rolewt)
            #----------
            async def CallOfDuty(): 
                if rolecod in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolecod not in ctx.message.author.roles:
                    embedcod = discord.Embed(title = "CallOfDuty", description = f"{ctx.message.author.mention} you now have the {COD} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedcod) 
                    await ctx.message.author.add_roles(rolecod)
            #----------
            async def CounterStrike(): 
                if rolecsgo in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolecsgo not in ctx.message.author.roles:
                    embedcsgo = discord.Embed(title = "CounterStrike", description = f"{ctx.message.author.mention} you now have the {CSGO} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedcsgo) 
                    await ctx.message.author.add_roles(rolecsgo)
            #----------
            async def ApexLegends():
                if roleal in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if roleal not in ctx.message.author.roles:
                    embedal = discord.Embed(title = "ApexLegends", description = f"{ctx.message.author.mention} you now have the {AL} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedal) 
                    await ctx.message.author.add_roles(roleal)
            #----------
            async def LeagueofLegends(): 
                if rolelol in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolelol not in ctx.message.author.roles:
                    embedlol = discord.Embed(title = "LeagueofLegends", description = f"{ctx.message.author.mention} you now have the {LOL} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedlol) 
                    await ctx.message.author.add_roles(rolelol)
            #----------
            async def SuperSmashBros(): 
                if rolessb in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolessb not in ctx.message.author.roles:
                    embedssb = discord.Embed(title = "SuperSmashBros", description = f"{ctx.message.author.mention} you now have the {SSB} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedssb) 
                    await ctx.message.author.add_roles(rolessb)
            #----------
            async def RainbowSixSiege(): 
                if rolerss in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolerss not in ctx.message.author.roles:
                    embedrss = discord.Embed(title = "RainbowSixSiege", description = f"{ctx.message.author.mention} you now have the {RSS} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedrss) 
                    await ctx.message.author.add_roles(rolerss)
            #----------
            async def Overwatch(): 
                if roleo in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if roleo not in ctx.message.author.roles:
                    embedo = discord.Embed(title = "Overwatch", description = f"{ctx.message.author.mention} you now have the {O} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedo) 
                    await ctx.message.author.add_roles(roleo)
            #----------
            async def BattleField(): 
                if rolebf in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolebf not in ctx.message.author.roles:
                    embedbf = discord.Embed(title = "BattleField", description = f"{ctx.message.author.mention} you now have the {BF1} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedbf) 
                    await ctx.message.author.add_roles(rolebf)
            #----------
            async def Minecraft(): 
                if rolem in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolem not in ctx.message.author.roles:
                    embedm = discord.Embed(title = "Minecraft", description = f"{ctx.message.author.mention} you now have the {M} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedm) 
                    await ctx.message.author.add_roles(rolem)
            #----------
            async def Doom(): 
                if roled in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if roled not in ctx.message.author.roles:
                    embedd = discord.Embed(title = "Doom", description = f"{ctx.message.author.mention} you now have the {D} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedd) 
                    await ctx.message.author.add_roles(roled)
            #----------
            async def Valorant(): 
                if rolev in ctx.message.author.roles:
                    await lftr.edit(embed=alreadyhave)
                if rolev not in ctx.message.author.roles:
                    embedd = discord.Embed(title = "Valorant", description = f"{ctx.message.author.mention} you now have the {V} role!" + f"\n\nRunning CUBEBOT {BotVerson}")
                    await lftr.edit(embed=embedd) 
                    await ctx.message.author.add_roles(rolev)
            #----------
            def check(res):
                return ctx.author == res.user and res.channel == ctx.channel
            #----------
            res = await bot.wait_for("button_click", check=check)
            members =  res.component.label
            if members == "WarThunder":
                await WarThunder()
            if members == "CallOfDuty":
                await CallOfDuty()
            if members == "CounterStrike":
                await CounterStrike()
            if members == "ApexLegends":
                await ApexLegends()
            if members == "LeagueofLegends":
                await LeagueofLegends()
            if members == "SuperSmashBros":
                await SuperSmashBros()
            if members == "RainbowSixSiege":
                await RainbowSixSiege()
            if members == "Overwatch":
                await Overwatch()
            if members == "BattleField":
                await BattleField()
            if members == "Minecraft":
                await Minecraft()
            if members == "Doom":
                await Doom()
            if members == "Valorant":
                await Valorant()
    #----------
    @commands.command(name="DCLProle", aliases=["DCLPRole"],pass_context = True)
    async def DCLProle(self,ctx): 
        '''This command give you the Developer Change Log Ping role.'''
        role = get(ctx.guild.roles, name = f"{DCP}")
        await ctx.send (f'{ctx.message.author.mention} you now have the {DCP} role!') 
        await ctx.message.author.add_roles(role)
#-------------------------------------------------
class Admin(commands.Cog, description="These are commands for the staff of the server."):
    #----------
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin', 'Trial Moderator')
    async def mute(self,ctx, member: discord.Member, time: int, d, *, reason=None):
        '''A command to mute members.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                embedalreadymuted = discord.Embed(title="Already Muted", description=f"{member.mention} is already muted " + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                if role in member.roles:
                    await ctx.send(embed=embedalreadymuted)
                else:
                    await member.add_roles(role)
                    embed = discord.Embed(title="Muted!", description=f"{member.mention} has been muted ", colour=discord.Colour.red())
                    embed.add_field(name="Reason:", value=reason, inline=False)
                    embed.add_field(name="Time left for the mute:", value=f'{time} {d}' + f'\n\nRunning CUBEBOT {BotVerson}', inline=False)
                    await ctx.send(embed=embed)
                    if d == "s":
                        await asyncio.sleep(time)
                    if d == "m":
                        await asyncio.sleep(time*60)
                    if d == "h":
                        await asyncio.sleep(time*60*60)
                    if d == "d":
                        await asyncio.sleep(time*60*60*24)
                    if role in member.roles:
                        await member.remove_roles(role)
                        embed = discord.Embed(title="Unmuted ", description=f"{member.mention} your mute time is up." + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                        await ctx.send(embed=embed)
                    else:
                        return
    #----------
    @commands.command()
    @commands.has_any_role('Moderator', 'Admin', 'Trial Moderator')
    async def unmute(self,ctx, member: discord.Member):
        '''A command to unmute member who are muted.'''
        guild = ctx.guild
        for role in guild.roles:
            if role.name == "Muted":
                if role in member.roles:
                    await member.remove_roles(role)
                    embed = discord.Embed(title="unmuted ", description=f"{member.mention} you have been unmuted" + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                    await ctx.send(embed=embed)
                else:
                    embednot = discord.Embed(title="Not Muted", description=f"{member.mention} is not muted." + f'\n\nRunning CUBEBOT {BotVerson}', color=discord.Colour.red())
                    await ctx.send(embed=embednot)
                    return
    #----------
    @commands.command()
    @commands.has_any_role('Admin', 'Moderator', 'Trial Moderator')
    async def warn(self,ctx,  member: discord.Member, *, reason = None ):
        '''This command warns people when they are misbehaving'''
        embed = discord.Embed(title = "**Warn**", description = f'\n**{member.mention} Has Been Warned**', color=discord.Color.blue())
        embed.add_field (name = "Reason: ", value = reason + f'\n\nRunning CUBEBOT {BotVerson}', inline = False )
        await ctx.send(f"{member.mention}")
        await ctx.send(embed = embed) 
#-------------------------------------------------
def run():
    bot.add_cog(Announcements(bot))
    bot.add_cog(Suggest_Report(bot))
    bot.add_cog(Miscellaneous(bot))
    bot.add_cog(Roles(bot))
    bot.add_cog(Admin(bot))
    bot.run(TOKEN)
#-------------------------------------------------
if __name__ == "__main__":
    run()
