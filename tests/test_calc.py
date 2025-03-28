import pytest
# komentarz

def add(a,b):
    return a + b

def test_add():
    assert add(2,3) == 5

# def test_add_not_good():
#     assert add(2,3) == 55

@pytest.mark.parametrize("a,b,wynik",[
    (2,3,5),
    (1,1,2),
    (0,0,0)
])
def test_param_add(a,b,wynik):
    assert add(a,b) == wynik
def test_add_not_good():
    assert add(2,3) == 55
