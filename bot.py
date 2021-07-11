import logging
from os import getcwd, getenv

from discord import Intents, AllowedMentions
from dotenv import load_dotenv

from discord.ext import commands


logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)

load_dotenv(getcwd()+"/.env")
DEFAULT_PREFIX = getenv("DEFAULT_PREFIX")


bot = commands.Bot(
    command_prefix=DEFAULT_PREFIX, 
    intents=Intents.default(), 
    case_insensitive=True, 
    allowed_mentions=AllowedMentions(
        everyone=False,
        roles=False,
        replied_user=False
    )
)

initial_cogs = [
    "jishaku",
    "cogs.error_handler",
    "cogs.general"
]

for cog in initial_cogs:
    try:
        bot.load_extension(cog)
        logging.info(f"Successfully loaded {cog}")
    except Exception as e:
        logging.error(f"Failed to load cog {cog}: {e}")


@bot.event
async def on_ready():
    logging.info(f"Bot has successfully launched as {bot.user}")

@bot.before_invoke
async def before_invoke(ctx):
    logging.info(f"Invoked {ctx.command} in {ctx.guild.name} by {ctx.author.name}\nArgs: {ctx.args}")

@bot.after_invoke
async def after_invoke(ctx):
    logging.info(f"Concluded {ctx.command}")


bot.run(getenv("TOKEN"))
