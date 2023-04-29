import tkinter as tk
from tkinter import ttk
# from funkcijas import *
# Create the main window
root = tk.Tk()
root.title("Degvielas Kalkulators")

def paterins():
    degv = float(degvieldaudz.get())
    km = float(km_nobr.get())
    pat=(degv*100)/km
    print(pat)
    Degvielas_pat_sk.config(text=f"{pat:.2f} l/100")

# Laiks patērēts atkļūdošanā = 2h
#sendhelp


def nobrAtt():
    degv = float(degvdaudz2_ievade.get())
    pat = float(Degv_pat_sk2.get())
    km_nobraucamais = (degv/pat)*100

    KM_sk.config(text=f"{km_nobraucamais:.2f} km")


def DegvDaudzums():
    pat = float(Degv_pat_sk.get())
    km = float(km_sk.get())
    degv=(pat*km)/100
    degvdaudz.config(text=f"{degv:.2f} L")



notebook = ttk.Notebook(root)


DegvielasPaterins = ttk.Frame(notebook)
NobrAtt = ttk.Frame(notebook)
NepDegv = ttk.Frame(notebook)

# tab 1
notebook.add(DegvielasPaterins, text="Degvielas patēriņs L/100")

degv_label = tk.Label(DegvielasPaterins, text="Degvielas daudzums (L):")
degv_label.grid(row=0, column=0)

degvieldaudz= tk.Entry(DegvielasPaterins)
degvieldaudz.grid(row=0, column=1)

km_skaits_label = tk.Label(DegvielasPaterins, text="Nobrauktie KM:")
km_skaits_label.grid(row=1, column=0)

km_nobr = tk.Entry(DegvielasPaterins)
km_nobr.grid(row=1, column=1)

apr_button = tk.Button(DegvielasPaterins, text="Aprēķināt", command=lambda:paterins())
apr_button.grid(row=2, column=0, columnspan=2)

Degv_pat_label = tk.Label(DegvielasPaterins, text="Patērņš (l/100km) = ")
Degv_pat_label.grid(row=3, column=0)
Degvielas_pat_sk = tk.Label(DegvielasPaterins,text="")
Degvielas_pat_sk.grid(row=3, column=1)

# tab 2
notebook.add(NobrAtt, text="Nobraucamais attālums")
degv_label = tk.Label(NobrAtt, text="Degvielas daudzums (L):")
degv_label.grid(row=0, column=0)

degvdaudz2_ievade = tk.Entry(NobrAtt)
degvdaudz2_ievade.grid(row=0, column=1)

Degv_pat_label = tk.Label(NobrAtt, text="Degvielas Patēriņš L/100:")
Degv_pat_label.grid(row=1, column=0)

Degv_pat_sk2 = tk.Entry(NobrAtt)
Degv_pat_sk2.grid(row=1, column=1)

apr_button = tk.Button(NobrAtt, text="Aprēķināt", command=lambda:nobrAtt())
apr_button.grid(row=2, column=0, columnspan=2)

KM_sk_label = tk.Label(NobrAtt, text="Nobraucamais attālums = ")
KM_sk_label.grid(row=3, column=0)
KM_sk = tk.Label(NobrAtt, text="")
KM_sk.grid(row=3, column=1)

# tab 3
notebook.add(NepDegv, text="Nepieciešamā Degviela")

Degv_pat_label = tk.Label(NepDegv, text="Degvielas Patēriņš L/100:")
Degv_pat_label.grid(row=0, column=0)

Degv_pat_sk = tk.Entry(NepDegv)
Degv_pat_sk.grid(row=0, column=1)

km_sk_label = tk.Label(NepDegv, text="Attālums KM:")
km_sk_label.grid(row=1, column=0)

km_sk = tk.Entry(NepDegv)
km_sk.grid(row=1, column=1)

apr_button = tk.Button(NepDegv, text="Aprēķināt", command=lambda:DegvDaudzums())
apr_button.grid(row=2, column=0, columnspan=2)

degvdaudz_label = tk.Label(NepDegv, text="Nepieciešamā degviela = ")
degvdaudz_label.grid(row=3, column=0)
degvdaudz = tk.Label(NepDegv, text="")
degvdaudz.grid(row=3, column=1)



notebook.pack(expand=1, fill="both")


root.mainloop()
