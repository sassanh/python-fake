"""Test general usage of `Fake`."""

import asyncio

from fake import Fake


def test_general() -> None:
    """Test general usage of `Fake`."""
    x = Fake(
        _Fake__props={
            'some_prop': Fake(
                _Fake__return_value=Fake(
                    _Fake__await_value='result',
                ),
            ),
        },
    )

    async def check() -> None:
        assert await x.some_prop()

    asyncio.run(check())
