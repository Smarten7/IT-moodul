fail = open("tulemused.txt", encoding="UTF-8")

tulemuste_tabel = []

for rida in fail: # iga rea jaoks failist
    seti_punktid = [] # kogume ühe seti punkte
    osad = rida.split() # tühikute kohalt osadeks

    for osa in osad: # osade kaupa
        seti_punktid.append(int(osa)) # järjekordsed punktid juurde

    tulemuste_tabel.append(seti_punktid) # seti punktide järjend juurde
fail.close()

print(tulemuste_tabel)

eesti = 0
soome = 0

for set in tulemuste_tabel:
    if set[0] > set[1]:
        eesti += 1
    else:
        soome += 1

if eesti > soome:
    võitja = "Eesti"
    võitja_punktid = eesti
    kaotaja_punktid = soome
else:
    võitja = "Soome"
    võitja_punktid = soome
    kaotaja_punktid = eesti
print(str(võitja) + " võitis " + str(võitja_punktid) + "-" + str(kaotaja_punktid))