import hikari
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get('discord_token')

bot = hikari.GatewayBot(token=token)

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    
    if event.content.startswith("hk.ping"):
        await event.message.respond("Pong!")

bot.run()