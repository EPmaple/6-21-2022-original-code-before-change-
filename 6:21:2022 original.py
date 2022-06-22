import os
import discord
from discord.ext import commands, tasks
from datetime import datetime, timezone, timedelta
from replit import db
from keep_alive import keep_alive
import nest_asyncio
import requests
import traceback

# INIT PART 1 #

nest_asyncio.apply()

client = commands.Bot(command_prefix='!')

name_id = {'AGELaVolpe': '720352409817186345', 'AGE_Atomsk': '433367046248595466',\
           'AGE_Cats': '359361962414440449', 'Cats On Mars': '359361962414440449',\
           'AGE_Leofar': '328108124953247746', 'Leofarr': '328108124953247746',\
           'AGE_Lux': '400768894521966604', 'luxury777': '400768894521966604',\
           'AGE_Solid': '222808023255613440','SolidD': '222808023255613440',\
           'AGE_Vent': '207924668844212225', 'Vent': '207924668844212225',\
           'Ainthe': '234077877958606849', 'Angel': '563787164987686925',\
           'Apeks': '139662285089013760', 'Aquarios':'342895832057643018',\
           'Ben': '281087273418752001', 'traffyboi': '120428736637173760',\
           'CloudExt': '362102976581599241', 'Collin': '884080970666504202',\
           'Collin still PURE F2P': '884080970666504202', 'Consutron': '153660394349658112',\
           'Dan': '274133775917645824','Dante': '270699806949638144',\
           'Evian': '591897303573331978', 'GoldHunter': '926128198574547024', \
           'Gunther': '315112026093649920', 'G̷̉̕u̷͑̚ǹ̴̕ẗ̴̕ḧ̵̏e̴͆́ṙ̵͝': '315112026093649920', \
           'Ioni': '202635850599759873', 'JAV_Dostic': '312642855330119681',\
           'JAV_Eolf ': '162171044566794240','JAV_Moss': '207111511410212865',\
           'JAV_booyah': '211679799867998218', 'eph || booyah': '211679799867998218',\
           'KENSHIN': '509805857425588224', 'Levi': '223398953549299712',\
           'Link2D3atH': '139262103214227456', 'Maori':'944366152648372266',\
           'Mixer': '201177323293114368', 'MoonMan': '250779681257684992',\
           'Moose': '571291284480851979', 'Neostep':'248297824477773825',\
           'Odyn': '553055447469522944', 'Pengest':'364344681129312257',\
           'PlainDoe': '189350494328586240','ReddlsRow': '274682038970482688',\
           'SenorTonto': '130852537199886337', 'Spikeman': '134863783444086784',\
           'Spike/Chitoge': '134863783444086784', 'Tachii': '176147192719998977',\
           'Tedo': '826618819191242792', 'Thaelon': '197085461624127488',\
           'ULTRA_Foxs': '396398521462554624', 'Foxcolt': '396398521462554624',\
           'Ultra_Moon': '497120107819040768', 'Moon': '497120107819040768',\
           'Unihorn':'355906565422841867', 'virant (Variant-1)': '579199616143327258',\
           'WindaRB': '673517909125103619', 'Daedalus': '210041889414447105',\
           'latvice': '281088989610377216', 'mUmU': '500124144755671040',\
           'zero00': '563082215198556211', '17maple': '253994447782543361',\
           'GonBu': '465942228791984149', 'aile': '123456789', 'zeta': '333666',\
           'Zerefsis': '215506389353758720', 'Tympest': '292615553942683648',\
           'leafa1244': '187764065131560960', 'Tatumi': '394763425777057794',\
           'Firis': '323444581033050113', 'Ciaosuh': '218659635513524224',\
           'donuts':'506124628188594181', 'fiE':'961291207210856448',\
           'mantis3175':'560576301149192203', 'rocketeer':'238091448073846784',\
           'esyw':'847443895327785030','RenTrout':'332846967971512322'}

