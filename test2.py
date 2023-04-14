import tkinter as tk
from tkinter import ttk

def calculate_trip():
    distance = float(distance_entry.get())
    fuel_consumption = float(fuel_consumption_entry.get())
    fuel_price = float(fuel_price_entry.get())

    fuel_used = (fuel_consumption / 100) * distance
    trip_cost = fuel_used * fuel_price
    fuel_range = fuel_level / (fuel_consumption / 100)

    fuel_used_label.config(text=f"{fuel_used:.2f} liters")
    trip_cost_label.config(text=f"${trip_cost:.2f}")
    fuel_range_label.config(text=f"{fuel_range:.2f} km")

root = tk.Tk()
root.title("Fuel Consumption Calculator")

# Create a Notebook widget to hold multiple tabs
notebook = ttk.Notebook(root)

# Create the first tab for the trip calculator
trip_tab = ttk.Frame(notebook)
notebook.add(trip_tab, text="Trip Calculator")

distance_label = tk.Label(trip_tab, text="Distance (km):")
distance_label.grid(row=0, column=0)

distance_entry = tk.Entry(trip_tab)
distance_entry.grid(row=0, column=1)

fuel_consumption_label = tk.Label(trip_tab, text="Fuel Consumption (L/100km):")
fuel_consumption_label.grid(row=1, column=0)

fuel_consumption_entry = tk.Entry(trip_tab)
fuel_consumption_entry.grid(row=1, column=1)

fuel_price_label = tk.Label(trip_tab, text="Fuel Price ($/L):")
fuel_price_label.grid(row=2, column=0)

fuel_price_entry = tk.Entry(trip_tab)
fuel_price_entry.grid(row=2, column=1)

calculate_button = tk.Button(trip_tab, text="Calculate", command=calculate_trip)
calculate_button.grid(row=3, column=0, columnspan=2)

fuel_used_label = tk.Label(trip_tab, text="")
fuel_used_label.grid(row=4, column=0)

trip_cost_label = tk.Label(trip_tab, text="")
trip_cost_label.grid(row=5, column=0)

fuel_range_label = tk.Label(trip_tab, text="")
fuel_range_label.grid(row=6, column=0)

# Create the second tab for the fuel range calculator
range_tab = ttk.Frame(notebook)
notebook.add(range_tab, text="Fuel Range Calculator")

fuel_level_label = tk.Label(range_tab, text="Fuel Level (L):")
fuel_level_label.grid(row=0, column=0)

fuel_level_entry = tk.Entry(range_tab)
fuel_level_entry.grid(row=0, column=1)

fuel_consumption_label = tk.Label(range_tab, text="Fuel Consumption (L/100km):")
fuel_consumption_label.grid(row=1, column=0)

fuel_consumption_entry = tk.Entry(range_tab)
fuel_consumption_entry.grid(row=1, column=1)

calculate_button = tk.Button(range_tab, text="Calculate", command=calculate_trip)
calculate_button.grid(row=2, column=0, columnspan=2)

fuel_range_label = tk.Label(range_tab, text="")
fuel_range_label.grid(row=3, column=0)

notebook.pack()

root.mainloop()
