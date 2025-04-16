import tkinter as tk
from tkinter import messagebox

# Function to calculate delivery charge
def calculate_charge():
    try:
        weight = float(weight_entry.get())
        location = location_var.get()

        if location == "Ibeju-Lekki":
            if weight >= 10:
                charge = 5000
            else:
                charge = 3500
        elif location == "Epe":
            if weight >= 10:
                charge = 10000
            else:
                charge = 5000
        else:
            messagebox.showerror("Invalid Location", "Please select a valid location.")
            return

        result_label.config(text=f"Delivery charge: ₦{charge:,}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid weight (number).")

# GUI window
window = tk.Tk()
window.title("Simi Services Delivery Charge Calculator")
window.geometry("350x250")

# Location input
tk.Label(window, text="Select Location:").pack(pady=5)
location_var = tk.StringVar()
location_menu = tk.OptionMenu(window, location_var, "Ibeju-Lekki", "Epe")
location_menu.pack()

# Weight input
tk.Label(window, text="Enter Package Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(window)
weight_entry.pack()

# Calculate button
tk.Button(window, text="Calculate Charge", command=calculate_charge).pack(pady=10)

# Result label
result_label = tk.Label(window, text="Delivery charge: ₦0")
result_label.pack(pady=10)

window.mainloop()
