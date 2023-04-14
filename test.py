import tkinter as tk
fuel_level=0
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

distance_label = tk.Label(root, text="Distance (km):")
distance_label.grid(row=0, column=0)

distance_entry = tk.Entry(root)
distance_entry.grid(row=0, column=1)

fuel_consumption_label = tk.Label(root, text="Fuel Consumption (L/100km):")
fuel_consumption_label.grid(row=1, column=0)

fuel_consumption_entry = tk.Entry(root)
fuel_consumption_entry.grid(row=1, column=1)

fuel_price_label = tk.Label(root, text="Fuel Price ($/L):")
fuel_price_label.grid(row=2, column=0)

fuel_price_entry = tk.Entry(root)
fuel_price_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate_trip)
calculate_button.grid(row=3, column=0, columnspan=2)

fuel_used_label = tk.Label(root, text="")
fuel_used_label.grid(row=4, column=0)

trip_cost_label = tk.Label(root, text="")
trip_cost_label.grid(row=5, column=0)

fuel_range_label = tk.Label(root, text="")
fuel_range_label.grid(row=6, column=0)

root.mainloop()
