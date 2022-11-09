from tkinter import *
from extra_options.state_of_button import check_state_of_button
from extra_options.limit_of_windows import *
from tkinter import messagebox


def add_new_product(program_data, update_products):
    """
    param program_data: Is the information that json file holds.
    param update_products: Is a function which updates the screen after the ADD button is clicked, and it will be called
    after the product_validation.
    This functions opens up a window with 3 labels describing what to fill in the empty blanks.
    There are 2 entries where the user can fill in the new product and the product group(where the product belongs to).

    """
    if check_if_opened():
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
        add_button = Button(add_product_window, font='Arial 20 bold', text='ADD', bd=3, bg='grey', state='disabled',
                            command=lambda: product_validation(program_data, update_products, add_product_window,
                                                               product_name,
                                                               product_group))
        add_button.pack()
        add_product_window.protocol('WM_DELETE_WINDOW', lambda: ask_to_close_window(add_product_window))
        color_of_add_button = '#40FA5A'
        product_name.bind('<KeyRelease>',
                          lambda message: check_state_of_button(product_name, product_group, add_button,
                                                                color_of_add_button))
        product_group.bind('<KeyRelease>',
                           lambda message: check_state_of_button(product_name, product_group, add_button,
                                                                 color_of_add_button))


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
    add_product_window.destroy()
    # goes into limit_of_windows function
    limit_of_windows['is opened'] = False
    update_products()
