import discord
from discord.ext import commands
from utils.permissions import has_permissions

@commands.command()
@has_permissions()
async def kick(ctx, member: discord.Member):
    # Kick member logic
    pass