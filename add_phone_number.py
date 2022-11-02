from tkinter import *
from tkinter import messagebox


def add_new_phone_number(program_data, update_distributors):
    """
    param program_data: Holds the json file information.
    param update_distributors: Is a function which updates the screen on every distributor related button.
    This function makes a window where you write the new phone number and adds it to the distributor you chose.
    The entries are sent to new_phone_number_validation function.
    There are 2 labels giving information above the entries.
    """
    add_phone_window = Tk()
    add_phone_window.title("Add phone")
    add_phone_window.geometry('250x230+800+400')
    add_phone_window.resizable(False, False)
    Label(add_phone_window, bd=3, text='Write the phone number', font='Arial 16 bold').pack()

    entry_number = Entry(add_phone_window, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
    entry_number.pack()

    Label(add_phone_window, bd=3, text='Add to "distributor"', font='Arial 18 bold').pack()

    entry_distributor = Entry(add_phone_window, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
    entry_distributor.pack()

    add_button = Button(add_phone_window, bd=3, bg='#40FA5A',
                        font='Arial 20 bold', text='ADD',
                        command=lambda: new_phone_number_validation(add_phone_window, entry_number, entry_distributor,
                                                                    program_data, update_distributors))
    add_button.pack()


def new_phone_number_validation(window, phone_number, distributor_name, program_data, update_distributors):
    """
    param window: Is the window that has been made in function add_new_phone_number
    param phone_number: Is the entry phone-number from the user.
    param distributor_name: Is the entry distributor name from the user.
    param program_data: Holds the json file information.
    param update_distributors: Is a function which updates the screen on every distributor related buttons.
    First checking if the distributor is already existing, if the distributor exists, then it checks for
    the phone number.If the phone number does not exist, then it is being added.
    If the phone number and distributor exists, then a message will pop up showing that you can't have same numbers.
    If the distributor name does not exist, doesn't matter if the phone-number is correct, then an error message will
    pop up with text that distributor is not found, and you should write a correct one.
    """
    phone_number, distributor_name = phone_number.get(), distributor_name.get().capitalize()
    if distributor_name in program_data['distributors']:
        if phone_number not in program_data['distributors'][distributor_name]['phone_numbers']:
            program_data['distributors'][distributor_name]['phone_numbers'].append(phone_number)
            messagebox.showinfo("Added",
                                f"Phone number {phone_number} has been added to {distributor_name} distributor.")
        elif phone_number in program_data['distributors'][distributor_name]['phone_numbers']:
            messagebox.showinfo('Error',
                                f"Phone number {phone_number} is not unique.You can't have two identical numbers.")
    elif distributor_name not in program_data['distributors']:
        messagebox.showerror('Not found', f"{distributor_name} distributor is not found in the data base."
                                          f"Please write a correct distributor name.")

    window.destroy()
    update_distributors()