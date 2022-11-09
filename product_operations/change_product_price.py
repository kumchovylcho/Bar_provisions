from tkinter import *
from extra_options.limit_of_windows import *
from extra_options.state_of_button import check_state_of_button
from extra_options.quantity_and_price_validation import check_for_number
from tkinter import messagebox


def change_price(program_data, update_products):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen with all products.
    This function checks if there are any opened side windows before it creates new one.
    If there are no windows opened then the if statement is executed.
    The entries are bound together and each time a key is pressed inside them, there is a callback to a function
    which checks if the entry is empty or not.
    If both entries has more than 1 character inside, the button state turns ON.
    If you try to close the window with X, a special question will follow, which you can answer with yes/no.
    """
    if check_if_opened():
        change_price_window = Tk()
        change_price_window.title("Change price")
        change_price_window.geometry('250x250+800+400')
        change_price_window.resizable(False, False)
        change_price_window.config(bg='#A49E97')
        Label(change_price_window, bd=3, text='Choose product', font='Arial 22 bold', bg='#FFCCA7',
              width=20).pack()
        entry_product = Entry(change_price_window, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
        entry_product.pack()
        Label(change_price_window, bd=3, text='Select new price', font='Arial 22 bold', bg='#FFCCA7',
              width=20).pack()
        entry_price = Entry(change_price_window, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
        entry_price.pack()
        change_price_button = Button(change_price_window, text='Change price', bd=3,
                                     font='Arial 15 bold', bg='grey', state='disabled',
                                     command=lambda: check_product(program_data, update_products, entry_product,
                                                                   entry_price,
                                                                   change_price_window))
        change_price_button.pack()
        change_price_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(change_price_window))
        color_of_delete_button = 'red'
        entry_product.bind('<KeyRelease>', lambda message: check_state_of_button(entry_product, entry_price,
                                                                                 change_price_button,
                                                                                 color_of_delete_button))
        entry_price.bind('<KeyRelease>', lambda message: check_state_of_button(entry_product, entry_price,
                                                                               change_price_button,
                                                                               color_of_delete_button))


def check_product(program_data, update_products, product, price, window):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen with all products.
    param product: Is the product that the user has written.
    param price: Is the price that the user has written.
    param window: Is the window that has been created in function change_price, which will be closed
    after the code below is executed.
    First it checks if the price written from the user is a valid float or integer.
    Then it checks if the product exists in json file.
    If the product does not exist in the json file, a special message will follow.
    If the price written by the user is not valid, a special error message will follow.
    """
    product_name, new_price = product.get().capitalize(), price.get()
    current_price = check_for_number(new_price)
    if isinstance(current_price, (int, float)):
        if product_name in program_data['products']['food']:
            messagebox.showinfo("Changed price", f"Product {product_name} price has been changed from"
                                                 f" {program_data['products']['food'][product_name]['price']} to "
                                                 f"{current_price}")
            program_data['products']['food'][product_name]['price'] = current_price
        elif product_name in program_data['products']['drinks']:
            messagebox.showinfo("Changed price", f"Product {product_name} price has been changed from"
                                                 f" {program_data['products']['drinks'][product_name]['price']} to "
                                                 f"{current_price}")
            program_data['products']['drinks'][product_name]['price'] = current_price
        elif product_name in program_data['products']['alcohol']:
            messagebox.showinfo("Changed price", f"Product {product_name} price has been changed from"
                                                 f" {program_data['products']['alcohol'][product_name]['price']} to "
                                                 f"{current_price}")
            program_data['products']['alcohol'][product_name]['price'] = current_price
        else:
            messagebox.showerror('Invalid', f"{product_name} does not exist in the database."
                                            f"Please add the product before you change its price.")
    else:
        messagebox.showerror('Invalid', f"{new_price} must be integer or float number.")
    window.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_products()