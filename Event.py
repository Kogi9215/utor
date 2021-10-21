import discord
from discord import commands
from core.classes import Cog_Extension
import os
import disnake

from disnake.ext import commands

clss Event(Cog_extension):
  @commands.Cog.listener()
  async def on_message(self,msg):
    if msg.author == '671366378351230996':
      await msg.channel.send('test')
    
def setup(bot):
  bot.add_cog(Event(bot))
