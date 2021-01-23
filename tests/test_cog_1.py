from unittest.mock import AsyncMock

from discord.ext import commands
import pytest

from cogs.cog_1 import CogOne


@pytest.fixture
def cog():
    # You may need to change the command_prefix
    client = commands.Bot(command_prefix='/')
    return CogOne(client)


@pytest.fixture
def ctx():
    mock = AsyncMock()
    mock.message.author = 'User'
    return mock


@pytest.fixture
def self():
    """It appears you need to mock self for methods decorated with
    @commands.Command(). Will need to research how the decorator and class are
    working together to pass self."""
    return AsyncMock()


@pytest.mark.asyncio
async def test_hello(self, cog, ctx):
    await cog.hello(self, ctx)

    ctx.message.channel.send.assert_called_once_with('Hello User!')
