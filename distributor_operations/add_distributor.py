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


def add_new_distributor(program_data, update_screen):
    global limit_of_windows
    """
    This function makes a window with geometry to center the window in the middle when it opens.
    The window is not resizable
    You can write distributor name , and then you can press the ADD button to save
    the changes.
    If the information you filled is unique, then the distributor will be added.
    The ADD button sends the entry from the user, program_data and update_screen to function named "look_through_json"
    """
    if limit_of_windows < 2:
        limit_of_windows += 1
        distributor_add_window = Tk()
        distributor_add_window.title("Add")
        distributor_add_window.geometry('250x150+800+400')
        distributor_add_window.resizable(False, False)
        distributor_add_window.config(bg='#A49E97')
        title_name = Label(distributor_add_window, bd=3, text='Distributor', font='Arial 15 bold', bg='#FFCCA7',
                           width=20)

        entry_text = Entry(distributor_add_window, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
        title_name.pack()
        entry_text.pack()

        add_button = Button(distributor_add_window, text='ADD', bd=3,
                            font='Arial 15 bold', bg='grey', state='disabled',
                            command=lambda: check_for_existence(entry_text, distributor_add_window, program_data,
                                                                update_screen))
        add_button.pack()
        distributor_add_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(distributor_add_window))
        color_of_delete_button = '#40FA5A'
        entry_text.bind('<KeyRelease>', lambda message: capture_text(entry_text, add_button, color_of_delete_button))


def check_for_existence(distributor_name, add_info_window, program_data, refresh_screen):
    global limit_of_windows
    """
    Parameter distributor_name is taken after the ADD button is clicked, and it's first letter is capitalized.
    Checking if distributor_name is not empty.
    Adding the distributor to the json file if it is unique which means it doesn't exist.
    If the distributor does not exist, then a special message box will pop on the screen.
    """
    distributor_name = distributor_name.get().capitalize()
    if distributor_name:
        if distributor_name not in program_data["distributors"]:
            program_data["distributors"][distributor_name] = distributor_name
            program_data["distributors"][distributor_name] = {"phone_numbers": []}
            messagebox.showinfo('Added', f'{distributor_name} distributor has been added to the database.')
        elif distributor_name in program_data['distributors']:
            messagebox.showerror('Error', f"{distributor_name} is already in the database.")
    elif not distributor_name:
        messagebox.showinfo("Error", "Please fill in a distributor name.")
    add_info_window.destroy()
    limit_of_windows -= 1
    refresh_screen()
