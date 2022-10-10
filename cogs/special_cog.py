import discord 
from discord.ext import commands

class special_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  
  @commands.is_owner()
  @commands.command(name="scatter", aliases=["ccq"])
  async def shutdown(self, bot):
      await bot.send(":saluting_face:")
      await bot.bot.close()


async def setup(bot):
  await bot.add_cog(special_cog(bot))
    