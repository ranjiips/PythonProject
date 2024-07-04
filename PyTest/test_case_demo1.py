import pytest

@pytest.fixture()
def setup():
    print("\nSetup - Execute before each test methods")
    yield
    print("Tear Down - Execute after each test methods")

def test_methodA(setup):
    print("\nExecuting the test case A")

def test_methodB(setup):
    print("\nExecuting the test case B")

def test_methodC(setup):
    print("\nExecuting the test case C")