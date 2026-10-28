from typing import Callable, List


def check_int(value: str, min : int, max: int, banned_values:List[int] = [] ) -> int:
    if not value.isdigit():
        raise TypeError(f"{value} is not a digit")
    int_value = int(value)
    if int_value < min or int_value > max:
        raise Exception(f"{value} is outside of the accepted intervall : {min}-{max}")
    if int_value in banned_values:
        raise Exception(f"{value} is not an authorised value")
    return int_value

def check_str(value: str, min_len: int, max_len: int):
    if len(value)<min_len or len(value) > max_len:
        raise Exception(f"Your input must be more than 3 characters and less than 20")

def valid_input(validation_func: Callable, min: int, max: int, exceptions = None ) -> int|str:

    while True:
        user_choice = input()
        try:
            if exceptions == None:
                choice = validation_func(user_choice, min, max )
            else:
                choice = validation_func(user_choice, min, max, exceptions )
        except Exception as e : print(e)
        else :
            return choice