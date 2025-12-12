import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

import app


def test_add():
    assert app.add(5, 6) == 11

def test_add2():
    assert app.add(5, 6) != 10

def test_add3():
    assert app.add(-5, 1) == -4


def test_sub1():
    assert app.sub(6, 5) == 1

def test_sub2():
    assert app.sub(5, 6) == -1


def test_mult1():
    assert app.mult(10, 10) == 100

def test_mult2():
    assert app.mult(-1, 10) == -10

def test_mult3():
    assert app.mult(-1, -10) == 10


def test_div_by_zero():
    with pytest.raises(ValueError):
        app.div(10, 0)

def test_div2():
    assert app.div(10, 2) == 5

def test_div3():
    assert app.div(100, 10) == 10


def test_percent_invalid_a_gt_b():
    with pytest.raises(ValueError):
        app.percent(80, 40)

def test_percent_bounds():
        with pytest.raises(ValueError):
            app.percent(-1, 100)
        with pytest.raises(ValueError):
            app.percent(50, 200)

def test_percent2():
    assert app.percent(10, 100) == 10

def test_percent3():
    assert app.percent(5, 50) == 10


def test_sqrt_negative():
    with pytest.raises(ValueError):
        app.sqroot(-4)

def test_sqrt2():
    assert app.sqroot(4) == 2

def test_sqrt3():
    assert app.sqroot(1) == 1


def test_sine_invalid():
    with pytest.raises(ValueError):
        app.sine(-1)
    with pytest.raises(ValueError):
        app.sine(2)

def test_sine2():
    assert app.sine(0) == 0

def test_sine3():
    assert app.sine(1) != 1


def test_cosine_invalid():
    with pytest.raises(ValueError):
        app.cosine(-1)
    with pytest.raises(ValueError):
        app.cosine(2)

def test_cosine2():
    assert app.cosine(0) == 1

def test_cosine3():
    assert app.cosine(1) != 0


def test_squared1():
    assert app.squared(1) == 1

def test_squared2():
    assert app.squared(10) == 100

def test_squared3():
    assert app.squared(-10) == 100


def test_log_invalid_base():
    with pytest.raises(ValueError):
        app.logarithm(10, 1)

def test_log_invalid_argument():
    with pytest.raises(ValueError):
        app.logarithm(0, 2)

def test_log1():
    assert app.logarithm(64, 2) == 6

def test_log2():
    assert app.logarithm(16, 2) == 4

def test_log3():
    assert app.logarithm(125, 5) == pytest.approx(3)