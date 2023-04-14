import tkinter as tk
from tkinter import ttk
from funkcijas import *
# Create the main window
root = tk.Tk()
root.title("Degvielas Kalkulators")

# Create the notebook widget for the tabs
notebook = ttk.Notebook(root)

# Create the tabs
DegvielasPaterins = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)

# Add the tabs to the notebook
notebook.add(DegvielasPaterins, text="Degvielas patēriņs L/100")
degv_ievade = tk.Label(DegvielasPaterins, text="Degvielas daudzums (L):")
degv_ievade.grid(row=0, column=0)

degv = tk.Entry(DegvielasPaterins)
degv.grid(row=0, column=1)

fuel_consumption_label = tk.Label(DegvielasPaterins, text="Nobrauktais KM:")
fuel_consumption_label.grid(row=1, column=0)

km = tk.Entry(DegvielasPaterins)
km.grid(row=1, column=1)

calculate_button = tk.Button(DegvielasPaterins, text="Aprēķināt", command=lambda:paterins(float(degv),float(km)))
calculate_button.grid(row=2, column=0, columnspan=2)

fuel_range_label = tk.Label(DegvielasPaterins, text="")
fuel_range_label.grid(row=3, column=0)
notebook.add(tab2, text="Tab 2")
notebook.add(tab3, text="Tab 3")

# Add some widgets to the tabs
# tk.Label(tab1, text="This is Tab 1").pack(pady=10)
tk.Label(tab2, text="This is Tab 2").pack(pady=10)
tk.Label(tab3, text="This is Tab 3").pack(pady=10)

# Pack the notebook widget
notebook.pack(expand=1, fill="both")

# Start the main loop
root.mainloop()
