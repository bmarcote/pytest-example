
def add(a, b):
    return a + b


def test_add():
    assert add(2, 3) == 5
    assert add('space', 'ship') == 'spaceship'
    assert abs(add(0.1, 0.2)/0.3 - 1) < 1e-5

def subtract(a, b):
    return a - b


def test_subtract():
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0
    assert abs(subtract(5.5, 3.3)/(5.5-3.3) - 1) < 1e-5
