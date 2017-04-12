import discord
import logging
import asyncio
from playlist import Music
from discord.ext.commands import Bot
from discord import opus
from discord.client import Client
from discord.channel import Channel
from discord.enums import ChannelType
from test.test_trace import my_file_and_modname
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
my_bot = Bot(command_prefix="!")
voice_id = "300877947080802304"
my_bot.add_cog(Music(my_bot))

# @my_bot.command()
# async def join():
#     channel = my_bot.get_channel(voice_id)
#     await my_bot.join_voice_channel(channel)
#     return await my_bot.say("Joined")
@my_bot.command()
async def start():
    await my_bot.say("Morning fellas")
    await my_bot.login("MzAwODc4NDI5MDczNDQwNzY4.C89iMA.58LhgZOJLppVOOH4vGJBGTlGvtU")
@my_bot.command()
async def kys():
    await my_bot.say("Bye fgts")
    await my_bot.logout()
@my_bot.command()
async def print_channels():
    print([x.id for x in my_bot.get_all_channels()])
    
@my_bot.event
async def on_ready():
    print('Connected!')
    print('Username: ' + my_bot.user.name)
    print('ID: ' + my_bot.user.id)
    
@my_bot.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{1.content}'
    await my_bot.send_message(after.channel, fmt.format(after, before))
@my_bot.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await my_bot.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@cool.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await my_bot.say('Yes, the bot is cool.')
@my_bot.event
async def on_message_delete(message):
    fmt = '{0.author.name} has deleted the message:\n{0.content}'
    await my_bot.send_message(message.channel, fmt.format(message))
# @my_bot.command()
# async def play():
#     print([x.id for x in my_bot.get_all_channels()])
my_bot.run("MzAwODc4NDI5MDczNDQwNzY4.C89iMA.58LhgZOJLppVOOH4vGJBGTlGvtU")