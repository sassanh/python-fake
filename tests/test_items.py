"""Test items of `Fake` instances."""

from fake.fake import Fake


def test_get_item() -> None:
    """Test `Fake` instance having different random attributes with type `Fake`."""
    assert isinstance(Fake()[0], Fake)
    assert isinstance(Fake()[-1], Fake)
    assert isinstance(Fake()[42], Fake)
    assert isinstance(Fake()[-42:42], Fake)
    assert isinstance(Fake()[42:-42], Fake)


def test_set_item() -> None:
    """Test `Fake`'s `__items` behavior."""
    x = Fake()

    x[0] = 0
    x[-1] = 1
    x[42] = ''
    x[-42:42] = {}
    x[42:-42] = []

    assert isinstance(x[0], Fake)
    assert isinstance(x[42], Fake)


def test_items() -> None:
    """Test `Fake`'s `__items` behavior."""
    x = Fake(_Fake__items={'special_item': 'special_value'})

    assert x['special_item'] == 'special_value'
    assert not isinstance(x['special_item'], Fake)
    assert isinstance(x['non_special_item'], Fake)


def test_list() -> None:
    """Test `Fake`'s `__items` behavior."""
    x = Fake(_Fake__list=[2, 1, 0])

    for i in range(3):
        assert not isinstance(x[i], Fake)
        assert x[i] == 2 - i
