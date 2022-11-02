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
    distributors_show_info = Frame(window_frame, width=67, height=29, bg='#F4F3F1')
    distributors_show_info.place(x=230, y=80)
    scrollbar = Scrollbar(distributors_show_info)
    scrollbar.pack(side=RIGHT, fill=Y)
    showing_all_distributors = Text(distributors_show_info, width=37, height=17, bg='#F4F3F1', font='Arial 17 bold',
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
        showing_all_distributors.insert('1.0', "There are currently no distributors.")
    showing_all_distributors.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=showing_all_distributors.yview())
    showing_all_distributors.config(state=DISABLED, pady=3)


def update_products():
    products_show_info = Frame(window_frame, width=67, height=29, bg='#F4F3F1')
    products_show_info.place(x=230, y=80)
    scrollbar = Scrollbar(products_show_info)
    scrollbar.pack(side=RIGHT, fill=Y)
    show_all_products = Text(products_show_info, width=37, height=17, bg='#F4F3F1', font='Arial 17 bold',
                             yscrollcommand=scrollbar.set)
    if program_data["products"]:
        for item in sorted(program_data["products"]):
            show_info = f"{item}:\n"
            show_all_products.insert(END, show_info)
            if not program_data['products']:
                items = f"{4 * ' '}phone numbers:{2 * ' '}" \
                        f"None\n\n"
                show_all_products.insert(END, items)
            elif program_data['products']:
                items = f"{4 * ' '}phone numbers:{2 * ' '}" \
                        f"{', '.join(program_data['products'])}\n\n"
                show_all_products.insert(END, items)

    else:
        show_all_products.insert('1.0', "Currently there aren't any products. You must add them manually.")
    show_all_products.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=show_all_products.yview())
    show_all_products.config(state=DISABLED, pady=3)


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
window_frame.configure(bg='#A49E97')

# adding a frame in the middle of screen to show result of buttons
frame_window = Frame(window_frame, width=app_width // 2, height=450, bg='#F4F3F1')
frame_window.place(x=230, y=80)


distributors = Button(window_frame, text='Distributors', bd=3, font='Arial 18 bold', width=12,
                      command=update_distributors)
distributors.place(x=0, y=0)


add_extra_distributors = Button(window_frame, text='Add Distributor', bd=3, font='Arial 11 bold', bg='#40FA5A',
                                width=17, command=lambda: add_new_distributor(program_data, update_distributors))
add_extra_distributors.place(x=-1, y=50)


remove_distributor = Button(window_frame, text='Remove Distributor', font='Arial 11 bold', bd=3, width=17,
                            bg='red', command=lambda: delete_distributor(program_data, update_distributors))
remove_distributor.place(x=-1, y=142)


add_phone_number = Button(window_frame, text='Add phone-number', bd=3, font='Arial 11 bold',
                          width=17, command=lambda: add_new_phone_number(program_data, update_distributors))
add_phone_number.place(x=-1, y=81)


remove_phone_number = Button(window_frame, text='Remove phone-number', bd=3, font='Arial 10 bold',
                             width=19, command=lambda: delete_phone_number(program_data, update_distributors))
remove_phone_number.place(x=0, y=113)


products = Button(window_frame, text='Products', width=14, bd=3, font='Arial 16 bold', command=update_products)
products.place(x=0, y=170)


program_data = read_json()
window_frame.mainloop()
save_on_close(program_data)
