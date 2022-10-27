from tkinter import *
import json
import os.path


def show_distributors_info():
    """
    Making a frame to use its parameters so the Text box can be positioned and the scrollbar can be added to the frame.
    The scrollbar is set to be on the right side of the text and set to be vertical.
    Making a Text widget to fill all the information about DISTRIBUTORS when the button is clicked.
    Checking if there is something inside distributors to start inserting process on the screen, if there is no
    distributors, a special message will appear.
    Showing all distributors and their phone numbers on screen with a single for loop.
    The text is positioned on the left side of the frame and made the text non-deletable(read-only), but can be copied
    with ctrl + C.
    Added a button right above the frame visible only after the Distributors button is clicked.The Add Distributor
    button leads to another function.
    """
    text_box = Frame(window_frame, width=67, height=29, bg='powder blue')
    text_box.place(x=230, y=80)
    scrollbar = Scrollbar(text_box)
    scrollbar.pack(side=RIGHT, fill=Y)
    showing_all_distributors = Text(text_box, width=60, height=28, bg='powder blue', yscrollcommand=scrollbar.set)
    if program_data["distributors"]:
        for name in sorted(program_data["distributors"]):
            show_info = f"{name}:\n" \
                        f"phone numbers:{2 * ' '}{', '.join(program_data['distributors'][name]['phone_numbers'])}\n\n"
            showing_all_distributors.insert(END, show_info)
    else:
        showing_all_distributors.insert('1.0', "There are no current distributors.")
    showing_all_distributors.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=showing_all_distributors.yview())
    showing_all_distributors.config(state=DISABLED)

    add_extra_distributors = Button(window_frame, text='Add Distributor', bd=3, command=add_new_distributor)
    add_extra_distributors.grid(row=2, column=1, padx=107, pady=24)


def add_new_distributor():
    """
    This function makes a window with geometry to center the window in the middle when it opens.
    The window is not resizable
    You can write distributor name and their phone number, and then you can press the ADD button to save the changes.
    If the information you filled is unique, then the changes will be applied.
    The ADD button sends the entry from entry_text and entry_phone_number to function named "look_through_json"
    """
    distributor_add_window = Tk()
    distributor_add_window.geometry('150x150+800+400')
    distributor_add_window.resizable(False, False)
    title_name = Label(distributor_add_window, bd=3, text='Distributor')
    entry_text = Entry(distributor_add_window, bd=3, width=30, bg='powder blue')
    title_phone = Label(distributor_add_window, bd=3, text='Phone number')
    entry_phone_number = Entry(distributor_add_window, bd=3, width=30, bg='powder blue')
    title_name.pack()
    entry_text.pack()
    title_phone.pack()
    entry_phone_number.pack()
    Button(distributor_add_window, text='ADD', bd=3,
           command=lambda: look_through_json(entry_text, entry_phone_number, distributor_add_window)).pack()


def look_through_json(name, phone_number, add_info_window):
    """
    Parameter name and phone_number is taken after the ADD button is clicked.
    Checking if name and phone_number are not empty.
    Adding the distributor name to the json file if it is unique which means it doesn't exist , so is the phone number.
    If the name exists, but new phone number is added which must be unique, the phone number is saved.
    """
    name, phone_number = name.get(), phone_number.get()
    if name and phone_number:
        if name not in program_data["distributors"]:
            program_data["distributors"][name] = name
            program_data["distributors"][name] = {"phone_numbers": [phone_number]}
        else:
            if phone_number not in program_data["distributors"][name]["phone_numbers"]:
                program_data["distributors"][name]["phone_numbers"].append(phone_number)
    add_info_window.destroy()


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

# program name
window_frame.title('Bar-Manager')

# background color of main window
window_frame.configure(bg='#C1C1FF')

# distributors button
distributors = Button(window_frame, text='Distributors', bd=3, padx=25, command=show_distributors_info)
# distributor button position
distributors.grid(row=0, column=0)

# adding a frame in the middle of screen to show result of buttons
frame_window = Frame(window_frame, width=app_width // 2, height=450, bg='powder blue')
frame_window.place(x=230, y=80)

program_data = read_json(app_information)
window_frame.mainloop()
with open('app_information.json', 'w') as data:
    json.dump(program_data, data, indent=2)

