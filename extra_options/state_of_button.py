buttons_clicked = {
    'blank 1': False,
    'blank 2': False
}


def check_state_of_button(*args):
    """
    param args: holds the entries from the user, the button state and the color of the button
    This function checks if the user has written anything.
    Function is called when the user releases the button that is being pressed.
    Changes the state of the button to normal if the user has written anything in the blank and changes the button color
    If the user has not written anything, then the function is not called and the button state remains disabled.
    """
    if len(args) == 4:    # if there are 2 fields of entries
        blank_one = args[0]
        blank_two = args[1]
        button = args[2]
        main_color_of_button = args[3]
        if blank_one.get():
            buttons_clicked['blank 1'] = True
        else:
            buttons_clicked['blank 1'] = False
        if blank_two.get():
            buttons_clicked['blank 2'] = True
        else:
            buttons_clicked['blank 2'] = False
        if buttons_clicked['blank 1'] and buttons_clicked['blank 2']:
            button['state'] = 'normal'
            button['bg'] = main_color_of_button
        else:
            button['state'] = 'disabled'
            button['bg'] = 'grey'
    elif len(args) == 3:    # if there is only 1 field of entry
        blank_one = args[0]
        button = args[1]
        main_color_of_button = args[2]
        if blank_one.get():
            buttons_clicked['blank 1'] = True
        else:
            buttons_clicked['blank 1'] = False
        if buttons_clicked['blank 1']:
            button['state'] = 'normal'
            button['bg'] = main_color_of_button
        else:
            button['state'] = 'disabled'
            button['bg'] = 'grey'
