def check_for_number(number):
    """
    param number: Is the number that is being checked.
    This function checks if the number is integer or float.
    return: Returns integer or float number.
    """
    allowed_characters = "0123456789."
    check_for_letter_or_symbol = [digit for digit in number if digit not in allowed_characters]
    if len(number) > 1 and 0 < number.count(".") < 2 and not check_for_letter_or_symbol:
        return float(number)
    elif number and not number.count(".") and not check_for_letter_or_symbol:
        return int(number)
