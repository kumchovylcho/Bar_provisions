from tkinter import messagebox

limit_of_windows = {
    'is opened': False
}


def ask_to_close_window(window):
    """
    param window: Is the window that will be closed if the user selects yes on the message box.
    This function checks if the user tries to close the window with X button or alt-f4.
    The only way to close the window is selecting yes from the message box or going through the steps of the button.
    """
    question = messagebox.askokcancel('Confirm', 'Do you want to close the window ?')
    if question:
        limit_of_windows['is opened'] = False
        window.destroy()


def check_if_opened():
    """
    This function checks if a window is opened after any button is clicked.
    return: Returns True if there isn't any window opened.
    """
    if not limit_of_windows['is opened']:
        limit_of_windows['is opened'] = True
        return True
