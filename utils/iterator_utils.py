from typing import Optional
from custom_exceptions import ConstraintError
from collections.abc import Iterable

def get_list_str(length:int)->list[str]:
    """
    Reads a fixed number of strings from standard input.

    Args:
        length (int): Number of strings to read.

    Returns:
        list[str]: A list containing the inserted strings.
    """
    list_str:list[str] = list()

    for i in range(length+1):
        list_str.append(input().strip())

    return list_str

def get_el_in_iterable(iterable_str:Iterable[str])->str:
    """
    Reads a string from input and checks that it exists inside a given iterable.

    The function keeps asking until a valid value is provided.

    Args:
        iterable_str (Iterable[str]): Allowed values.

    Returns:
        str: A valid value contained in the iterable.

    Raises:
        ConstraintError: If the inserted value is not in the iterable.
    """
    while True:
        user_value = input().strip()

        if user_value in iterable_str:
            return user_value
        else:
            raise ConstraintError()

def get_str_by_iterable(
    items: Iterable,
    general_marker: str,
    first_marker: str,
    last_marker: str,
    base_str: Optional[str] = None,
    before_last_marker: Optional[str] = None
) -> str:
    """
    Builds a formatted string from an iterable with custom separators.

    This function is useful for presenting selectable options to the user.

    Example:
        items = ("a", "b", "c")
        Result: "a, b and c"

    Args:
        items (Iterable): Elements to format.
        general_marker (str): Separator between all elements except the last.
        first_marker (str): Prefix added before the generated string.
        last_marker (str): Suffix added after the generated string.
        base_str (Optional[str]): Base string prepended to the output.
        before_last_marker (Optional[str]): Separator before the last element.

    Returns:
        str: A formatted string representation of the iterable.
    """
    parts = [str(x) for x in items]
    n = len(parts)

    if n == 0:
        return base_str + first_marker + last_marker

    if before_last_marker is None:
        core = general_marker.join(parts)

    else:
        if n == 1:
            core = parts[0]
        elif n == 2:
            core = before_last_marker.join(parts)  # es: "a and b"
        else:
            core = general_marker.join(parts[:-1])  # "a, b"
            core = core + before_last_marker + parts[-1]  # "a, b and c"

    return base_str + first_marker + core + last_marker