id_name = {'333666': 'zeta','720352409817186345':'LaVolpe', '433367046248595466': 'Atomsk',\
           '359361962414440449': 'Cats On Mars', '328108124953247746': 'Leofarr',\
           '400768894521966604': 'luxury777', '222808023255613440': 'SolidD',\
           '207924668844212225': 'Vent','234077877958606849': 'Ainthe',\
           '563787164987686925': 'Angel', '139662285089013760': 'Apeks',\
           '342895832057643018':'Aquarios','281087273418752001': 'Ben',\
           '120428736637173760': 'traffyboi','362102976581599241': 'CloudExt',\
           '884080970666504202': 'Collin', '153660394349658112': 'Consutron',\
           '274133775917645824': 'Dan', '270699806949638144': 'Dante',\
           '591897303573331978': 'Evian','926128198574547024': 'GoldHunter',\
           '315112026093649920': 'Gunther', '202635850599759873': 'Ioni',\
           '312642855330119681': 'Dostic', '162171044566794240': 'Eolf',\
           '207111511410212865': 'Moss', '211679799867998218': 'eph || booyah',\
           '509805857425588224': 'Kenshin','223398953549299712': 'Levi',\
           '139262103214227456': 'Link2D3atH', '944366152648372266':'Maori',\
           '201177323293114368': 'Mixer','250779681257684992': 'MoonMan',\
           '571291284480851979':'Moose', '248297824477773825':'Neostep',\
           '553055447469522944': 'Odyn', '364344681129312257':'Pengest',\
           '274682038970482688': 'ReddlsRow', '130852537199886337': 'SenorTonto',\
           '134863783444086784': 'Spike/Chitoge','176147192719998977': 'Tachii',\
           '826618819191242792': 'Tedo','197085461624127488': 'Thaelon',\
           '396398521462554624': 'Foxcolt', '497120107819040768': 'Moon',\
           '355906565422841867':'Unihorn','579199616143327258': 'virant (Variant-1)',\
           '673517909125103619': 'WindaRB', '210041889414447105': 'Daedalus',\
           '281088989610377216': 'latvice','500124144755671040': 'mUmU',\
           '563082215198556211': 'zero00', '253994447782543361': '17maple',\
           '465942228791984149':'GonBu', '123456789': 'aile', '189350494328586240': 'PlainDoe',\
           '215506389353758720': 'Zerefsis', '292615553942683648': 'Tympest',\
           '394763425777057794': 'Tatumi', '187764065131560960': 'leafa',\
           '323444581033050113': 'Firis', '218659635513524224': 'Ciaosuh',\
           '506124628188594181':'donuts', '961291207210856448':'fiE',\
           '560576301149192203':'mantis', '238091448073846784':'rocketeer',\
           '847443895327785030':'esyw','332846967971512322':'RenTrout'}

#creates a dicitonary with each id from id_name and the value is default slime number 0
AGE_members = {}
for x in id_name:
    AGE_members[x] = 0


# HELPER METHODS #

#helper method, takes in member id and the number of slimes want to be added
#can use negative numbers to subtract slimes
def add_slime(member_id, number):
    if member_id in db:  #if member id already in replit database,
        slime_count = db[member_id]
        slime_count += int(number)
        db[member_id] = slime_count
    else:  #if member id was not in replit database
        db[member_id] = 1


#helper method, knowing this member id is already in db, subtract one slime count
def minus_slime(member_id):
    slime_count = db[member_id]
    slime_count -= 1
    db[member_id] = slime_count


#helper method, in case there are multiple greatest key-value pairs with the same value
def multiple_max(dictionary):
    max_key = max(dictionary, key=dictionary.get)
    first = [max_key]

    for x in dictionary:
        if x != max_key:
            if dictionary[x] == dictionary[max_key]:
                first += [x]
    return first


#check whether the author's id is the same as the specified user's id
def is_bot_admin(ctx):
    return ctx.author.id == 253994447782543361
def is_slime_admin(ctx):
    return ctx.author.id in (253994447782543361, 315112026093649920)


#check whether it's in the specified channel
def in_slime_channel(ctx):
    return ctx.channel.id in (887894832708730881, 887967982356148254)


#return formatted timestamp
def utcTimestamp():
    return f'{datetime.utcnow().replace(microsecond=0).isoformat()}Z'


