from tkinter import *
from tkinter import messagebox


def add_new_distributor(program_data, update_screen):
    """
    This function makes a window with geometry to center the window in the middle when it opens.
    The window is not resizable
    You can write distributor distributor_name and their phone number, and then you can press the ADD button to save
    the changes.
    If the information you filled is unique, then the changes will be applied.
    The ADD button sends the entry from entry_text and entry_phone_number to function named "look_through_json"
    """
    distributor_add_window = Tk()
    distributor_add_window.title("Add")
    distributor_add_window.geometry('250x150+800+400')
    distributor_add_window.resizable(False, False)
    title_name = Label(distributor_add_window, bd=3, text='Distributor', font='Arial 15')
    entry_text = Entry(distributor_add_window, bd=3, width=50, bg='powder blue', font='Arial 30')
    title_name.pack()
    entry_text.pack()
    Button(distributor_add_window, text='ADD', bd=3, font='Arial 15', bg='light green',
           command=lambda: look_through_json(entry_text, distributor_add_window, program_data, update_screen)).pack()


def look_through_json(distributor_name, add_info_window, program_data, refresh_screen):
    """
    Parameter distributor_name and phone_number is taken after the ADD button is clicked.
    Checking if distributor_name and phone_number are not empty.
    Adding the distributor distributor_name to the json file if it is unique which means it doesn't exist , so is the
    phone number. If the distributor_name exists, but new phone number is added which must be unique,
    the phone number is saved.                     NEED TO CHANGE DOC STRING
    """
    distributor_name = distributor_name.get().capitalize()
    if distributor_name:
        if distributor_name not in program_data["distributors"]:
            program_data["distributors"][distributor_name] = distributor_name
            program_data["distributors"][distributor_name] = {"phone_numbers": []}
            messagebox.showinfo('Added', f'{distributor_name} distributor has been added to the data base.')
    elif not distributor_name:
        messagebox.showinfo("Error", "Please fill in a distributor name.")
    add_info_window.destroy()
    refresh_screen()



