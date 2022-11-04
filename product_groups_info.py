from tkinter import *


def show_products_information(window_frame, read_careful_message):
    """
    param window_frame: Is the main window frame, so the label can be positioned.
    param read_careful_message: Is the label that is positioned right above the text frame.
    This function shows all the information about PRODUCT groups.
    """
    read_careful_message['text'] = f"Read carefully"
    products_show_info = Frame(window_frame, width=67, height=29, bg='#F4F3F1')
    products_show_info.place(x=230, y=80)

    show_all_products = Text(products_show_info, width=38, height=17, bg='#F4F3F1', font='Arial 17 bold')
    show_info = f"Group 1 of products is for FOOD only.\n\n" \
                f"Group 2 of products is for DRINKS only.\n\n" \
                f"Group 3 of products is for ALCOHOL only.\n\n" \
                f"You must insert correct product group when adding new item.\n\n" \
                f"For example you add item ~Potatoes~ and you must select group 1, since potatoes are food.\n\n" \
                f"Groups are selected with raw numbers: 1, 2 or 3"
    show_all_products.insert(END, show_info)
    show_all_products.pack(side=LEFT, fill=BOTH)
    show_all_products.config(state=DISABLED, padx=3, pady=3)