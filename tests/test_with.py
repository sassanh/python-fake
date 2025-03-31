"""Test `Fake` instance being used in a `with` statement."""

import asyncio

from fake.fake import Fake


def test_with() -> None:
    """Test `Fake` instance being used in a `with` statement."""
    x = Fake()

    with x as y:
        assert isinstance(y, Fake)
        assert y is x


def test_async_with() -> None:
    """Test `Fake` instance being used in an async `with` statement."""
    x = Fake()

    async def check() -> None:
        async with x as y:
            assert isinstance(y, Fake)
            assert y is x

    asyncio.run(check())
