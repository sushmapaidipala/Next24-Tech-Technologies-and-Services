import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    email = email_entry.get()
    age = age_entry.get()
    
    if not name or not email or not age:
        messagebox.showerror("Error", "Please fill in all fields")
        return
    
    messagebox.showinfo("Success", f"Registration successful!\nName: {name}\nEmail: {email}\nAge: {age}")

root = tk.Tk()
root.title("Registration Form")

# Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=5)

# Age
age_label = tk.Label(root, text="Age:")
age_label.grid(row=2, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()