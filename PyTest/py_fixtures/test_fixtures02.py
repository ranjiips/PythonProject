import os

import pytest

weekdays1=['mon','tue','wed']
weekdays2=['fri','sat','sun']
weekdays3=['mon','tue','wed','thur','fri','sat','sun']
filename = "../sample.txt"
content = "Writing content in file"

@pytest.fixture()
def setup01():
    wk1 = weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print("\n After yield in setup01 Fixture")
    wk1.pop()

@pytest.fixture()
def setup02():
    wk2 = weekdays2.copy()
    wk2.insert(0,'thur')
    yield wk2

@pytest.fixture()
def setup03():
    f = open(filename,'w')
    f.write(content)
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)


@pytest.mark.run(order=4)
def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == weekdays3

@pytest.mark.run(order=5)
def test_len(setup02):
    assert len(weekdays1+setup02) == len(weekdays3)

@pytest.mark.run(order=6)
def test_readFile(setup03):
    filecontent = setup03.readline()
    assert filecontent==content
