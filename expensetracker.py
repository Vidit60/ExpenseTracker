import tkinter as tk
from tkinter import ttk
import pandas as pd

# Create the main window
root = tk.Tk()
root.title('Expense Tracker')
root.geometry('800x400')  # Width x Height

# DataFrame to store expenses
expenses_df = pd.DataFrame(columns=['Date', 'Payee', 'Description', 'Amount', 'Mode of Payment'])

# Function placeholders for button commands
def add_expense():
    pass

def delete_expense():
    pass

def clear_fields():
    pass

def edit_expense():
    pass

def convert_expense_to_sentence():
    pass

def view_selected_expense_details():
    pass

# GUI Components
# Left side of the GUI
date_label = tk.Label(root, text='Date (M/DD/YY):')
date_label.grid(row=0, column=0, sticky='E')
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1)

description_label = tk.Label(root, text='Description:')
description_label.grid(row=1, column=0, sticky='E')
description_entry = tk.Entry(root)
description_entry.grid(row=1, column=1)

amount_label = tk.Label(root, text='Amount:')
amount_label.grid(row=2, column=0, sticky='E')
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1)

payee_label = tk.Label(root, text='Payee:')
payee_label.grid(row=3, column=0, sticky='E')
payee_entry = tk.Entry(root)
payee_entry.grid(row=3, column=1)

mode_of_payment_label = tk.Label(root, text='Mode of Payment:')
mode_of_payment_label.grid(row=4, column=0, sticky='E')
mode_of_payment_options = ['Cash', 'Credit Card', 'Debit Card', 'Google Pay']
mode_of_payment_var = tk.StringVar(root)
mode_of_payment_var.set(mode_of_payment_options[0])  # default value
mode_of_payment_dropdown = tk.OptionMenu(root, mode_of_payment_var, *mode_of_payment_options)
mode_of_payment_dropdown.grid(row=4, column=1)

add_expense_button = tk.Button(root, text='Add expense', command=add_expense)
add_expense_button.grid(row=5, column=0, columnspan=2)

# Right side of the GUI
expenses_treeview = ttk.Treeview(root, columns=list(expenses_df.columns), show='headings')
for col in expenses_df.columns:
    expenses_treeview.heading(col, text=col)
expenses_treeview.grid(row=0, column=2, rowspan=4, sticky='NSEW')

delete_expense_button = tk.Button(root, text='Delete Expense', command=delete_expense)
delete_expense_button.grid(row=5, column=2)

clear_fields_button = tk.Button(root, text='Clear Fields', command=clear_fields)
clear_fields_button.grid(row=6, column=0, columnspan=2)

edit_expense_button = tk.Button(root, text='Edit Selected Expense', command=edit_expense)
edit_expense_button.grid(row=6, column=2)

convert_to_words_button = tk.Button(root, text='Convert Expense to a sentence', command=convert_expense_to_sentence)
convert_to_words_button.grid(row=7, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
