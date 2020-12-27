import os # for importing env vars for the bot to use
from twitchio.ext import commands

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")

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


@bot.command(name='twitter')
async def twitter(ctx):
    await ctx.send('Follow AuraSwap on Twitter for memes, cat pics, and to find out when she goes live! https://twitter.com/auraswap')  

@bot.command(name='caster')
async def caster(ctx):
    caster_name = ctx.content.split()
    await ctx.send(f'Show some love to this amazing caster! https://www.twitch.tv/{caster_name[1]}')

if __name__ == "__main__":
    bot.run()