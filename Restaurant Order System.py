from tkinter import *
from tkinter import messagebox
import webbrowser

myframe = Tk()
myframe.title("Restaurant Order System")
myframe.geometry("400x320")

def open_menu_link():
    webbrowser.open("https://www.google.com/search?q=restaurant+menu+online")

def place_order():
    table_number = entry_table.get()
    order_item = entry_order.get()
    
    if table_number and order_item:
        print(f"Table {table_number} placed order: {order_item}")
        messagebox.showinfo("Order Sent", f"Order for Table {table_number} has been sent to the kitchen.")
    else:
        messagebox.showwarning("Missing Details", "Please enter Table number and your Order.")

def exit_app():
    myframe.quit()

myframe.columnconfigure(1, weight=1) 
myframe.rowconfigure(4, weight=1)

header_label = Label(myframe, text="Restaurant Order System", font="Arial 16 bold")
header_label.grid(row=0, column=0, columnspan=2, pady=(20, 15), sticky=N)

lbl_table = Label(myframe, text="Table No:", font="Arial 10")
lbl_table.grid(row=1, column=0, padx=(20, 5), pady=5, sticky=W) 

entry_table = Entry(myframe, width=25)
entry_table.grid(row=1, column=1, padx=(5, 20), pady=5, sticky=E+W)

lbl_order = Label(myframe, text="Your Order:", font="Arial 10")
lbl_order.grid(row=2, column=0, padx=(20, 5), pady=5, sticky=W)

entry_order = Entry(myframe, width=25)
entry_order.grid(row=2, column=1, padx=(5, 20), pady=5, sticky=E+W)

btn_order = Button(
    myframe, 
    text="Place Order", 
    font="Arial 12 bold", 
    command=place_order
)
btn_order.grid(row=3, column=0, columnspan=2, pady=(15, 10), sticky=E+W, padx=20) 

btn_menu = Button(
    myframe, 
    text="View Menu", 
    font="Arial 10", 
    command=open_menu_link
)
btn_menu.grid(row=4, column=0, pady=(5, 15), padx=20, sticky=W)

btn_exit = Button(
    myframe, 
    text="Exit System", 
    font="Arial 10 bold", 
    command=exit_app
)
btn_exit.grid(row=4, column=1, pady=(5, 15), padx=20, sticky=E)

myframe.mainloop()