#error handler helper
def handleError(e):
  try:
    logname = f'log/{utcTimestamp()}.txt'
    with open(f'{logname}', 'w') as outfile:
        outfile.write(f'# TRACE:\n{traceback.format_exc()}')
    sendWebhook(f'Klee encountered an error :( Please check {logname} <@253994447782543361> <@579199616143327258>\nStatus page: https://1122022-slime-bot-for-dc.tonycen.repl.co/')
  except Exception as err:
    print(f'{utcTimestamp()} ERROR in handleError(): {err}')


#helper to call discord webhook API
def sendWebhook(msg):
    webhookUrl = 'https://discord.com/api/webhooks/' + os.getenv('WEBHOOK_ID_TOKEN')
    r = requests.post(webhookUrl, data = {'content': msg})
    print(f'{utcTimestamp()} DEBUG Webhook response code: {r.status_code}')
    r.raise_for_status() #raise error if response status_code is 4XX or 5XX


# BOT EVENTS #

#gets the bot online
@client.event
async def on_ready():
  try:
    await client.change_presence(status = discord.Status.online, \
                        activity = discord.Game(f'counting slimes since {utcTimestamp()} (UTC)'))
    print(f'{utcTimestamp()} INFO Bot is ready.')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in on_ready(): {err}')
    handleError(err)


@client.event
async def on_command_error(ctx, error):
  try:
    if ctx.channel.id == 887894832708730881:
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Klee does not know this command... ヾ(⌒(_´･ㅅ･`)_ ')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Klee does not know this name... ヾ(⌒(_´･ㅅ･`)_ ')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in on_command_error(): {err}')
    handleError(err)


#listens to @ultra role mention
@client.listen('on_message')
async def message(message):
  try:
    if message.author == client.user:  #make sure is not responding to message from the bot
        return
    if message.channel.id == 887894832708730881:  #make sure the @ is from the right channel

        if ('<@&887894985398157363>') in message.content or (
                '<@&887915507804692511>') in message.content:

            if len(message.raw_mentions) != 0:
                member_id = str(message.raw_mentions[0])

                add_slime(member_id, 1)
                await message.channel.send(
                    f'Woah! It is a slime!  (ﾉ>ω<)ﾉ  Klee has counted {db[member_id]} slimes for {id_name[member_id]}!'
                )

            elif (message.content.split()[1].lower()
                  == 'me') or ('me' in message.content.split()[1].lower()):
                member_id = str(message.author.id)

                add_slime(member_id, 1)

                await message.channel.send(
                    f'Woah! It is a slime!  (ﾉ>ω<)ﾉ  Klee has counted {db[member_id]} slimes for {id_name[member_id]}!'
                )

            else:
                name_mentioned = message.content.split()[1]

                member_id = 0

                if name_mentioned.lower() == 'dan':
                    member_id = str(name_id['Dan'])
                elif name_mentioned.lower() == 'moon':
                    member_id = str(name_id['Moon'])
                else:
                    for x in name_id:
                        if name_mentioned.lower() in x.lower():
                            member_id = str(name_id[x])

                if member_id == 0:
                    await message.channel.send(
                        'Uh, Klee does not know this name, and therefore cannot add this slime to anyone...'
                    )
                    return

                add_slime(member_id, 1)

                await message.channel.send(
                    f'Woah! It is a slime!  (ﾉ>ω<)ﾉ  Klee has counted {db[member_id]} slimes for {id_name[member_id]}!'
                )

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in message(): {err}')
    handleError(err)


# BOT COMMANDS #

