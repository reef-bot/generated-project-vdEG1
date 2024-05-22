import discord
from discord.ext import commands
from utils.permissions import has_permissions

@commands.command()
@has_permissions()
async def mute(ctx, member: discord.Member):
    # Mute member logic
    pass