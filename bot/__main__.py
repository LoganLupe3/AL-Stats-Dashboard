import os
from re import L
from dotenv import load_dotenv

import hikari
import lightbulb
from apex_legends import ApexLegends

__version__ = "0.1.0"

load_dotenv()

apex = ApexLegends(os.environ.get('tracker_api'))
#test_player = apex.player("snoopar420weed")
#print(test_player)

bot = lightbulb.BotApp(
    os.environ['discord_token'],
    default_enabled_guilds = int(os.environ['GUILD_ID']),
    help_slash_command=True,
)

bot.load_extensions_from("./bot/extensions")

"""
@bot.listen(hikari.StartedEvent)
async def on_started(event: hikari.StartedEvent) -> None:
    await (await bot.rest.fetch_channel(STDOUT_CHANNEL_ID)).send("Online.")
"""


"""
    Ping Command

    Responds with the message "Pong"
"""
@bot.command()
@lightbulb.command("ping", "checks the bot is alive")
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx: lightbulb.Context) -> None:
    await ctx.respond("Pong!")

@bot.command
@lightbulb.option("text", "User to check stats")
@lightbulb.command("stats", "Gives the stats of the user")
@lightbulb.implements(lightbulb.SlashCommand)
async def stats(ctx: lightbulb.Context) -> None:
    #await ctx.respond(ctx.options.text)
    try:
        player = apex.player(ctx.options.text)
        #await ctx.respond(f'Stats for {ctx.options.text}:\n{player}')
        embed = (
            hikari.Embed(
                title = f'{ctx.options.text}\'s Stats',
                description = f'Displaying statistics for {ctx.options.text}',
                colour = ctx.member.accent_colour,
            )
            .set_author(name="Information")
            .set_footer(text=f'Requested by {ctx.member.display_name}',
                        icon = ctx.member.avatar_url,
            )
            .set_thumbnail(player.legends[0].icon)
            .add_field(name="Kills", value=player.kills)
            .add_field(name="Level", value=player.level)
            #.add_field(name="Damage", value=player.damage)
        )

        await ctx.respond(embed)
    except:
        await ctx.respond("User not found.")
    

if __name__ == "__main__":
    bot.run()