def capture_text(*args):
    """
    param args: Takes arguments such as button,entries and colors of the button.
    This function checks if the user has written anything.
    Function is called when the user releases the button that is being pressed.
    Changes the state of the button to normal if the user has written anything in the blank and changes the button color
    If the user has not written anything, then the function is not called and the button state remains disabled.
    The else statement on line 18 is to ensure if the user deletes what he has already typed, then the function is
    called again and if he deletes the whole blank, then the button is set to disabled once again.
    """
    user_entry_word, button, main_color = args[0].get(), args[1], args[2]
    if user_entry_word:
        button['state'] = 'normal'
        if main_color == 'grey':
            button['bg'] = 'red'
        else:
            button['bg'] = main_color
    else:
        button['state'] = 'disabled'
        button['bg'] = 'grey'
