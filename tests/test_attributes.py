"""Test attributes of `Fake` instances."""

import pytest

from fake.fake import Fake


def test_get_attributes() -> None:
    """Test `Fake` instance having different random attributes with type `Fake`."""
    assert isinstance(Fake().x, Fake)
    assert isinstance(Fake().some_other_random_attribute, Fake)

    with pytest.raises(
        AttributeError,
        match=r"^module '' has no attribute '__real_attr'$",
    ):
        assert Fake()._Fake__real_attr  # noqa: SLF001


def test_file_attribute() -> None:
    """Test `Fake`'s `__file__` attribute behavior."""
    assert Fake().__file__ == 'fake'
    assert Fake(_Fake__file='some_file').__file__ == 'some_file'


def test_set_attributes() -> None:
    """Test `Fake` instance having different random attributes with type `Fake`."""
    x = Fake()

    x.some_attribute = 'some_value'
    assert isinstance(Fake().some_attribute, Fake)


def test_attrs() -> None:
    """Test `Fake`'s `__attrs` behavior."""
    x = Fake(_Fake__attrs={'special_attr': 'special_value'})

    assert not isinstance(x.special_attr, Fake)
    assert x.special_attr == 'special_value'
    assert isinstance(x.non_special_attr, Fake)
