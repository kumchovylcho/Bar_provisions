from read_json import *
from add_distributor import *
from delete_distributor import *
from delete_phone_number import *
from add_phone_number import *
from add_product import *
from product_groups_info import *
from tkinter import *


def update_distributors():
    global counter_of_distributors_and_products
    """
    Making a frame to use its parameters so the Text box can be positioned and the scrollbar can be added to the frame.
    The scrollbar is set to be on the right side of the text and set to be vertical.
    Making a Text widget to fill all the information about DISTRIBUTORS when the button is clicked.
    Checking if there is something inside distributors to start inserting process on the screen, if there is no
    distributors, a special message will appear.
    Showing all distributors and their phone numbers on screen with a single for loop.
    The text is positioned on the left side of the frame and made the text non-deletable(read-only), but can be copied
    with ctrl + C.
    Added counter of distributors which is placed in the top left corner of the Text frame.
    """
    counter_of_distributors_and_products['text'] = f"Total distributors: {len(program_data['distributors'])}"
    distributors_show_info = Frame(window_frame, width=67, height=29, bg='#F4F3F1')
    distributors_show_info.place(x=230, y=80)
    scrollbar = Scrollbar(distributors_show_info)
    scrollbar.pack(side=RIGHT, fill=Y)
    showing_all_distributors = Text(distributors_show_info, width=37, height=17, bg='#F4F3F1', font='Arial 17 bold',
                                    yscrollcommand=scrollbar.set)
    if program_data["distributors"]:
        indent, indent_after_phone_numbers = 4 * ' ', 2 * ' '
        for name in sorted(program_data["distributors"]):
            show_info = f"{name}:\n"
            showing_all_distributors.insert(END, show_info)
            if not program_data['distributors'][name]['phone_numbers']:
                phone_numbers = f"{indent}phone numbers:{indent_after_phone_numbers}" \
                                f"None\n\n"
                showing_all_distributors.insert(END, phone_numbers)
            elif program_data['distributors'][name]['phone_numbers']:
                phone_numbers = f"{indent}phone numbers:{indent_after_phone_numbers}" \
                                f"{', '.join(program_data['distributors'][name]['phone_numbers'])}\n\n"
                showing_all_distributors.insert(END, phone_numbers)
    elif not program_data['distributors']:
        showing_all_distributors.insert('1.0', "There are currently no distributors.")
    showing_all_distributors.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=showing_all_distributors.yview)
    showing_all_distributors.config(state=DISABLED, pady=3)


def update_products():
    """
    This function shows all products with their quantities and prices.
    It has a product counter above the frame.
    None message will appear beside the product group if there isn't any product in that group.
    If there are no products at all, then a message will appear in the text frame.
    """
    global counter_of_distributors_and_products
    total_products = len(program_data['products']['food']) + len(program_data['products']['drinks']) + \
                     len(program_data['products']['alcohol'])
    counter_of_distributors_and_products['text'] = f"Total unique products: {total_products}"
    products_show_info = Frame(window_frame, width=67, height=29, bg='#F4F3F1')
    products_show_info.place(x=230, y=80)
    scrollbar = Scrollbar(products_show_info)
    scrollbar.pack(side=RIGHT, fill=Y)
    show_all_products = Text(products_show_info, width=37, height=17, bg='#F4F3F1', font='Arial 17 bold',
                             yscrollcommand=scrollbar.set)
    integrate = 5 * ' '
    if program_data["products"]['food']:
        show_all_products.insert(END, f"Food:\n")
        for item in sorted(program_data["products"]['food']):
            show_food = f"{integrate}{item}:\n" \
                        f"{integrate * 2}quantity: {program_data['products']['food'][item]['quantity']}, " \
                        f"price: {program_data['products']['food'][item]['price']}"
            show_all_products.insert(END, f"{show_food}\n")
    else:
        show_all_products.insert(END, f"\nFood: None")
    if program_data['products']['drinks']:
        show_all_products.insert(END, f"\nDrinks:\n")
        for drink in sorted(program_data['products']['drinks']):
            show_drinks = f"{integrate}{drink}:\n" \
                          f"{integrate * 2}quantity: {program_data['products']['drinks'][drink]['quantity']}, " \
                          f"price: {program_data['products']['drinks'][drink]['price']}"
            show_all_products.insert(END, f"{show_drinks}\n")
    else:
        show_all_products.insert(END, f"\nDrinks: None\n")
    if program_data['products']['alcohol']:
        show_all_products.insert(END, f"\nAlcohol:\n")
        for alcohol in sorted(program_data['products']['alcohol']):
            show_alcohol = f"{integrate}{alcohol}:\n" \
                           f"{integrate * 2}quantity: {program_data['products']['alcohol'][alcohol]['quantity']}, " \
                           f"price: {program_data['products']['alcohol'][alcohol]['price']}"
            show_all_products.insert(END, f"{show_alcohol}\n")
    else:
        show_all_products.insert(END, f"Alcohol: None\n")
    if not program_data['products']['food'] and not program_data['products']['drinks'] \
            and not program_data['products']['alcohol']:
        show_all_products.insert('1.0', "Currently there aren't any products. You must add them manually.")
    show_all_products.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=show_all_products.yview)
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
frame_window = Frame(window_frame, width=app_width // 2, height=467, bg='#F4F3F1')
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

counter_of_distributors_and_products = Label(window_frame,
                                             text='',
                                             font='Arial 15 bold', bg='#A49E97')
counter_of_distributors_and_products.place(x=232, y=50)

products = Button(window_frame, text='Products', width=14, bd=3, font='Arial 16 bold',
                  command=update_products)
products.place(x=0, y=170)

add_product = Button(window_frame, text='Add Product', bd=3, font='Arial 16 bold', bg='#40FA5A',
                     command=lambda: add_new_product(program_data, update_products))
add_product.place(x=0, y=213)

products_information = Button(window_frame, text='Product groups info', bd=3, font='Arial 15 bold',
                              command=lambda: show_products_information(window_frame,
                                                                        counter_of_distributors_and_products))
products_information.place(x=0, y=560)

program_data = read_json()
window_frame.mainloop()
save_on_close(program_data)
