from tkinter import *
from tkinter import messagebox


def delete_phone_number(program_data, update_distributors):
    """
    param program_data: Is the information that json file holds.
    param update_distributors: is a function which updates the screen after every distributor related button
    is clicked.
    This function makes a window with 2 entries, 2 labels and an ADD button.
    You must fill both entries and click the ADD button and then the information you filled in is sent to a function
    named delete_phone_validation.
    """
    remove_phone = Tk()
    remove_phone.title("Remove phone")
    remove_phone.geometry('250x230+800+400')
    remove_phone.resizable(False, False)
    Label(remove_phone, bd=3, text='Write the phone number', font='Arial 14 bold').pack()

    entry_number = Entry(remove_phone, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
    entry_number.pack()

    Label(remove_phone, bd=3, text='Remove from "distributor"', font='Arial 14 bold').pack()

    entry_distributor = Entry(remove_phone, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
    entry_distributor.pack()

    add_button = Button(remove_phone, bd=3, bg='red',
                        font='Arial 20 bold', text='REMOVE',
                        command=lambda: delete_phone_validation(remove_phone, entry_number, entry_distributor,
                                                                program_data, update_distributors))
    add_button.pack()


def delete_phone_validation(window, phone, distributor, program_data, update_distributors):
    """
    param window: Is the window that has been made in function delete_phone_number which will be closed after the
    if statements.
    param phone: Is the phone number received from the user entry.
    param distributor: Is the distributor name received from the user entry.
    param program_data: Is the data that is being hold in json.
    param update_distributors: Is a function which updates the screen after every distributor related button
    is clicked.
    First it checks for empty entries.
    If the distributor exists and the phone-number exists, then a window will pop up with a confirmation which you can
    answer with Yes or No.If you click the Yes button ,then the phone-number will be deleted from the current
    distributor.
    If the distributor exists but the phone-number from the user does not exist, a special error message will pop up
    with information about that phone-number does not exist.
    If the distributor user does not exist, then a message will pop up that shows an error.
    """
    phone, distributor = phone.get(), distributor.get().capitalize()
    if phone and distributor:
        if distributor in program_data['distributors'] and \
                phone in program_data['distributors'][distributor]['phone_numbers']:
            question = messagebox.askquestion("Delete", f"Do you really want to delete {phone}"
                                                        f" number from {distributor} distributor?")
            if question == 'yes':
                program_data['distributors'][distributor]['phone_numbers'].remove(phone)
                messagebox.showinfo("Information", f"Phone number: {phone} has been successfully removed from"
                                                   f" {distributor} distributor.")
        elif distributor in program_data['distributors'] and\
                phone not in program_data['distributors'][distributor]['phone_numbers']:
            messagebox.showerror("Error", f"Phone number: {phone} does not exist in {distributor} distributor.")
        elif distributor not in program_data['distributors']:
            messagebox.showerror("Error", f"Distributor: {distributor} does not exist in data base.")
    window.destroy()
    update_distributors()