### Lib ###
import aiohttp, discord
from discord.ext import commands

### Config ###
BOT_TOKEN = '' #Required, ATTIVA GLI INTENTS DAL DISCORD DEVELOPER PORTAL / ACTIVATE INTENTS FROM THE DISCORD DEVELOPER PORTAL https://cdn.discordapp.com/attachments/1042473036407910410/1079046390115741806/image.png
ERRORCOLOR = 0xff0000
DONECOLOR = 0x00ff2e

class RaidCleanerBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '!',intents = discord.Intents.all(),case_insensitive=True)
        self.filecogs = ["cogs.antiraid"]

    async def setup_hook(self):
        self.sessione = aiohttp.ClientSession()
        for filedacaricare in self.filecogs: 
            await self.load_extension(filedacaricare)
        await self.tree.sync()
        print(f'{self.user} Syncato con successo!')

    async def close(self):
        await super().close()
        await self.sessione.close()

    async def on_ready(self):
        print(f'{self.user} Connesso con successo!')
        await bot.change_presence(activity=discord.Game(name=f"💖 By Mat#3616 - github.com/itsmat"))

### Bot ###
bot = RaidCleanerBot()
bot.remove_command('help')
bot.run(BOT_TOKEN)
