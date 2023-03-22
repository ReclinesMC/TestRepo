#Import requirements.
import discord
from discord.ext import commands

#Define the cog.
class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Ping command to make sure the bot is running.
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    #Clear command to clear messages from chat.
    @commands.command()
    async def clear(self, ctx, amount: int = 0, member: discord.Member = None):
        if amount is None:
            await ctx.send("Please specify a positive number of messages to clear.")
            return

        def check_user(message):
            return message.author == member if member else True

        deleted = await ctx.channel.purge(limit=amount + 1, check=check_user)  # +1 to include the clear command message
        await ctx.send(f"Cleared {len(deleted) - 1} messages", delete_after=5)  # -1 to exclude the clear command message


#Load the cog to the bot.
async def setup(bot):
    await bot.add_cog(Utility(bot))