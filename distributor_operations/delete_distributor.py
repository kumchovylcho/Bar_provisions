from tkinter import *
from extra_options.state_of_button import check_state_of_button
from extra_options.limit_of_windows import *
from tkinter import messagebox


def delete_distributor(program_data, update_distributors):
    """
    Made a window where you can enter distributor name which you want to delete.
    After the DELETE button is pressed , the entry from what user has typed is send to ~delete_confirmation~ function.
    """
    if check_if_opened():
        remove_distributor_window = Tk()
        remove_distributor_window.title("Delete")
        remove_distributor_window.geometry('250x170+800+400')
        remove_distributor_window.resizable(False, False)
        remove_distributor_window.config(bg='#A49E97')
        Label(remove_distributor_window, text='Delete Distributor', font='Arial 18 bold',
              bg='#FFCCA7', width=20).pack()
        user_input = Entry(remove_distributor_window, bg='powder blue', font='Arial 24 bold')
        user_input.pack()
        delete_button = Button(remove_distributor_window, font='Arial 20 bold', bg='grey', text='DELETE',
                               state='disabled',
                               command=lambda: delete_distributor_confirmation(user_input, remove_distributor_window,
                                                                               program_data,
                                                                               update_distributors))
        delete_button.pack()
        remove_distributor_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(remove_distributor_window))
        color_of_delete_button = 'red'
        user_input.bind('<KeyRelease>', lambda message: check_state_of_button(user_input, delete_button,
                                                                              color_of_delete_button))


def delete_distributor_confirmation(distributor_check, delete_distri_window, program_data, update_distributors):
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
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_distributors()
