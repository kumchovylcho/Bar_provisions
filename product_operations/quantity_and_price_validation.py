def check_for_number(number):
    """
    param number: Is the number that is being checked.
    This function checks if the quantity is integer or float.
    return: Returns integer or float number.
    """
    allowed_characters = "0123456789."
    scan_all_symbols = [digit if digit in allowed_characters else digit for digit in number]
    check_for_letter_or_symbol = [digit for digit in scan_all_symbols if digit not in allowed_characters]
    if scan_all_symbols and 0 < scan_all_symbols.count(".") < 2 and not check_for_letter_or_symbol:
        return float(number)
    elif scan_all_symbols and not scan_all_symbols.count(".") and not check_for_letter_or_symbol:
        return int(number)
