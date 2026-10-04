import math

import pytest

from src.calc import fun1, fun2, fun3, fun4, fun5, fun6, fun7, fun8, fun9, fun10


# ---------- shared fixtures ----------

@pytest.fixture
def bad_inputs():
    """Values that every function should reject."""
    return ["5", None, [1], {"a": 1}, True, (2,)]


@pytest.fixture
def angles_rad():
    """A spread of angles in radians, used for identity checks."""
    return [i * math.pi / 12 for i in range(-24, 25)]


# ---------- fun1: addition (parametrized table) ----------

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (10, 20, 30),
        (-7, 7, 0),
        (0, 0, 0),
        (1e10, 1e10, 2e10),
        (-1.5, -2.5, -4.0),
    ],
)
def test_fun1_table(x, y, expected):
    assert fun1(x, y) == pytest.approx(expected)


def test_fun1_is_commutative():
    assert fun1(3.7, -9) == fun1(-9, 3.7)


# ---------- fun2: subtraction ----------

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (100, 1, 99),
        (0, 5, -5),
        (-3, -3, 0),
        (1.75, 0.25, 1.5),
    ],
)
def test_fun2_table(x, y, expected):
    assert fun2(x, y) == pytest.approx(expected)


def test_fun2_is_inverse_of_fun1():
    # (a + b) - b == a
    assert fun2(fun1(42, 8), 8) == 42


# ---------- fun3: multiplication ----------

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (-4, 5, -20),
        (-4, -5, 20),
        (1, 999, 999),
        (0.5, 0.5, 0.25),
    ],
)
def test_fun3_table(x, y, expected):
    assert fun3(x, y) == pytest.approx(expected)


def test_fun3_distributive_over_fun1():
    # a * (b + c) == a*b + a*c
    a, b, c = 3, 4, 5
    assert fun3(a, fun1(b, c)) == fun1(fun3(a, b), fun3(a, c))


# ---------- fun4: sum of three ----------

def test_fun4_all_zero():
    assert fun4(0, 0, 0) == 0


def test_fun4_cancels_out():
    assert fun4(10, -4, -6) == 0


def test_fun4_order_does_not_matter():
    assert fun4(1, 2, 3) == fun4(3, 1, 2) == fun4(2, 3, 1)


def test_fun4_rejects_non_numbers():
    with pytest.raises(ValueError):
        fun4(1, "2", 3)


# ---------- fun5: division ----------

@pytest.mark.parametrize(
    "x, y, expected",
    [
        (10, 4, 2.5),
        (-9, 3, -3.0),
        (0, 7, 0.0),
        (1, 3, 1 / 3),
    ],
)
def test_fun5_table(x, y, expected):
    assert fun5(x, y) == pytest.approx(expected)


@pytest.mark.parametrize("zero", [0, 0.0])
def test_fun5_divide_by_zero(zero):
    with pytest.raises(ZeroDivisionError, match="divide by zero"):
        fun5(5, zero)


def test_fun5_undoes_fun3():
    assert fun5(fun3(6, 7), 7) == pytest.approx(6)


# ---------- fun6: power ----------

@pytest.mark.parametrize(
    "base, exp, expected",
    [
        (2, 10, 1024),
        (5, 0, 1),
        (9, 0.5, 3.0),
        (-2, 3, -8),
        (2, -1, 0.5),
    ],
)
def test_fun6_table(base, exp, expected):
    assert fun6(base, exp) == pytest.approx(expected)


def test_fun6_negative_base_fractional_exponent():
    with pytest.raises(ValueError, match="complex"):
        fun6(-8, 1 / 3)


# ---------- fun7: square root ----------

@pytest.mark.parametrize("x", [0, 1, 2, 16, 0.25, 1e6])
def test_fun7_squared_gives_back_input(x):
    assert fun7(x) ** 2 == pytest.approx(x)


def test_fun7_negative_raises():
    with pytest.raises(ValueError, match="negative"):
        fun7(-1)


# ---------- fun8: sine ----------

