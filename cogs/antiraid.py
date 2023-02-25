import discord
import datetime
from datetime import datetime
import pytz
from pytz import timezone
from discord.ext import commands
from discord import app_commands

class AntiRaid(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("AntiRaid online.")

    @commands.hybrid_command(name = 'raidclean', with_app_command = True, description='Elimina i canali di un raid') 
    @app_commands.describe(data = "Giorno del raid GIORNO-MESE-ANNO.")
    @app_commands.describe(orario = "Orario del raid ORA:MINUTI.")
    @app_commands.default_permissions(manage_guild = True)
    @app_commands.checks.bot_has_permissions(manage_channels = True)
    async def raidclean(self, ctx, data, orario):
        await ctx.send('Attendere...')
        data = datetime.strptime(data+" "+orario, "%d-%m-%Y %H:%M")
        differenza = datetime.now(timezone('Europe/London')).hour - datetime.now().hour
        data = data.replace(hour=differenza+data.hour, tzinfo=timezone('Europe/London'))
        canalieliminati = 0
        for channel in ctx.guild.channels:
            if channel.created_at > data: #se la stanza è stata creata dopo la data del raid viene eliminata
                await channel.delete()
                canalieliminati += 1
        await ctx.send(f'''**Tutti i canali creati dopo il {data.day}/{data.month} alle ore {data.hour}:{data.minute} sono stati eliminati con successo ({canalieliminati})**''')   

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AntiRaid(bot))