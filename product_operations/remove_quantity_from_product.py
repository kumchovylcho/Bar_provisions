from tkinter import *
from extra_options.quantity_and_price_validation import check_for_number
from extra_options.state_of_button import check_state_of_button
from extra_options.limit_of_windows import *
from tkinter import messagebox


def remove_quantity(program_data, update_products):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen with all products.
    This function checks if there are any opened side windows before it creates new one.
    If there are no windows opened then the if statement is executed.
    The entries are bound together and each time a key is pressed inside them, there is a callback to a function
    which checks if the entry is empty or not.
    If both entries has more than 0 characters inside, the button state turns ON.
    If you try to close the window with X, a special question will follow, which you can answer with yes/no.
    """
    if check_if_opened():
        remove_quantity_window = Tk()
        remove_quantity_window.title("Remove quantity")
        remove_quantity_window.resizable(False, False)
        remove_quantity_window.geometry('340x270+800+400')
        remove_quantity_window.config(bg='#A49E97')
        Label(remove_quantity_window, text='Choose the product', bg='#FFCCA7', width=20, font='Arial 20 bold').pack()
        product_name = Entry(remove_quantity_window, font='Arial 30 bold', bg='powder blue')
        product_name.pack()
        Label(remove_quantity_window, text='Select the amount to remove', bg='#FFCCA7', width=25,
              font='Arial 19 bold').pack()
        quantity_removed = Entry(remove_quantity_window, font='Arial 30 bold', bg='powder blue')
        quantity_removed.pack()
        Label(remove_quantity_window, text='Tip: Product name can be typed with lowercase letters.',
              font='Arial 9 bold').pack()
        add_button = Button(remove_quantity_window, font='Arial 20 bold', text='REMOVE', bd=3, bg='grey',
                            state='disabled',
                            command=lambda: remove_quantity_validation(program_data, update_products,
                                                                       product_name,
                                                                       quantity_removed, remove_quantity_window))
        add_button.pack()
        color_of_add_button = 'red'
        remove_quantity_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(remove_quantity_window))
        product_name.bind('<KeyRelease>',
                          lambda message: check_state_of_button(product_name, quantity_removed, add_button,
                                                                color_of_add_button))
        quantity_removed.bind('<KeyRelease>',
                              lambda message: check_state_of_button(product_name, quantity_removed, add_button,
                                                                    color_of_add_button))


def remove_quantity_validation(program_data, update_products, product_name, quantity_to_remove, window_to_close):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen with all products.
    param product_name: Is the product that the user has written.
    param quantity_to_remove: Is the quantity that the user wants to remove from the product.
    param window_to_close: Is the window that has been created in remove_quantity function, which will be closed
    after the code below is executed.
    First it checks if the quantity written from the user is a valid float or integer.
    Then it checks if the product exists in json file.
    If the product does not exist in the json file, a special message will follow.
    If the price written by the user is not valid, a special error message will follow.
    If the quantity you want to remove from the product goes below zero, then a special message will pop up.
    """
    product_name, quantity_to_remove = product_name.get().capitalize(), quantity_to_remove.get()
    quantity = check_for_number(quantity_to_remove)

    if isinstance(quantity, (int, float)):
        if product_name in program_data['products']['food']:
            if program_data['products']['food'][product_name]['quantity'] - quantity >= 0:
                program_data['products']['food'][product_name]['quantity'] -= quantity
                messagebox.showinfo("Removed", f"{quantity} quantity removed from {product_name}.")
            else:
                below_zero = program_data['products']['food'][product_name]['quantity'] - quantity
                messagebox.showinfo("Invalid", f"You can't have quantity that is below zero "
                                               f"{program_data['products']['food'][product_name]['quantity']}"
                                               f" - {quantity} = {below_zero:.2f}")
        elif product_name in program_data['products']['drinks']:
            if program_data['products']['drinks'][product_name]['quantity'] - quantity >= 0:
                program_data['products']['drinks'][product_name]['quantity'] -= quantity
                messagebox.showinfo("Removed", f"{quantity} quantity removed from {product_name}.")
            else:
                below_zero = program_data['products']['drinks'][product_name]['quantity'] - quantity
                messagebox.showinfo("Invalid", f"You can't have quantity that is below zero "
                                               f"{program_data['products']['drinks'][product_name]['quantity']}"
                                               f" - {quantity} = {below_zero:.2f}")
        elif product_name in program_data['products']['alcohol']:
            if program_data['products']['alcohol'][product_name]['quantity'] - quantity >= 0:
                program_data['products']['alcohol'][product_name]['quantity'] -= quantity
                messagebox.showinfo("Removed", f"{quantity} quantity removed from {product_name}.")
            else:
                below_zero = program_data['products']['alcohol'][product_name]['quantity'] - quantity
                messagebox.showinfo("Invalid", f"You can't have quantity that is below zero "
                                               f"{program_data['products']['alcohol'][product_name]['quantity']}"
                                               f" - {quantity} = {below_zero:.2f}")
        else:
            messagebox.showerror('Invalid', f"{product_name} does not exist in the database."
                                            f"Please add the product before you remove quantity.")
    else:
        messagebox.showerror('Invalid', f"{quantity_to_remove} must be integer or float number.")

    window_to_close.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_products()
