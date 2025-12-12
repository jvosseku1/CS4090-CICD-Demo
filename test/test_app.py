import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root/"src"))

import app
import math

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10

def test_add3():
    assert add(-5, 1) == -4

def test_sub1():
    assert sub(6,5) == 1

def test_sub2():
    assert sub(5,6) == -1

def test_mult1():
    assert mult(10,10) == 100

def test_mult2():
    assert mult(-1, 10) == -10

def test_mult3():
    assert mult(-1, -10) == 10

def test_div1():
    if b == 0:
        raise ValueError("b cannot be 0\n nothing divisible by 0")
    else:

        def test_div2():
            assert div(10, 2) == 5

        def test_div3():
            assert div(100, 10) == 10

def test_percent1():
    if a > b:
        raise ValueError("a cannot be greater than b")
    elif ((a < 0 or a > 100) or (b < 0 or b > 100)):
        raise ValueError("a and b must be between 0 and 100")
    else:
        def test_percent2():
            assert percent(10, 100) == 10
        
        def test_percent3():