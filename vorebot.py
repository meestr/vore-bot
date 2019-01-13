import asyncio
import datetime
import random
import discord



"""
Why the fuck would I ever agree to make this LOL

Timestamps were available in the Message object in the first revision, but they stopped working

also the log file var was never used because IT NEVER FUCKING WORKS
any with blocks wouldn't have worked 
"""



client = discord.Client()
log = open("log.txt", "w")
vore_responses = ['is a fucking degenerate', 'has weird fetishes', 'said vore!! ?? ? ?', 'said vore',
                  'is probably a furry', 'is definitely a furry', 'deserves death', 'needs to die']
vore_counts = 800   # before I found a good hosting place kek


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="I see your sins. Do not try resisting."))
    print("""

       .__                                    .__                   .___
  ____ |  |__    ___  _____________   ____    |  |   ___________  __| _/
 /  _ \|  |  \   \  \/ /  _ \_  __ \_/ __ \   |  |  /  _ \_  __ \/ __ | 
(  <_> )   Y  \   \   (  <_> )  | \/\  ___/   |  |_(  <_> )  | \/ /_/ | 
 \____/|___|  /    \_/ \____/|__|    \___  >  |____/\____/|__|  \____ | 
            \/                           \/                          \/ 

""")
    await asyncio.sleep(1.5)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("BOT USER: {}".format(client.user))
    print("STARTED AT {}".format(datetime.datetime.now()))
    log.write("INITIALIZED AT {} AS {}".format(datetime.datetime.now(), client.user))


@client.event
async def on_message(message):
    if client.user == message.author:
        return None
    a = str(message.content.lower())
    if "vore" in a:
        global vore_counts
        global vore_responses
        alist = a.split()
        vore_in_message = 0
        for item in alist:
            if "vore" in item:
                vore_in_message += 1
        if vore_in_message == 1:
            vore_counts += 1
            return await client.send_message(message.channel, "{}! {}! FUCK yOU !!! kys Now ! The vore counter is now at {}!!!!!!!! FUCK YOU BYE".format(message.author.mention, random.choice(vore_responses), vore_counts))
        if vore_in_message <= 5:
            vore_counts += vore_in_message
            return await client.send_message(message.channel, "{}. you FUCKIGN RETARD!!! WHAT THE FUCK QWHERE YOUTHINKIGN????? YOU SAIFD VORE FUCKING {} TIME S YOU RETARD!!! GOD THE COUNTERS NOW AT {}!!!!!!! FUCK YOUY!!!!! aaaaaaaaaaAAAAAAAAAAAAAAAAAAA".format(message.author.mention, vore_in_message, vore_counts))
        if vore_in_message >= 5:
            vore_counts += vore_in_message
            return await client.send_message(message.channel, "...{} do you have any idea what you've doing? YOU COULD HAVE OPENED A HOLE IN THE VORETIME CONTINUIM?? DO YOU REALIZE WHAT YOU JUST FUCING DID??? YOU COULD HAVE KILLED US ALL!!! Good thing that your message didnt have over 100 mentions of vore. Anyway")
#TODO: FINISH LATER LOL

@client.event
async def on_server_join(server):
    await client.send_message(server.owner, "HEy!! thanks for adding OH VORE LORD!!!(in {}) "
                                            "yOur tallies are now Being registered!! WOwZA!".format(server.name))

# bot made by meestr#3497 (im sorry)
