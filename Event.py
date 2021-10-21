import discord
from discord import commands
from core.classes import Cog_Extension
import os
import disnake

from disnake.ext import commands

class Event(Cog_Extension):
  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.content == 'food':
      await msg.channel.send('test')
    
def setup(bot):
  bot.add_cog(Event(bot))
