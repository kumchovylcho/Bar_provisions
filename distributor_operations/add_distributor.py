from tkinter import *
from extra_options.state_of_button import check_state_of_button
from extra_options.limit_of_windows import *
from tkinter import messagebox


def add_new_distributor(program_data, update_screen):
    """
    This function makes a window with geometry to center the window in the middle when it opens.
    The window is not resizable
    You can write distributor name , and then you can press the ADD button to save
    the changes.
    If the information you filled is unique, then the distributor will be added.
    The ADD button sends the entry from the user, program_data and update_screen to function named "look_through_json"
    """
    if check_if_opened():
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
        entry_text.bind('<KeyRelease>', lambda message: check_state_of_button(entry_text, add_button,
                                                                              color_of_delete_button))


def check_for_existence(distributor_name, add_info_window, program_data, refresh_screen):
    """
    Parameter distributor_name is taken after the ADD button is clicked, and it's first letter is capitalized.
    Checking if distributor_name is not empty.
    Adding the distributor to the json file if it is unique which means it doesn't exist.
    If the distributor does not exist, then a special message box will pop on the screen.
    """
    distributor_name = distributor_name.get().capitalize()
    if distributor_name not in program_data["distributors"]:
        program_data["distributors"][distributor_name] = distributor_name
        program_data["distributors"][distributor_name] = {"phone_numbers": []}
        messagebox.showinfo('Added', f'{distributor_name} distributor has been added to the database.')
    elif distributor_name in program_data['distributors']:
        messagebox.showerror('Error', f"{distributor_name} is already in the database.")
    add_info_window.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    refresh_screen()
