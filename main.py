import discord
import dotenv
import os

dotenv.load_dotenv()

bot = discord.Client(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("ready")
    guild = bot.get_guild(1555233329455038464)
    channel = guild.get_channel(1555233332479000607)
    await channel.send("golden pukeko is running")

@bot.event
async def on_reaction_add(reaction, user):
    evil_reactions = 0
    evil_reactors = []
    for reaction in reaction.message.reactions:
        print(reaction.emoji)
        if reaction.emoji in ["🇳", "🇮", "🇬", "🇦", "🇪", "🇷"]:
            evil_reactions += 1
            async for user in reaction.users():
                print(user, user.id)
                if user.id not in evil_reactors:
                    evil_reactors.append(user.id)
    if evil_reactions == 4:
        await reaction.message.channel.send("He was whipping up EVIL in a kettle!!")
        guild = bot.get_guild(1555233329455038464)
        for evil_reactor in evil_reactors:
            await guild.ban(guild.get_member(evil_reactor))
            print(f"banned {guild.get_member(evil_reactor)}!!")

bot.run(os.getenv("TOKEN"))