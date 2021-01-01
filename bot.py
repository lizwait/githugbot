import os # for importing env vars for the bot to use
import random
from tarot_deck import tarot_cards
from twitchio.ext import commands


bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL'],os.environ['CHANNEL2']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has arrived!")
    await ws.send_privmsg(os.environ['CHANNEL2'], f"/me has arrived!")

@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)   

    if 'hello' in ctx.content.lower():
        await ctx.channel.send(f"Oh hai, @{ctx.author.name}! <3 ")

    if 'hi' in ctx.content.lower():
        await ctx.channel.send(f"Oh hai, @{ctx.author.name}! <3 ")

    if 'yaas' in ctx.content.lower():
        await ctx.channel.send(f"YAAAAS! VirtualHug")

    if 'cat' in ctx.content.lower():
        await ctx.channel.send(f"/me mews")

@bot.command(name='twitter')
async def twitter(ctx):
    await ctx.send('Follow AuraSwap on Twitter for memes, cat pics, and to find out when she goes live! https://twitter.com/auraswap')  

@bot.command(name='caster')
async def caster(ctx):
    caster_name = ctx.content.split()
    await ctx.send(f'Show some love to this amazing caster! https://www.twitch.tv/{caster_name[1]}')

@bot.command(name='tarot')
async def tarot(ctx):
    tarot_pick = random.choice(tarot_cards)
    await ctx.send(f'Your card is {tarot_pick}')

@bot.command(name='coin')
async def coin(ctx):
    coin_flip = random.randint(1,2)
    result = ''
    if coin_flip == 1:
        result = "Heads Wins!"
    elif coin_flip == 2:
        result = "Tails Wins!"

    await ctx.send(f'{result}')

@bot.command(name='dice')
async def dice(ctx):
    await ctx.send('Roll a dice! Use !d4, !d6, !d8, !d10, !d12, !d20 to roll a dice of your choosing! Good luck! :) ')    

@bot.command(name='d4')
async def d4(ctx):
    d4_roll = random.randint(1,4)
    await ctx.send(f'You rolled a {d4_roll}!')

@bot.command(name='d6')
async def d6(ctx):
    d6_roll = random.randint(1,6)
    await ctx.send(f'You rolled a {d6_roll}!')

@bot.command(name='d8')
async def d8(ctx):
    d8_roll = random.randint(1,8)
    await ctx.send(f'You rolled a {d8_roll}!')

@bot.command(name='d10')
async def d10(ctx):
    d10_roll = random.randint(1,10)
    await ctx.send(f'You rolled a {d10_roll}!')    

@bot.command(name='d12')
async def d12(ctx):
    d12_roll = random.randint(1,12)
    await ctx.send(f'You rolled a {d12_roll}!')

@bot.command(name='d20')
async def d20(ctx):
    d20_roll = random.randint(1,20)
    await ctx.send(f'You rolled a {d20_roll}!')

@bot.command(name='uptime')
async def uptime(ctx):
    await ctx.send('Auraswap has been streaming for {}!')


if __name__ == "__main__":
    bot.run()