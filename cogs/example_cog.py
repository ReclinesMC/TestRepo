#Import requirements.
import discord
from discord.ext import commands

#Define the cog.
class Example_Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#Commands here.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

#Load the cog to the bot.
async def setup(bot):
    await bot.add_cog(Example_Cog(bot))