import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()

    character_set = ''
    if use_uppercase:
        character_set += string.ascii_uppercase
    if use_lowercase:
        character_set += string.ascii_lowercase
    if use_digits:
        character_set += string.digits
    if use_special:
        character_set += string.punctuation

    if not character_set:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(character_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create labels and entry widgets
length_label = tk.Label(root, text="Length:")
length_label.grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Uppercase", variable=uppercase_var)
uppercase_check.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

lowercase_var = tk.BooleanVar()
lowercase_check = tk.Checkbutton(root, text="Lowercase", variable=lowercase_var)
lowercase_check.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

digits_var = tk.BooleanVar()
digits_check = tk.Checkbutton(root, text="Digits", variable=digits_var)
digits_check.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

special_var = tk.BooleanVar()
special_check = tk.Checkbutton(root, text="Special Characters", variable=special_var)
special_check.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

password_entry_label = tk.Label(root, text="Generated Password:")
password_entry_label.grid(row=6, column=0, padx=5, pady=5)
password_entry = tk.Entry(root)
password_entry.grid(row=6, column=1, padx=5, pady=5)

# Start the main event loop
root.mainloop()
