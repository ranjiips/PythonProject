import pytest

@pytest.fixture()
def setup():
    print("\nSetup - Execute before each test methods")
    yield
    print("Tear Down - Execute after each test methods")

def test_methodD(setup):
    print("\nExecuting the test case D")

def test_methodE(setup):
    print("\nExecuting the test case E")

def test_methodF(setup):
    print("\nExecuting the test case F")