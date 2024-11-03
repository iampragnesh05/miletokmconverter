import tkinter as tk

def calculate_km():
    miles = float(entry.get())
    km = miles * 1.60934
    result_label.config(text=f"{km:.2f} km")

# Set up the window
window = tk.Tk()
window.title("Mile to Kilometer Converter")

# Set the initial window size and minimum size
window.geometry("400x200")  # Initial size
window.minsize(400, 200)    # Minimum size

# Center the grid in the window
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

# Entry for miles input with Roboto font, centered
entry = tk.Entry(window, width=10, font=("Roboto", 14), justify="center")
entry.grid(row=0, column=1, pady=10, sticky="ew")

# Label for "mile" with Roboto font
mile_label = tk.Label(window, text="mile", font=("Roboto", 14))
mile_label.grid(row=0, column=2, padx=10, sticky="w")

# Label for "equal to" and initial km value (0 km) with Roboto font, centered
equal_label = tk.Label(window, text="is equal to", font=("Roboto", 14))
equal_label.grid(row=1, column=0, padx=10, sticky="e")

result_label = tk.Label(window, text="0 km", font=("Roboto", 14))
result_label.grid(row=1, column=1, padx=10, sticky="ew")

# Button to calculate the result with Roboto font, centered
calculate_button = tk.Button(window, text="Calculate", command=calculate_km, font=("Roboto", 14))
calculate_button.grid(row=2, column=1, pady=20, sticky="ew")

# Start the GUI loop
window.mainloop()
