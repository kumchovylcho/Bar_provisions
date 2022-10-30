from tkinter import *
from tkinter import messagebox
import json
import os.path


def update_screen_distributors():
    """
    Making a frame to use its parameters so the Text box can be positioned and the scrollbar can be added to the frame.
    The scrollbar is set to be on the right side of the text and set to be vertical.
    Making a Text widget to fill all the information about DISTRIBUTORS when the button is clicked.
    Checking if there is something inside distributors to start inserting process on the screen, if there is no
    distributors, a special message will appear.
    Showing all distributors and their phone numbers on screen with a single for loop.
    The text is positioned on the left side of the frame and made the text non-deletable(read-only), but can be copied
    with ctrl + C.
    """
    text_box = Frame(window_frame, width=67, height=29, bg='powder blue')
    text_box.place(x=230, y=80)
    scrollbar = Scrollbar(text_box)
    scrollbar.pack(side=RIGHT, fill=Y)
    showing_all_distributors = Text(text_box, width=37, height=17, bg='powder blue', font='Arial 17',
                                    yscrollcommand=scrollbar.set)
    if program_data["distributors"]:
        for name in sorted(program_data["distributors"]):
            show_info = f"{name}:\n"
            showing_all_distributors.insert(END, show_info)
            if not program_data['distributors'][name]['phone_numbers']:
                phone_numbers = f"{4 * ' '}phone numbers:{2 * ' '}" \
                                f"None\n\n"
                showing_all_distributors.insert(END, phone_numbers)
            elif program_data['distributors'][name]['phone_numbers']:
                phone_numbers = f"{4 * ' '}phone numbers:{2 * ' '}" \
                                f"{', '.join(program_data['distributors'][name]['phone_numbers'])}\n\n"
                showing_all_distributors.insert(END, phone_numbers)

    else:
        showing_all_distributors.insert('1.0', "There are no current distributors.")
    showing_all_distributors.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=showing_all_distributors.yview())
    showing_all_distributors.config(state=DISABLED, pady=3)


def show_distributor_options():
    """
    Added a button right above the frame visible only after the Distributors button is clicked.The Add Distributor
    button leads to another function.
    Added a button right after Add Distributor button which deletes current distributor with all the phone numbers
    if there are any saved.
    Added a button which removes a single distributor and all of his phone numbers, which if you click on DELETE
    it opens up a confirmation window.
    Added a "Add phone-number" button next to the "Remove Distributor" button which leads to another function
    for validation process.
    Added a "Remove phone-number" button next to the "Add phone-number" button which leads to another function for
    validation process.
    Calling "update_screen_distributors" to update the screen with changes if there are any.
    """

    add_extra_distributors = Button(window_frame, text='Add Distributor', bd=3, command=add_new_distributor)
    add_extra_distributors.place(x=230, y=53)

    remove_distributor = Button(window_frame, text='Remove Distributor', bd=3, command=delete_distributor)
    remove_distributor.place(x=324, y=53)

    add_phone_number = Button(window_frame, text='Add phone-number', bd=3, command=add_new_phone_number)
    add_phone_number.place(x=439, y=53)

    remove_phone_number = Button(window_frame, text='Remove phone-number', bd=3, command=delete_phone_number)
    remove_phone_number.place(x=558, y=53)

    update_screen_distributors()


def delete_distributor():
    """
    Made a window which you can enter a distributor name which you want to delete.
    After the DELETE button is pressed , the entry from what user has typed is send to ~delete_confirmation~ function.
    """
    remove_distributor_window = Tk()
    remove_distributor_window.title("Delete")
    remove_distributor_window.geometry('250x160+800+400')
    remove_distributor_window.resizable(False, False)
    distributor_to_be_deleted = Label(remove_distributor_window, text='Delete Distributor', font='Arial 18')
    user_input = Entry(remove_distributor_window, bg='powder blue', font='Arial 24')
    distributor_to_be_deleted.pack()
    user_input.pack()
    delete_distributor_button = Button(remove_distributor_window, font='Arial 20', bg='red', text='DELETE',
                                       command=lambda: delete_distributor_confirmation(user_input,
                                                                                       remove_distributor_window))
    delete_distributor_button.pack()


def delete_distributor_confirmation(distributor_check, delete_distri_window):
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
    update_screen_distributors()


def delete_phone_number():
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
                        command=lambda: delete_phone_validation(remove_phone, entry_number, entry_distributor))
    add_button.pack()


def delete_phone_validation(window, phone, distributor):
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
    update_screen_distributors()


def add_new_distributor():
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
           command=lambda: look_through_json(entry_text, distributor_add_window)).pack()


def add_new_phone_number():
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
                        command=lambda: new_phone_number_validation(add_phone_window, entry_number, entry_distributor))
    add_button.pack()


def new_phone_number_validation(window, phone_number, distributor_name):
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
    update_screen_distributors()


def look_through_json(distributor_name, add_info_window):
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
    update_screen_distributors()


def read_json(all_data):
    if not os.path.isfile('app_information.json'):
        with open("app_information.json", "w") as file:
            json.dump(all_data, file)
    with open("app_information.json", 'r') as f:
        take_from_file = json.load(f)
    return take_from_file


app_information = {
    "distributors": {},
    "products": {}
}

window_frame = Tk()
app_width = 1000
app_height = 600
window_frame.resizable(False, False)

# centering the main window
screen_width = window_frame.winfo_screenwidth()
screen_height = window_frame.winfo_screenheight()
centering_width = screen_width // 2 - app_width // 2
centering_height = screen_height // 2 - app_height // 2
window_frame.geometry(f"{app_width}x{app_height}+{centering_width}+{centering_height}")

# program distributor_name
window_frame.title('Bar-Manager')

# background color of main window
window_frame.configure(bg='#C1C1FF')

# distributors button
distributors = Button(window_frame, text='Distributors', bd=3, width=15, height=2, command=show_distributor_options)
# distributor button position
distributors.place(x=0, y=0)

# adding a frame in the middle of screen to show result of buttons
frame_window = Frame(window_frame, width=app_width // 2, height=450, bg='powder blue')
frame_window.place(x=230, y=80)

program_data = read_json(app_information)
window_frame.mainloop()
with open('app_information.json', 'w') as data:
    json.dump(program_data, data, indent=2)
