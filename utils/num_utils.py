from typing import Optional
from custom_exceptions import ConversionError , ConstraintError

def get_num_in_range(x:int , y:Optional[int]=None)->int:
    while True:
        try:
            num:int = get_num()

            if y is None:
                if num > x:
                    return num
                else:
                    raise ConstraintError()
            else:
                if y>=num>x:
                    return num
                else:
                    raise ConstraintError()
        except ConstraintError:
            raise ConstraintError()
        except ConversionError:
            raise ConversionError()

def get_num()->int:
    try:
        num:int = int(input().strip())
        return num
    except ValueError:
        raise ConversionError()