#method name doubleping, simply wrapper for minus_slime
@client.command()
async def doubleping(ctx, *, member):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

        if (member.lower() == 'me') or ('me' in member.lower()):
            member_id = str(ctx.message.author.id)

            minus_slime(member_id)

        else:
            name_mentioned = member

            member_id = 0

            if name_mentioned.lower() == 'dan':
                member_id = str(name_id['Dan'])
            elif name_mentioned.lower() == 'moon':
                member_id = str(name_id['Moon'])
            else:
                for x in name_id:
                    if name_mentioned.lower() in x.lower():
                        member_id = str(name_id[x])

            if member_id == 0:
                await ctx.send(
                    'Uh, Klee does not know this name, and therefore cannot subtract this slime from anyone...'
                )
                return

            minus_slime(member_id)

        await ctx.send(
            f'Klee has subtracted a slime from {id_name[member_id]}! The number of slimes {id_name[member_id]} has summoned has gone from {int(db[member_id])+1} to {db[member_id]}'
        )
        return

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in doubleping(): {err}')
    handleError(err)


@client.command()
async def total(ctx):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

        #gets db.keys from db and store in dictionary named member_count
        member_count = db.keys()

        total = 0
        for member_id in member_count:  #for loop to get slime counts(values) of each member_id(key)
            slime_count = db[member_id]
            total += slime_count

        await ctx.send(
            f'For the current season, Ultra has {len(id_name)} members with 3 Altras, and we have summoned {total} slimes so far! Dear RNG God, please help us summon more slime! ٩(๑•̀ω•́๑)۶'
        )

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in total(): {err}')
    handleError(err)


#only accessible by me and gunther
#returns who are in first, second and third in slime spawns for the current season
@client.command()
@commands.check(is_slime_admin)
async def first(ctx):  #change to AGE_members
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

        member_count = db.keys()
        dictionary = {}
        for member_id in member_count:
            dictionary[member_id] = db[member_id]

        copy = dict(dictionary)

        first = multiple_max(copy)

        copy1 = dict(dictionary)
        for x in copy1:
            for y in first:
                if x == y:
                    del copy[x]

        second = multiple_max(copy)

        copy2 = dict(copy1)
        for x in copy2:
            for y in second:
                if x == y:
                    del copy[x]

        third = multiple_max(copy)

        first_name = []
        for x in first:
            first_name += [id_name[x]]

        second_name = []
        for y in second:
            second_name += [id_name[y]]

        third_name = []
        for z in third:
            third_name += [id_name[z]]

        await ctx.send(
            f'The current first is {first_name} with {db[x]} slimes! Second is {second_name} with {db[y]} slimes, and third is {third_name} with {db[z]} slimes! They are the best! ⁽⁽٩(๑˃̶͈̀ ᗨ ˂̶͈́)۶⁾⁾'
        )

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in first(): {err}')
    handleError(err)


#sends the specific person the entire replit db, each person with their slime counts
@client.command()
@commands.check(is_slime_admin)
async def member_total(ctx, user_id):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
        target = await client.fetch_user(user_id)
        message = job()

        await target.send(f'{message}')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in member_total(): {err}')
    handleError(err)


#helper method
def job():
    message = {}

    member_count = db.keys()
    for x in AGE_members:
        for y in member_count:
            if x == y:  #if both ids match
                AGE_members[x] = db[
                    y]  #utilize the AGE_members dictionary created in the earlier lines
                #store the values from the replit db as the values for the AGE_members dictionary

    for x in AGE_members:  #creates key-value pairs with key being the player name from id_name
        #and values being slime counts
        message[id_name[x]] = AGE_members[x]

    return message


#use to check number of slime counts for self
@client.command()
async def sself(ctx):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
        self_member_id = str(ctx.author.id)
        await ctx.send(
            f'Klee knows that you have summoned {db[self_member_id]} slimes so far this season! You are the best!'
        )

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in sself(): {err}')
    handleError(err)


#use to get the approximate number of slimes summoned in the past 24 hours
#not working correctly
@client.command()
async def daily(ctx):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:

        current = datetime.now(timezone.utc)

        dayago = current - timedelta(days=1)

        counter = 0

        #the codes below do not work
        msg = discord.utils.get(await ctx.channel.history(limit=10))
        await ctx.send(msg)

        async for message in ctx.channel.history(limit=300,
                                                 after=dayago,
                                                 before=current):
            if ('<@&887894985398157363>') in message.content or (
                    '<@&887915507804692511>') in message.content or (
                        '@ULTRA') in message.content:
                counter += 1

        await ctx.send(
            f'Klee has counted hand by hand, in the past 24 hours, we have summoned {counter} slimes! ٩(๑❛ᴗ❛๑)۶ '
        )

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in daily(): {err}')
    handleError(err)


