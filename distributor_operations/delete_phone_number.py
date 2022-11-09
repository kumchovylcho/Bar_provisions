from tkinter import *
from extra_options.state_of_button import check_state_of_button
from extra_options.limit_of_windows import *
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
    if check_if_opened():
        remove_phone = Tk()
        remove_phone.title("Remove phone")
        remove_phone.geometry('250x230+800+400')
        remove_phone.resizable(False, False)
        remove_phone.config(bg='#A49E97')
        Label(remove_phone, bd=3, text='Write the phone number', font='Arial 14 bold', bg='#FFCCA7', width=20).pack()

        entry_number = Entry(remove_phone, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
        entry_number.pack()

        Label(remove_phone, bd=3, text='Remove from "distributor"', font='Arial 14 bold', bg='#FFCCA7', width=20).pack()

        entry_distributor = Entry(remove_phone, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
        entry_distributor.pack()

        delete_button = Button(remove_phone, bd=3, bg='grey', state='disabled',
                               font='Arial 20 bold', text='REMOVE',
                               command=lambda: delete_phone_validation(remove_phone, entry_number, entry_distributor,
                                                                       program_data, update_distributors))
        delete_button.pack()
        remove_phone.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(remove_phone))
        color_of_delete_button = 'red'
        entry_number.bind('<KeyRelease>',
                          lambda message: check_state_of_button(entry_number, entry_distributor, delete_button,
                                                                color_of_delete_button))
        entry_distributor.bind('<KeyRelease>',
                               lambda message: check_state_of_button(entry_number, entry_distributor, delete_button,
                                                                     color_of_delete_button))


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
    if distributor in program_data['distributors'] and \
            phone in program_data['distributors'][distributor]['phone_numbers']:
        question = messagebox.askquestion("Delete", f"Do you really want to delete {phone}"
                                                    f" number from {distributor} distributor?")
        if question == 'yes':
            program_data['distributors'][distributor]['phone_numbers'].remove(phone)
            messagebox.showinfo("Information", f"Phone number: {phone} has been successfully removed from"
                                               f" {distributor} distributor.")
    elif distributor in program_data['distributors'] and \
            phone not in program_data['distributors'][distributor]['phone_numbers']:
        messagebox.showerror("Error", f"Phone number: {phone} does not exist in {distributor} distributor.")
    elif distributor not in program_data['distributors']:
        messagebox.showerror("Error", f"Distributor: {distributor} does not exist in data base.")
    window.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_distributors()
