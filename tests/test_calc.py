import pytest

from src.calc import fun1, fun2, fun3, fun4


# ---------- fun1: addition ----------

def test_fun1_integers():
    assert fun1(2, 3) == 5


def test_fun1_negatives():
    assert fun1(-2, -3) == -5


def test_fun1_floats():
    assert fun1(0.1, 0.2) == pytest.approx(0.3)


def test_fun1_invalid_input():
    with pytest.raises(ValueError):
        fun1("2", 3)


# ---------- fun2: subtraction ----------

def test_fun2_integers():
    assert fun2(5, 3) == 2


def test_fun2_negative_result():
    assert fun2(2, 3) == -1


def test_fun2_floats():
    assert fun2(5.5, 2.25) == pytest.approx(3.25)


def test_fun2_invalid_input():
    with pytest.raises(ValueError):
        fun2(5, None)


# ---------- fun3: multiplication ----------

def test_fun3_integers():
    assert fun3(2, 3) == 6


def test_fun3_by_zero():
    assert fun3(7, 0) == 0


def test_fun3_floats():
    assert fun3(2.5, 4) == pytest.approx(10.0)


def test_fun3_invalid_input():
    with pytest.raises(ValueError):
        fun3([2], 3)


# ---------- fun4: sum of three ----------

def test_fun4_integers():
    assert fun4(1, 2, 3) == 6


def test_fun4_mixed():
    assert fun4(1, 2.5, -0.5) == pytest.approx(3.0)


def test_fun4_chained():
    # Mirrors the commented-out example at the bottom of calc.py
    f1 = fun1(2, 3)   # 5
    f2 = fun2(2, 3)   # -1
    f3 = fun3(2, 3)   # 6
    assert fun4(f1, f2, f3) == 10
