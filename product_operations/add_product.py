from tkinter import *
from tkinter import messagebox

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


def add_new_product(program_data, update_products):
    global limit_of_windows
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen after the ADD button is clicked, and it will be called
    after the product_validation.
    This functions opens up a window with 3 labels describing what to fill in the empty blanks.
    There are 2 entries where the user can fill in the new product and the product group(where the product belongs to).

    """
    if limit_of_windows < 2:
        limit_of_windows += 1
        add_product_window = Tk()
        add_product_window.title('Add Product')
        add_product_window.resizable(False, False)
        add_product_window.geometry('340x270+800+400')
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
        add_product_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(add_product_window))


def product_validation(program_data, update_products, add_product_window, product_name, product_group):
    global limit_of_windows
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
            if current_product not in program_data['products']['food'] and \
                    current_product not in program_data['products']['drinks'] and \
                    current_product not in program_data['products']['alcohol']:
                program_data['products']['food'][current_product] = {'quantity': 0, 'price': 0}
                messagebox.showinfo('Added', f"{current_product} has been added to the database.")
            elif current_product in program_data['products']['drinks'] or \
                    current_product in program_data['products']['alcohol']:
                messagebox.showerror('Invalid', f"{current_product} already exists in other product group!")
            elif current_product in program_data['products']['food']:
                messagebox.showinfo('Invalid', f"{current_product} already exists!")

        elif product_group == '2':
            if current_product not in program_data['products']['food'] and \
                    current_product not in program_data['products']['drinks'] and \
                    current_product not in program_data['products']['alcohol']:
                program_data['products']['drinks'][current_product] = {'quantity': 0, 'price': 0}
                messagebox.showinfo('Added', f"{current_product} has been added to the database.")
            elif current_product in program_data['products']['food'] or \
                    current_product in program_data['products']['alcohol']:
                messagebox.showerror('Invalid', f"{current_product} already exists in other product group!")
            elif current_product in program_data['products']['drinks']:
                messagebox.showinfo('Invalid', f"{current_product} already exists!")

        elif product_group == '3':
            if current_product not in program_data['products']['food'] and \
                    current_product not in program_data['products']['drinks'] and \
                    current_product not in program_data['products']['alcohol']:
                program_data['products']['alcohol'][current_product] = {'quantity': 0, 'price': 0}
                messagebox.showinfo('Added', f"{current_product} has been added to the database.")
            elif current_product in program_data['products']['food'] or \
                    current_product in program_data['products']['drinks']:
                messagebox.showerror('Invalid', f"{current_product} already exists in other product group!")
            elif current_product in program_data['products']['alcohol']:
                messagebox.showinfo('Invalid', f"{current_product} already exists!")

        elif product_group not in all_groups:
            messagebox.showerror('Invalid', f"{product_group} is not a valid group! Please enter a valid group.")

    elif not current_product or not product_group:
        messagebox.showinfo('Not found', "I can't work with empty blanks.")
    add_product_window.destroy()
    limit_of_windows -= 1
    update_products()
