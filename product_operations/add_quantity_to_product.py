from tkinter import *
from extra_options.quantity_and_price_validation import check_for_number
from extra_options.state_of_button import check_state_of_button
from extra_options.limit_of_windows import *
from tkinter import messagebox


def add_quantity(program_data, update_products_screen):
    """
    param program_data: Is the information that json file holds.
    param update_products_screen: Is a function which updates the screen with current products.
    This function checks if there are any opened side windows before it creates new one.
    If there are no windows opened then the if statement is executed.
    Then makes a window where you can write your product name and quantity to add.
    The entries are bound together and each time a key is pressed inside them, there is a callback to a function
    which checks if the entry is empty or not.
    If both entries has more than 0 characters inside, the button state turns ON.
    After the ADD button is clicked, the information the user has written is sent to quantity_and_product_validation
    function for validation.
    """
    if check_if_opened():
        add_quantity_window = Tk()
        add_quantity_window.title("Add quantity")
        add_quantity_window.resizable(False, False)
        add_quantity_window.geometry('340x270+800+400')
        add_quantity_window.config(bg='#A49E97')
        Label(add_quantity_window, text='Choose the product', bg='#FFCCA7', width=20, font='Arial 20 bold').pack()
        product_name = Entry(add_quantity_window, font='Arial 30 bold', bg='powder blue')
        product_name.pack()
        Label(add_quantity_window, text='Add the wanted quantity', bg='#FFCCA7', width=25, font='Arial 19 bold').pack()
        quantity_added = Entry(add_quantity_window, font='Arial 30 bold', bg='powder blue')
        quantity_added.pack()
        Label(add_quantity_window, text='Tip: Product name can be typed with lowercase letters.',
              font='Arial 9 bold').pack()
        add_button = Button(add_quantity_window, font='Arial 20 bold', text='ADD', bd=3, bg='grey', state='disabled',
                            command=lambda: quantity_and_product_validation(program_data, update_products_screen,
                                                                            product_name,
                                                                            quantity_added, add_quantity_window))
        add_button.pack()
        color_of_add_button = '#40FA5A'
        add_quantity_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(add_quantity_window))
        product_name.bind('<KeyRelease>',
                          lambda message: check_state_of_button(product_name, quantity_added, add_button,
                                                                color_of_add_button))
        quantity_added.bind('<KeyRelease>',
                            lambda message: check_state_of_button(product_name, quantity_added, add_button,
                                                                  color_of_add_button))


def quantity_and_product_validation(program_data, update_products_screen, product_name, quantity_added,
                                    window_to_close):
    """
    param program_data: Is the information that json file holds.
    param update_products_screen: Is a function which updates the screen with current products.
    param product_name: Is the product that the user has filled in the blank. First letter will be capitalized.
    param quantity: Is the quantity that the user has filled in the blank.
    param window_to_close: Is the window that has been made in function add_quantity, which will be closed after
    the validation process.
    After that it checks if the product name exists in any of the product groups. If it exists then the quantity
    is added to the desired product.
    If the product name does not exist, an error message will pop up.
    """
    product_name, quantity_added = product_name.get().capitalize(), quantity_added.get()
    quantity = check_for_number(quantity_added)
    if isinstance(quantity, (int, float)):
        if product_name in program_data['products']['food']:
            program_data['products']['food'][product_name]['quantity'] += quantity
        elif product_name in program_data['products']['drinks']:
            program_data['products']['drinks'][product_name]['quantity'] += quantity
        elif product_name in program_data['products']['alcohol']:
            program_data['products']['alcohol'][product_name]['quantity'] += quantity
        else:
            messagebox.showerror('Invalid', f"{product_name} does not exist in the database."
                                            f"Please add the product before you add quantity.")
        if product_name in program_data['products']['food'] or \
                product_name in program_data['products']['drinks'] or \
                product_name in program_data['products']['alcohol']:
            messagebox.showinfo("Added", f"{quantity} quantity added to {product_name}.")
    else:
        messagebox.showerror('Invalid', f"{quantity_added} must be integer or float number.")
    window_to_close.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_products_screen()