#wrapper for add_slime method
@client.command()
async def add(ctx, number, *, username):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
        member = username.strip()

        member_count = db.keys()
        dictionary = {}
        for member_id in member_count:
            dictionary[member_id] = db[member_id]

        if (member.lower() == 'me') or ('me' in member.lower()):
            member_id = str(ctx.message.author.id)

            if member_id in member_count:
                original = db[member_id]
                add_slime(member_id, number)
            else:
                original = 0
                db[member_id] = 1
        else:
            name_mentioned = member
            if name_mentioned.lower() == 'dan':
                member_id = str(name_id['Dan'])
            elif name_mentioned.lower() == 'moon':
                member_id = str(name_id['Moon'])
            else:
                for x in name_id:
                    if str(name_mentioned.lower()) in x.lower() or str(
                            name_mentioned.lower()) == x.lower():
                        member_id = str(name_id[x])

            if member_id in member_count:
                original = db[member_id]
                add_slime(member_id, number)

            else:
                original = 0
                db[member_id] = 1
        await ctx.send(
            f'Klee has added a slime to {id_name[member_id]}! The number of slimes {id_name[member_id]} has summoned has gone from {original} to {db[member_id]}'
        )

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in add(): {err}')
    handleError(err)


#method for sending no-talking gif
@client.command()
async def gif(ctx):
  try:
    if ctx.channel.id == 887894832708730881:
        embed = discord.Embed(title='Channel not for talking',
                              color=discord.Colour.blue())
        embed.set_image(
            url='https://c.tenor.com/EwX63Uf2_x0AAAAC/sml-jackie-chu.gif')
        await ctx.send(embed=embed)

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in gif(): {err}')
    handleError(err)


#only allows me and gunther to clear slime records (by setting slime counts to 0)
@client.command()
@commands.check(is_slime_admin)
async def clear(ctx):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
        member_count = db.keys()
        for member_id in member_count:
            db[member_id] = 0
        await ctx.send('slime record cleared')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in clear(): {err}')
    handleError(err)


#command to restart bot to try to reclaim new IP. WIP, not working yet.
@client.command()
async def restart(ctx):
  try:
    if ctx.channel.id == 887894832708730881 or ctx.channel.id == 887967982356148254:
        print(f'{utcTimestamp()} INFO restart() is initiated...?')
        await ctx.send('command accepted, but Klee does not know what to do with this command... ヾ(⌒(_´･ㅅ･`)_ ')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in restart(): {err}')
    handleError(err)


#test bot response
@client.command()
@commands.check(in_slime_channel)
async def ping(ctx):
  try:
    await ctx.send('pong!')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in ping(): {err}')
    handleError(err)


# TASKS #

#for a time loop, sends out the dictionary representing the replit db with names and slime counts
@tasks.loop(hours=12)
async def called_once_every12hour():
  try:
    message_channel = client.get_channel(950051638075334686)
    #print(f'Got channel {message_channel}')
    message = job()
    timestamp = datetime.now(timezone.utc)
    await message_channel.send(f'UTC time: {timestamp}, slime record{message}')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in called_once_every12hour(): {err}')
    raise err


@called_once_every12hour.before_loop
async def before():
  try:
    await client.wait_until_ready()
    #print('Finished waiting')

  except Exception as err:
    print(f'{utcTimestamp()} ERROR in called_once_every12hour.before_loop(): {err}')
    raise err


# INIT PART 2 #

# Scheduled task for #daily-slime-results
called_once_every12hour.start()

# Run simple web server to be called by uptime-robot. See: keep_alive.py
keep_alive()

# Initialize discord bot
try:
    client.run(os.getenv('TOKEN'))
except Exception as err:
    print(f'{utcTimestamp()} ERROR on client.run(): {err}')
    print(f'{utcTimestamp()} ERROR initializing discord bot.')
    handleError(err)


# END #