@pytest.mark.parametrize(
    "deg, expected",
    [
        (0, 0.0),
        (30, 0.5),
        (90, 1.0),
        (180, 0.0),
        (270, -1.0),
    ],
)
def test_fun8_known_degrees(deg, expected):
    assert fun8(deg, degrees=True) == pytest.approx(expected, abs=1e-12)


def test_fun8_radians_default():
    assert fun8(math.pi / 2) == pytest.approx(1.0)


def test_fun8_is_odd_function(angles_rad):
    # sin(-x) == -sin(x)
    for a in angles_rad:
        assert fun8(-a) == pytest.approx(-fun8(a), abs=1e-12)


def test_fun8_is_periodic():
    assert fun8(1.0) == pytest.approx(fun8(1.0 + 2 * math.pi))


def test_fun8_output_bounded(angles_rad):
    assert all(-1.0 <= fun8(a) <= 1.0 for a in angles_rad)


# ---------- fun9: cosine ----------

@pytest.mark.parametrize(
    "deg, expected",
    [
        (0, 1.0),
        (60, 0.5),
        (90, 0.0),
        (180, -1.0),
        (360, 1.0),
    ],
)
def test_fun9_known_degrees(deg, expected):
    assert fun9(deg, degrees=True) == pytest.approx(expected, abs=1e-12)


def test_fun9_is_even_function(angles_rad):
    # cos(-x) == cos(x)
    for a in angles_rad:
        assert fun9(-a) == pytest.approx(fun9(a), abs=1e-12)


def test_fun9_is_shifted_sine():
    # cos(x) == sin(x + pi/2)
    x = 0.7
    assert fun9(x) == pytest.approx(fun8(x + math.pi / 2))


# ---------- sin and cos together ----------

def test_pythagorean_identity(angles_rad):
    # sin^2(x) + cos^2(x) == 1
    for a in angles_rad:
        assert fun8(a) ** 2 + fun9(a) ** 2 == pytest.approx(1.0)


def test_double_angle_identity():
    # sin(2x) == 2 sin(x) cos(x)
    x = 0.4
    assert fun8(2 * x) == pytest.approx(2 * fun8(x) * fun9(x))


# ---------- fun10: tangent ----------

@pytest.mark.parametrize(
    "deg, expected",
    [
        (0, 0.0),
        (45, 1.0),
        (-45, -1.0),
        (180, 0.0),
    ],
)
def test_fun10_known_degrees(deg, expected):
    assert fun10(deg, degrees=True) == pytest.approx(expected, abs=1e-12)


def test_fun10_equals_sin_over_cos():
    x = 1.1
    assert fun10(x) == pytest.approx(fun8(x) / fun9(x))


@pytest.mark.parametrize("deg", [90, 270, -90])
def test_fun10_undefined_angles(deg):
    with pytest.raises(ValueError, match="undefined"):
        fun10(deg, degrees=True)


# ---------- input validation across every function ----------

TWO_ARG_FUNCS = [fun1, fun2, fun3, fun5, fun6]
ONE_ARG_FUNCS = [fun7, fun8, fun9, fun10]


@pytest.mark.parametrize("func", TWO_ARG_FUNCS)
def test_two_arg_funcs_reject_bad_inputs(func, bad_inputs):
    for bad in bad_inputs:
        with pytest.raises(ValueError):
            func(bad, 1)
        with pytest.raises(ValueError):
            func(1, bad)


@pytest.mark.parametrize("func", ONE_ARG_FUNCS)
def test_one_arg_funcs_reject_bad_inputs(func, bad_inputs):
    for bad in bad_inputs:
        with pytest.raises(ValueError):
            func(bad)


# ---------- end-to-end pipeline ----------

def test_chained_pipeline():
    a = fun1(2, 3)        # 5
    b = fun2(10, 4)       # 6
    c = fun3(a, b)        # 30
    d = fun5(c, 3)        # 10.0
    e = fun6(d, 2)        # 100.0
    f = fun7(e)           # 10.0
    assert fun4(a, b, f) == pytest.approx(21.0)
