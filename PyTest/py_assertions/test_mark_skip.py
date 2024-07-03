import pytest
pytestmark = [pytest.mark.smoke]

@pytest.mark.xfail
def test_string01():
    letters = "abcdefghijklmnopqrstuvwxyz"
    assert len(letters)==30

#pytest -v -m "sanity" PythonPyTest
@pytest.mark.sanity
def test_string02():
    a = "Ranjith"
    b = 'Kumar'
    print(a)
    print(b)

@pytest.mark.sanity
def test_string03():
    c = "string with 'single quotes'"
    d = 'string with "double quotes"'
    print(c)
    print(d)

@pytest.mark.xfail
def test_string04():
    e = "string with \"double quotes\""
    f = 'string with \'single quotes\''
    print(f)
    g = "string with single quote's"
    print(g)

@pytest.mark.sanity
def test_string05():
    h = "string written in multiple lines\
     but displaying in single line\
     continuing the line"
    print(h)

@pytest.mark.slice
def test_string06():
    name = "Ranjith"
    assert name[:]==name
    assert name[2:]=="njith"
    assert name[:3]=="Ran"

@pytest.mark.slice
def test_string07():
    name = "Ranjith"
    assert name[::-1]=="htijnaR"
    assert name[::-2]=="hinR"
