from typing import Optional
from custom_exceptions import ConstraintError
from collections.abc import Iterable

def get_list_str(length:int)->list[str]:
    list_str:list[str] = list()

    for i in range(length+1):
        list_str.append(input().strip())

    return list_str

def get_el_in_iterable(iterable_str:Iterable[str])->str:
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

