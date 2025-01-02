import tkinter as tk
from tkinter import ttk

def convert():
    try:
        input_value = float(entry.get())
        from_unit = from_combobox.get()
        to_unit = to_combobox.get()
        
        conversion_factors = {
            'Kilometers': 1000,
            'Meters': 1,
            'Centimeters': 0.01,
            'Millimeters': 0.001,
        }
        
        result = input_value * conversion_factors[from_unit] / conversion_factors[to_unit]
        result_label.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        result_label.config(text="Invalid input! Please enter a number.")

# Create the main window
app = tk.Tk()
app.title("Unit Converter")
app.geometry("300x250")

# Input field
entry_label = tk.Label(app, text="Enter value:")
entry_label.pack(pady=5)
entry = tk.Entry(app, width=20)
entry.pack(pady=5)

# From unit combobox
from_label = tk.Label(app, text="From:")
from_label.pack(pady=5)
from_combobox = ttk.Combobox(app, values=["Kilometers", "Meters", "Centimeters", "Millimeters"])
from_combobox.pack(pady=5)
from_combobox.current(1)

# To unit combobox
to_label = tk.Label(app, text="To:")
to_label.pack(pady=5)
to_combobox = ttk.Combobox(app, values=["Kilometers", "Meters", "Centimeters", "Millimeters"])
to_combobox.pack(pady=5)
to_combobox.current(2)

# Convert button
convert_button = tk.Button(app, text="Convert", command=convert)
convert_button.pack(pady=10)

# Result label
result_label = tk.Label(app, text="Result: ", font=("Arial", 12))
result_label.pack(pady=10)

# Run the application
app.mainloop()
