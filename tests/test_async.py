"""Test `Fake` behaving as different async objects."""

from __future__ import annotations

import asyncio
from typing import Coroutine

import pytest

from fake import Fake


def test_awaitable() -> None:
    """Test `Fake` behaving as an awaitable."""
    x = Fake()

    async def check() -> None:
        assert isinstance(await x(), Fake)
        assert isinstance(await x, Fake)

    asyncio.run(check())


@pytest.mark.xfail
def test_coroutine() -> None:
    """Test `Fake` being and instance of `Coroutine`."""
    x = Fake()

    assert isinstance(x, Coroutine)
