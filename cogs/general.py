from discord import Embed, Permissions

from discord.ext import commands
from discord.utils import oauth_url


class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=["invite"])
    async def links(self, ctx):
        permission_names = (
            "administrator",
        )
        perms = Permissions()
        perms.update(**dict.fromkeys(permission_names, True))
        embed = Embed(
            description= # Other links can be included here, such as a home server link or a github repo
f"""[**Bot Invite Link**]({oauth_url(self.bot.user.id, perms)})""",
            color=0x00A9E0)
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.reply(embed=embed)


def setup(bot):
    bot.add_cog(General(bot))