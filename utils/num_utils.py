from typing import Optional
from custom_exceptions import ConversionError , ConstraintError

def get_num_in_range(x: int, y: Optional[int] = None) -> int:
    num = get_num()

    if y is None:
        if num <= x:
            raise ConstraintError()
    else:
        if not (x < num <= y):
            raise ConstraintError()

    return num

def get_num()->int:
    try:
        num:int = int(input().strip())
        return num
    except ValueError:
        raise ConversionError()
