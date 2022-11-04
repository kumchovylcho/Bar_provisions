from tkinter import *
from tkinter import messagebox


def add_new_product(program_data, update_products):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen after the ADD button is clicked, and it will be called
    after the product_validation.
    This functions opens up a window with 3 labels describing what to fill in the empty blanks.
    There are 2 entries where the user can fill in the new product and the product group(where the product belongs to).

    """
    add_product_window = Tk()
    add_product_window.title('Add Product')
    add_product_window.resizable(False, False)
    add_product_window.geometry('340x300+800+400')
    add_product_window.config(bg='#A49E97')
    Label(add_product_window, text='Add product name', bg='#FFCCA7', width=20, font='Arial 20 bold').pack()
    product_name = Entry(add_product_window, font='Arial 30 bold', bg='powder blue')
    product_name.pack()
    Label(add_product_window, text='Choose product group', bg='#FFCCA7', width=25, font='Arial 19 bold').pack()
    product_group = Entry(add_product_window, font='Arial 30 bold', bg='powder blue')
    product_group.pack()
    Label(add_product_window, text='Group 1: Food, Group 2: Drinks, Group 3: Alcohol', font='Arial 10 bold').pack()
    Button(add_product_window, font='Arial 20 bold', text='ADD', bd=3, bg='#40FA5A',
           command=lambda: product_validation(program_data, update_products, add_product_window, product_name,
                                              product_group)).pack()


def product_validation(program_data, update_products, add_product_window, product_name, product_group):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen after the ADD button is clicked, and it will be called
    after the product_validation.
    param add_product_window: Is the window that has been made in add_new_product function, which will be closed upon
    clicking the ADD button.
    param product_name: Is the product which the user has filled in.
    param product_group: Is the group which the user has filled in.
    The product name is capitalized for more readability(making the first letter of the word capital).
    The function checks if the current product exists and if it is in the range of the existing groups.
    If both conditions are met, the product is created followed by quantities and price.
    If conditions are not met, then error messages will pop up on the screen.
    """
    current_product, product_group = product_name.get().capitalize(), product_group.get()
    all_groups = ['1', '2', '3']
    if current_product and product_group:
        if product_group == '1':
            program_data['products']['food'][current_product] = program_data['products']['food'].get(
                current_product, {'quantity': 0, 'price': 0})
        elif product_group == '2':
            program_data['products']['drinks'][current_product] = program_data['products']['drinks'].get(
                current_product, {'quantity': 0, 'price': 0})
        elif product_group == '3':
            program_data['products']['alcohol'][current_product] = program_data['products']['alcohol'].get(
                current_product, {'quantity': 0, 'price': 0})
        if product_group in all_groups:
            messagebox.showinfo('Added', f"{current_product} has been added to the database.")
        elif product_group not in all_groups:
            messagebox.showerror('Invalid', f"{product_group} is not a valid group! Please enter a valid group.")
    elif not current_product or not product_group:
        messagebox.showinfo('Not found', "I can't work with empty blanks.")
    add_product_window.destroy()
    update_products()