# pat=0
cena=0
degv=5
km=100
kmvec=0
kmjaun=1008546

def nobraukums(kmvec,kmjaun):
    kmvec-kmjaun
    return 


def degvpaterins(degv,km):
    # km=kmjaun-kmvec
    pat=(degv*100)/km
    return pat

def vajagDeg(km, pat):
    return (pat / 100) * km

def pirkcena():
    degv*cena
    return
def kmArDegv(pat, degv):
    return (degv / (pat / 100))

def BraucCena(Km, pat, cena):
    degv = (pat / 100) * km
    return degv * cena


print(degvpaterins(degv,km), " l/100")
print(vajagDeg(200,5.5), "l")

print(kmArDegv(5,5),"km")

print(BraucCena(100,5,1.60))

def paterins():
    degv = float(degvdaudz_ievade.get())
    km = float(km_nobr.get())
    pat=(degv*100)/km

    Degv_pat_sk.config(text=f"{pat:.2f} L/100Km")
    return pat
    
def nobrAtt():
    degv = float(degvdaudz_ievade.get())
    pat = float(Degv_pat_sk.get())
    km_nobr = (pat*degv)/100

    KM_sk.config(text=f"{km_nobr:.2f} km")


def DegvDaudzums():
    pat = float(Degv_pat_sk.get())
    km = float(km_sk.get())
    degv=(pat*km)/100
    degvdaudz.config(text=f"{degv:.2f} km")