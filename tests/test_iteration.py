"""Test iteration over `Fake` instances."""

import asyncio

from fake.fake import Fake


def test_iteration() -> None:
    """Test `Fake` instance being iterable."""
    x = Fake()
    counter = 0
    for i in x:
        assert isinstance(i, Fake)
        counter += 1
    assert counter == 1

    counter = 0
    for i in x:
        assert isinstance(i, Fake)
        counter += 1
    assert counter == 1


def test_iteration_with_length() -> None:
    """Test `Fake` instance with length being iterable."""
    x = Fake(_Fake__length=3)
    counter = 0
    for i in x:
        assert isinstance(i, Fake)
        counter += 1

    assert counter == 3

    counter = 0
    for i in x:
        assert isinstance(i, Fake)
        counter += 1

    assert counter == 3


def test_iteration_with_list() -> None:
    """Test `Fake` instance set with a list being iterable."""
    x = Fake(_Fake__list=[2, 1, 0])
    counter = 0
    for i in x:
        assert not isinstance(i, Fake)
        assert i == 2 - counter
        counter += 1

    assert counter == 3

    counter = 0
    for i in x:
        assert not isinstance(i, Fake)
        assert i == 2 - counter
        counter += 1

    assert counter == 3


def test_iteration_with_iter() -> None:
    """Test `Fake` instance set with an iterator being iterable."""
    x = Fake(_Fake__iter=iter([2, 1, 0]))
    counter = 0
    for i in x:
        assert not isinstance(i, Fake)
        assert i == 2 - counter
        counter += 1

    assert counter == 3


def test_async_iteration_with_iter() -> None:
    """Test `Fake` instance set with an iterator being iterable."""
    x = Fake(_Fake__iter=iter([2, 1, 0]))

    async def check() -> None:
        counter = 0
        async for i in x:
            assert not isinstance(i, Fake)
            assert i == 2 - counter
            counter += 1

        assert counter == 3

    asyncio.run(check())
