from tkinter import *
from tkinter import messagebox


def delete_phone_number(program_data, update_distributors):
    remove_phone = Tk()
    remove_phone.title("Remove phone")
    remove_phone.geometry('250x230+800+400')
    remove_phone.resizable(False, False)
    Label(remove_phone, bd=3, text='Write the phone number', font='Arial 14').pack()

    entry_number = Entry(remove_phone, bd=3, width=50, bg='powder blue', font='Arial 30')
    entry_number.pack()

    Label(remove_phone, bd=3, text='Remove from "distributor"', font='Arial 14').pack()

    entry_distributor = Entry(remove_phone, bd=3, width=50, bg='powder blue', font='Arial 30')
    entry_distributor.pack()

    add_button = Button(remove_phone, bd=3, bg='red',
                        font='Arial 20', text='REMOVE',
                        command=lambda: delete_phone_validation(remove_phone, entry_number, entry_distributor,
                                                                program_data, update_distributors))
    add_button.pack()


def delete_phone_validation(window, phone, distributor, program_data, update_distributors):
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