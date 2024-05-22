import discord
from discord.ext import commands
from utils.permissions import has_permissions

@commands.command()
@has_permissions()
async def ban(ctx, member: discord.Member):
    # Ban member logic
    pass