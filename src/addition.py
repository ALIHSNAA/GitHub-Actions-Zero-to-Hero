# app.py
#testing
#hello
# This is a test commit
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
def test_sub():
    assert sub(7, 4) == 3
