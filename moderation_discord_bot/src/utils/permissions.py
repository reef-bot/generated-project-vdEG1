import discord
from discord.ext import commands

def has_permissions():
    async def predicate(ctx):
        # Check permissions logic
        return True
    return commands.check(predicate)