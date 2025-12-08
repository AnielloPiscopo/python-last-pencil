from typing import Optional
from custom_exceptions import ConversionError , ConstraintError

def get_num_in_range(x: int, y: Optional[int] = None) -> int:
    """
    Reads a numeric input and validates that it falls within a specified range.

    If y is None, the function checks that:
        num > x

    If y is provided, the function checks that:
        x < num <= y

    Args:
        x (int): Lower exclusive bound.
        y (Optional[int]): Upper inclusive bound. If None, only the lower bound is enforced.

    Returns:
        int: A valid integer that satisfies the specified constraints.

    Raises:
        ConstraintError: If the value does not respect the given range.
        ConversionError: If the value cannot be converted to an integer.
    """
    num = get_num()

    if y is None:
        if num <= x:
            raise ConstraintError()
    else:
        if not (x < num <= y):
            raise ConstraintError()

    return num

def get_num()->int:
    """
    Reads an integer from standard input.

    Returns:
        int: The integer value entered by the user.

    Raises:
        ConversionError: If the input is not a valid numeric value.
    """
    try:
        num:int = int(input().strip())
        return num
    except ValueError:
        raise ConversionError()
