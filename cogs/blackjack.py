import discord
import random
from discord.ext import commands

class BlackjackCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def get_card_value(self, card):
        if card in ['J', 'Q', 'K']:
            return 10
        elif card == 'A':
            return 11
        else:
            return int(card)

    @commands.command()
    async def blackjack(self, ctx):
        player_hand = random.sample(self.cards, 2)
        dealer_hand = random.sample(self.cards, 2)

        player_points = sum(map(self.get_card_value, player_hand))
        dealer_points = sum(map(self.get_card_value, dealer_hand))

        await ctx.send(f'You got: {", ".join(player_hand)} (Total: {player_points})')
        await ctx.send(f'Dealer got: {dealer_hand[0]}, X')

        if player_points == 21:
            await ctx.send('Congratulations! You got a blackjack!')
            return

        action = await ctx.send('What would you like to do? Type `hit` or `stand`.')
        def check(m):
            return m.author == ctx.author and m.content.lower() in ['hit', 'stand']

        try:
            message = await self.bot.wait_for('message', check=check, timeout=30)
        except asyncio.TimeoutError:
            await ctx.send('Sorry, you took too long to respond. The game has ended.')
            return

        if message.content.lower() == 'hit':
            new_card = random.choice(self.cards)
            player_hand.append(new_card)
            player_points += self.get_card_value(new_card)
            await ctx.send(f'You got: {new_card} (Total: {player_points})')

            if player_points > 21:
                await ctx.send('You busted! Dealer wins.')
                return
            elif player_points == 21:
                await ctx.send('Congratulations! You got a blackjack!')
                return

        await ctx.send(f'Dealer reveals their card: {dealer_hand[1]} (Total: {dealer_points})')

        if dealer_points > player_points:
            await ctx.send('Dealer wins!')
        elif dealer_points < player_points:
            await ctx.send('You win!')
        else:
            await ctx.send('It\'s a tie!')

async def setup(bot):
    await bot.add_cog(BlackjackCog(bot))