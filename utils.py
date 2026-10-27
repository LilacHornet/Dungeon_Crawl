def check_int(value: str, min : int, max: int ) -> int:
    if not value.isdigit():
        raise TypeError(f"{value} is not a digit")
    int_value = int(value)
    if int_value < min or int_value > max:
        raise Exception(f"{value} is outside of the accepted intervall : {min}-{max}")
    return int_value