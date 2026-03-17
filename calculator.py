def add(a: float, b: float) -> float:
    """
    Returns the arithmetic sum of two numbers.

    Args:
        a (float): First number to add.
        b (float): Second number to add.

    Returns:
        float: The result of a + b.

    Example:
        >>> add(2.5, 3.0)
        5.5
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """
    Returns the difference between a and b.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The result of a - b.

    Example:
        >>> subtract(5.3, 1.2)
        4.2
    """
    return a - b


def product(a: float, b: float) -> float:
    """
    Returns the product sum of two numbers.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The result of a * b.

    Example:
        >>> product(3.6, 2.0)
        7.2
    """
    return a * b


def division(a: float, b: float) -> float:
    """
    Returns the division of a by b.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The result of a / b.

    Example:
        >>> division(5.0, 2.0)
        2.5
    """
    assert b != 0, "b cannot be 0"

    return a / b
