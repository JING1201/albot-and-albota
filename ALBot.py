import discord
from discord.utils import get
from discord.ext import commands
import config

'''Cogs to load when the bot first starts'''
startup_cogs = [
    "cogs.helloworld",
    "cogs.memes",
    "cogs.projects"
]

bot = commands.Bot(command_prefix="!", description="ALBot (A Lame Bot)", case_insensitive=True)

@bot.event
async def on_ready():
    """Print the bots information on connect"""
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    await bot.change_presence(activity=discord.Game(name="Destroying propritary software"))

@bot.command()
async def load(ctx, extension_name : str):
    """Loads an extension."""
    try:
        if extension_name.startswith("cogs."):
            bot.load_extension(extension_name)
        else:
            bot.load_extension("cogs." + extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} loaded.".format(extension_name))

@bot.command()
async def unload(ctx, extension_name : str):
    """Unloads an extension."""
    if extension_name.startswith("cogs."):
        bot.unload_extension(extension_name)
    else:
        bot.unload_extension("cogs." + extension_name)
    await ctx.send("{} unloaded.".format(extension_name))

@bot.command()
async def reload(ctx, extension_name : str):
    '''Unloads and then loads an extension'''
    try:
        if extension_name.startswith("cogs."):
            bot.unload_extension(extension_name)
            bot.load_extension(extension_name)
        else:
            bot.unload_extension("cogs." + extension_name)
            bot.load_extension("cogs." + extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await ctx.send("{} reloaded.".format(extension_name))

if __name__ == "__main__":
    for extension in startup_cogs:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.ALBOT_TOKEN)