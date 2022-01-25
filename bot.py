import hikari
import os
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.mozambiquehe.re/games?auth=5platform="
uid = 1011580145761
apex_token = os.environ.get('apex_token')

def get_apex_info():
    data = requests.get(f'{base_url}{apex_token}&uid={uid}')
    print(data.text)

token = os.environ.get('discord_token')
"""
bot = hikari.GatewayBot(token=token)

@bot.listen()
async def ping(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    
    if event.content.startswith("hk.ping"):
        await event.message.respond("Pong!")

bot.run()
"""

get_apex_info()