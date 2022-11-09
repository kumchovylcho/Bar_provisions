from tkinter import *
from extra_options.limit_of_windows import *
from extra_options.state_of_button import check_state_of_button
from tkinter import messagebox


def delete_product(program_data, update_products):
    """
    param program_data: Is the information that json file holds.
    param update_products_screen: Is a function which updates the screen with current products.
    This function checks if there are any opened side windows before it creates new one.
    If there are no windows opened then the if statement is executed.
    The product entry is bound and when any character is pressed in the entry, there is a callback to a function
    which checks if the entry is empty or not.
    If the entry has more than 0 character inside, the button state turns ON.
    """
    if check_if_opened():
        remove_product_window = Tk()
        remove_product_window.title("Delete product")
        remove_product_window.geometry('250x150+800+400')
        remove_product_window.resizable(False, False)
        remove_product_window.config(bg='#A49E97')
        Label(remove_product_window, bd=3, text='Select product', font='Arial 15 bold', bg='#FFCCA7',
              width=20).pack()
        product = Entry(remove_product_window, bd=3, width=50, bg='powder blue', font='Arial 30 bold')
        product.pack()
        delete_product_button = Button(remove_product_window, text='Remove product', bd=3,
                                       font='Arial 15 bold', bg='grey', state='disabled',
                                       command=lambda: delete_product_validation(program_data, update_products, product,
                                                                                 remove_product_window))
        delete_product_button.pack()
        remove_product_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(remove_product_window))
        color_of_delete_button = 'red'
        product.bind('<KeyRelease>', lambda message: check_state_of_button(product, delete_product_button,
                                                                           color_of_delete_button))


def delete_product_validation(program_data, update_products, product, window):
    """
    param program_data: Is the information that json file holds.
    param update_products_screen: Is a function which updates the screen with current products.
    param product: Is the product that the user has written and is capitalized for more readability.
    param window: Is the window created in function delete_product, which will be closed after the code below is
    executed.
    First the function checks if the product exists in any of the food,drinks or alcohol groups.
    If the product exists in any of those, a question appears.
    If you answer the question with 'yes', the product written by the user is deleted with its quantities and price.
    If the product does not exist, a special message will follow.
    """
    product = product.get().capitalize()
    if product in program_data['products']['food'] or product in program_data['products']['drinks'] or \
            product in program_data['products']['alcohol']:
        question = messagebox.askquestion("Confirm", f"Do you want to delete {product} from the database? "
                                          f"Deleting {product} will delete its quantities and price.")
        if question == 'yes':
            if product in program_data['products']['food']:
                del program_data['products']['food'][product]
            elif product in program_data['products']['drinks']:
                del program_data['products']['drinks'][product]
            elif product in program_data['products']['alcohol']:
                del program_data['products']['alcohol'][product]
            messagebox.showinfo("Deleted", f"{product} has been successfully deleted.")
    else:
        messagebox.showinfo('Invalid', f"{product} does not exist in the database.")
    window.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_products()
