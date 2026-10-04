import math


def _validate(*args):
    """
    Checks that every argument is a real number (int or float).
    bool is rejected on purpose, since True/False are technically ints in Python.
    Raises:
        ValueError: If any argument is not a number.
    """
    for arg in args:
        if isinstance(arg, bool) or not isinstance(arg, (int, float)):
            raise ValueError("All inputs must be numbers.")


def fun1(x, y):
    """
    Adds two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Sum of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    _validate(x, y)
    return x + y


def fun2(x, y):
    """
    Subtracts two numbers.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Difference of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    _validate(x, y)
    return x - y


def fun3(x, y):
    """
    Multiplies two numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
    Returns:
        int/float: Product of x and y.
    Raises:
        ValueError: If x or y is not a number.
    """
    _validate(x, y)
    return x * y


def fun4(x, y, z):
    """
    Adds three numbers together.
    Args:
        x (int/float): First number.
        y (int/float): Second number.
        z (int/float): Third number.
    Returns:
        int/float: Sum of x, y and z.
    Raises:
        ValueError: If any input is not a number.
    """
    _validate(x, y, z)
    return x + y + z


def fun5(x, y):
    """
    Divides x by y.
    Args:
        x (int/float): Numerator.
        y (int/float): Denominator.
    Returns:
        float: Quotient of x and y.
    Raises:
        ValueError: If x or y is not a number.
        ZeroDivisionError: If y is zero.
    """
    _validate(x, y)
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return x / y


def fun6(base, exponent):
    """
    Raises base to the power of exponent.
    Args:
        base (int/float): The base.
        exponent (int/float): The exponent.
    Returns:
        int/float: base ** exponent.
    Raises:
        ValueError: If inputs are not numbers, or a negative base is raised
                    to a fractional exponent (complex result).
    """
    _validate(base, exponent)
    if base < 0 and not float(exponent).is_integer():
        raise ValueError("Negative base with fractional exponent gives a complex result.")
    return base ** exponent


def fun7(x):
    """
    Square root of a number.
    Args:
        x (int/float): Non-negative number.
    Returns:
        float: Square root of x.
    Raises:
        ValueError: If x is not a number or is negative.
    """
    _validate(x)
    if x < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(x)


def fun8(angle, degrees=False):
    """
    Sine of an angle.
    Args:
        angle (int/float): The angle.
        degrees (bool): If True, angle is in degrees; otherwise radians.
    Returns:
        float: sin(angle).
    Raises:
        ValueError: If angle is not a number.
    """
    _validate(angle)
    if degrees:
        angle = math.radians(angle)
    return math.sin(angle)


def fun9(angle, degrees=False):
    """
    Cosine of an angle.
    Args:
        angle (int/float): The angle.
        degrees (bool): If True, angle is in degrees; otherwise radians.
    Returns:
        float: cos(angle).
    Raises:
        ValueError: If angle is not a number.
    """
    _validate(angle)
    if degrees:
        angle = math.radians(angle)
    return math.cos(angle)


def fun10(angle, degrees=False):
    """
    Tangent of an angle.
    Args:
        angle (int/float): The angle.
        degrees (bool): If True, angle is in degrees; otherwise radians.
    Returns:
        float: tan(angle).
    Raises:
        ValueError: If angle is not a number, or cos(angle) is ~0 (tan undefined).
    """
    _validate(angle)
    if degrees:
        angle = math.radians(angle)
    if math.isclose(math.cos(angle), 0.0, abs_tol=1e-12):
        raise ValueError("Tangent is undefined at this angle.")
    return math.tan(angle)


# f1_op = fun1(2, 3)
# f2_op = fun2(2, 3)
# f3_op = fun3(2, 3)
# f4_op = fun4(f1_op, f2_op, f3_op)
# print(fun8(30, degrees=True))   # 0.5
# print(fun9(60, degrees=True))   # 0.5
