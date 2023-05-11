

def paterins():
    degv = float(degvieldaudz.get().replace(",", "."))
    km = float(km_nobr.get().replace(",", "."))
    pat=(degv*100)/km
    Degvielas_pat_sk.config(text=f"{pat:.2f} l/100")

# Laiks patērēts atkļūdošanā = 4h
# sendhelp


def nobrAtt():
    degv = float(degvdaudz2_ievade.get().replace(",", "."))
    pat = float(Degv_pat_sk2.get().replace(",", "."))
    km_nobraucamais = (degv/pat)*100

    KM_sk.config(text=f"{km_nobraucamais:.2f} km")


def DegvDaudzums():
    pat = float(Degv_pat_sk.get().replace(",", "."))
    km = float(km_sk.get().replace(",", "."))
    degv=(pat*km)/100
    degvdaudz.config(text=f"{degv:.2f} L")
