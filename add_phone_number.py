from tkinter import *
from tkinter import messagebox


def add_new_phone_number(program_data, update_distributors):
    add_phone_window = Tk()
    add_phone_window.title("Add phone")
    add_phone_window.geometry('250x230+800+400')
    add_phone_window.resizable(False, False)
    Label(add_phone_window, bd=3, text='Write the phone number', font='Arial 11').pack()

    entry_number = Entry(add_phone_window, bd=3, width=50, bg='powder blue', font='Arial 30')
    entry_number.pack()

    Label(add_phone_window, bd=3, text='Add the phone number to "distributor"', font='Arial 11').pack()

    entry_distributor = Entry(add_phone_window, bd=3, width=50, bg='powder blue', font='Arial 30')
    entry_distributor.pack()

    add_button = Button(add_phone_window, bd=3, bg='light green',
                        font='Arial 20', text='ADD',
                        command=lambda: new_phone_number_validation(add_phone_window, entry_number, entry_distributor,
                                                                    program_data, update_distributors))
    add_button.pack()


def new_phone_number_validation(window, phone_number, distributor_name, program_data, update_distributors):
    phone_number, distributor_name = phone_number.get(), distributor_name.get().capitalize()
    if distributor_name in program_data['distributors']:
        if phone_number not in program_data['distributors'][distributor_name]['phone_numbers'] \
                and distributor_name in program_data['distributors']:
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