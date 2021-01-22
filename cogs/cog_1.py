from discord.ext import commands


class CogOne(commands.Cog):
    def __init__(self, client):
        """Instantiates a CypherSystem object.
        Args:
            client (discord.ext.commands.Bot): The bot the Class/Cog is being
                added to.
        """
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        """Logs that the bot is logged in and ready.
        """
        print(f'Bot logged on as {self.client.user}')

    @commands.command()
    async def hello(self, ctx):
        username = str(ctx.message.author)
        message = f'Hello {username}!'
        await ctx.message.channel.send(message)


def setup(client):
    """Allows a Bot from discord.ext.commands to add Utilities as a cog.
    Args:
        client (discord.ext.commands.Bot): The bot to add the Cog to.
    """
    client.add_cog(CogOne(client))
