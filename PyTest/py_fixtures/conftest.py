import pytest
import os
def pytest_configure():
    pytest.weekdays1=['mon','tue','wed']
    pytest.weekdays2=['fri','sat','sun']
    pytest.weekdays3=['mon','tue','wed','thur','fri','sat','sun']
    pytest.filename = "../sample.txt"
    pytest.content = "Writing content in file"

@pytest.fixture(scope="module")
def setup01():
    wk1 = pytest.weekdays1.copy()
    wk1.append('thur')
    yield wk1
    print("\n Fixture setup closing")
    # wk1.pop()

@pytest.fixture()
def setup02():
    wk2 = pytest.weekdays2.copy()
    wk2.insert(0,'thur')
    yield wk2

@pytest.fixture()
def setup03():
    f = open(pytest.filename,'w')
    f.write(pytest.content)
    f.close()
    f = open(pytest.filename, 'r+')
    yield f
    f.close()
    os.remove(pytest.filename)

@pytest.fixture()
def setup():
    print("\nSetup - Execute before each test methods")
    yield
    print("Tear Down - Execute after each test methods")

