import discord 
from discord.ext import commands

class help_cog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.help_message = """
```
General commands:
+help - displays all commands
+play <keywords> - plays a song on youtube
+queue - displays the current music queue
+skip - skips the current song
+clear - Clears the queue
+disconnect - Disconnects the bot
+pause - Pauses the current song
+resume - Resumes playing the current song
```
"""
    self.text_channel_text = []
    
  @commands.Cog.listener()
  async def on_ready(self):
    print("Bot is Online")
    for guild in self.bot.guilds:
      for channel in guild.text_channels:
        self.text_channel_text.append(channel)

    await self.send_to_all(self.help_message)

  async def send_to_all(self, msg):
    for text_channel in self.text_channel_text:
      await text_channel.send(msg)
    
  @commands.command(name="help", aliases=["h"], help="Displays all the available commands.")
  async def help(self, ctx, *args):
    print('Used help command')
    await ctx.send(self.help_message)



async def setup(bot):
  await bot.add_cog(help_cog(bot))
    