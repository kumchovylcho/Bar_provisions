from tkinter import *
from tkinter import messagebox
from product_operations.quantity_and_price_validation import check_for_number

limit_of_windows = 1


def ask_to_close_window(window):
    """
    param window: Is the window that will be closed if the user selects yes on the message box.
    This function checks if the user tries to close the window with X button or alt-f4.
    The only way to close the window is selecting yes from the message box or going through the steps of the button.
    """
    global limit_of_windows
    question = messagebox.askokcancel('Confirm', 'Do you want to close the window ?')
    if question:
        limit_of_windows -= 1
        window.destroy()


def add_quantity(program_data, update_products_screen):
    global limit_of_windows
    """
    param program_data: Is the information that json file holds.
    param update_products_screen: Is a function which updates the screen with current products.
    This function makes a window where you can write your product name and quantity to add.
    After the ADD button is clicked, the information the user has written is sent to quantity_and_product_validation
    function for validation.
    """
    if limit_of_windows < 2:
        limit_of_windows += 1
        add_quantity_window = Tk()
        add_quantity_window.title("Add quantity")
        add_quantity_window.resizable(False, False)
        add_quantity_window.geometry('340x300+800+400')
        add_quantity_window.config(bg='#A49E97')
        Label(add_quantity_window, text='Choose the product', bg='#FFCCA7', width=20, font='Arial 20 bold').pack()
        product_name = Entry(add_quantity_window, font='Arial 30 bold', bg='powder blue')
        product_name.pack()
        Label(add_quantity_window, text='Add the wanted quantity', bg='#FFCCA7', width=25, font='Arial 19 bold').pack()
        quantity_added = Entry(add_quantity_window, font='Arial 30 bold', bg='powder blue')
        quantity_added.pack()
        Label(add_quantity_window, text='Tip: Product name can be typed with lowercase letters.',
              font='Arial 9 bold').pack()
        Button(add_quantity_window, font='Arial 20 bold', text='ADD', bd=3, bg='#40FA5A',
               command=lambda: quantity_and_product_validation(program_data, update_products_screen, product_name,
                                                               quantity_added, add_quantity_window)).pack()
        add_quantity_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(add_quantity_window))


def quantity_and_product_validation(program_data, update_products_screen, product_name, quantity_added,
                                    window_to_close):
    global limit_of_windows
    """
    param program_data: Is the information that json file holds.
    param update_products_screen: Is a function which updates the screen with current products.
    param product_name: Is the product that the user has filled in the blank. First letter will be capitalized.
    param quantity: Is the quantity that the user has filled in the blank.
    param window_to_close: Is the window that has been made in function add_quantity, which will be closed after
    the validation process.
    It checks if the blanks that the user has written are not empty. If one of the two blanks is empty, then an error
    message will pop up.
    After that it checks if the product name exists in any of the product groups. If it exists then the quantity
    is added to the desired product.
    If the product name does not exist, an error message will pop up.
    """
    product_name, quantity_added = product_name.get().capitalize(), quantity_added.get()
    quantity = check_for_number(quantity_added)
    if product_name:
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
    elif not product_name or not quantity:
        messagebox.showinfo('Invalid', "I can't work with empty blanks."
                                       "Please fill in correct information.")
    window_to_close.destroy()
    limit_of_windows -= 1
    update_products_screen()
