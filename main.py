from read_json import *
from add_distributor import *
from delete_distributor import *
from delete_phone_number import *
from add_phone_number import *
from tkinter import *


def update_distributors():
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

# adding a frame in the middle of screen to show result of buttons
frame_window = Frame(window_frame, width=app_width // 2, height=450, bg='powder blue')
frame_window.place(x=230, y=80)


distributors = Button(window_frame, text='Distributors', bd=3, font='Arial 18', width=12, command=update_distributors)
distributors.place(x=0, y=0)


add_extra_distributors = Button(window_frame, text='Add Distributor', bd=3, font='Arial 11', bg='light green',
                                width=15, command=lambda: add_new_distributor(program_data, update_distributors))
add_extra_distributors.place(x=-1, y=48)


remove_distributor = Button(window_frame, text='Remove Distributor', font='Arial 10', bd=3, width=17,
                            bg='red', command=lambda: delete_distributor(program_data, update_distributors))
remove_distributor.place(x=-2, y=140)


add_phone_number = Button(window_frame, text='Add phone-number', bd=3, font='Arial 11',
                          width=15, command=lambda: add_new_phone_number(program_data, update_distributors))
add_phone_number.place(x=-1, y=79)


remove_phone_number = Button(window_frame, text='Remove phone-number', bd=3, font='Arial 10',
                             width=17, command=lambda: delete_phone_number(program_data, update_distributors))
remove_phone_number.place(x=-2, y=109)


# # products button
# products = Button(window_frame, text='Products', width=14, bd=3, font='Arial 16',
#                   command=lambda: update_products(window_frame))
# # products button position
# products.place(x=0, y=170)


program_data = read_json()
window_frame.mainloop()
save_on_close(program_data)
