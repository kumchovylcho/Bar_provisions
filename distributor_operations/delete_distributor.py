from tkinter import *
from tkinter import messagebox
from extra_options.detect_text import capture_text

limit_of_windows = 1


def ask_to_close_window(window):
    """
    param window: Is the window that will be closed if the user selects yes on the message box.
    This function checks if the user tries to close the window with X button or alt-f4.
    The only way to close the window is selecting yes from the message box or going through the steps of the button.
    """
    global limit_of_windows
    question = messagebox.askokcancel('Confirm', 'Do you want to close the window ?')
    if question:
        limit_of_windows -= 1
        window.destroy()


def delete_distributor(program_data, update_distributors):
    global limit_of_windows
    """
    Made a window where you can enter distributor name which you want to delete.
    After the DELETE button is pressed , the entry from what user has typed is send to ~delete_confirmation~ function.
    """
    if limit_of_windows < 2:
        limit_of_windows += 1
        remove_distributor_window = Tk()
        remove_distributor_window.title("Delete")
        remove_distributor_window.geometry('250x170+800+400')
        remove_distributor_window.resizable(False, False)
        remove_distributor_window.config(bg='#A49E97')
        Label(remove_distributor_window, text='Delete Distributor', font='Arial 18 bold',
              bg='#FFCCA7', width=20).pack()
        user_input = Entry(remove_distributor_window, bg='powder blue', font='Arial 24 bold')
        user_input.pack()
        delete_button = Button(remove_distributor_window, font='Arial 20 bold', bg='grey', text='DELETE',
                               state='disabled',
                               command=lambda: delete_distributor_confirmation(user_input, remove_distributor_window,
                                                                               program_data,
                                                                               update_distributors))
        delete_button.pack()
        remove_distributor_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(remove_distributor_window))
        color_of_delete_button = 'grey'
        user_input.bind('<KeyRelease>', lambda message: capture_text(user_input, delete_button, color_of_delete_button))


def delete_distributor_confirmation(distributor_check, delete_distri_window, program_data, update_distributors):
    global limit_of_windows
    """
    param distributor_check: Is the entry from the user.
    param delete_distri_window: This is the window that has been made in delete_distributor function, which will be
    closed after the program checks if the entry from the user is valid.
    Checking if the entry from the user exist in distributors, if so then a window with a question shows up which
    you can answer with yes/no.
    If the user does not exist in distributors, an error message will appear.
    If you typed a correct distributor and click DELETE, you need to confirm with yes/no if you really want to delete it
    After that, the window of delete_distributor will close.
    """
    user_input_from_button = distributor_check.get().capitalize()
    if user_input_from_button in program_data["distributors"]:
        msg_box = messagebox.askquestion("Confirm",
                                         f"Deleting distributor {user_input_from_button}"
                                         f" will delete all of it's data including phone numbers!")
        if msg_box == "yes":
            del program_data["distributors"][user_input_from_button]
            messagebox.showinfo("Deleted", f"{user_input_from_button} and it's phone numbers are deleted.")
    elif user_input_from_button not in program_data["distributors"]:
        messagebox.showerror("Error", f"Distributor {user_input_from_button} does not exist!")
    delete_distri_window.destroy()
    limit_of_windows -= 1
    update_distributors()
