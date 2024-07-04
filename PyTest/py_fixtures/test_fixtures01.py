import pytest

@pytest.fixture()
def setup_list():
    print("\n executing fixtures.. \n")
    city = ['Chennai', 'Delhi', 'Banglore', 'Mumbai', 'Kolkata', 'Coimbatore', 'Cochin']
    return city
@pytest.mark.run(order=1)
def test_getCity(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'Chennai'
    assert setup_list[::2] == ['Chennai', 'Banglore', 'Kolkata', 'Cochin']

def reverse_list(listValues):
    listValues.reverse()
    return listValues
@pytest.mark.run(order=2)
def test_reverseList(setup_list):
    assert setup_list[::-1] == reverse_list(setup_list)

@pytest.mark.run(order=3)
@pytest.mark.xfail(reason="userfixtures cannot use the fixture's return values")
@pytest.mark.usefixtures("setup_list")
def test_useFixtures():
    assert 1==1
    assert (setup_list[0]) == "Chennai"

