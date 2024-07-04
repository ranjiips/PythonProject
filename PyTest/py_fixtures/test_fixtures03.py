import pytest


@pytest.mark.run(order=7)
def test_deleteItems(setup01):
    print(setup01)
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1

@pytest.mark.run(order=8)
def test_removeItems(setup02):
    print(setup02)
    setup02.remove("thur")
    print(setup02)
    assert setup02 == pytest.weekdays2
