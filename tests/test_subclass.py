"""Test subclasses of `Fake` class."""

from fake.fake import Fake


class _X(Fake): ...


def test_is_subclass() -> None:
    """Test subclasses of `Fake` also being fake."""
    assert isinstance(_X(), Fake)
