def kala_kaal(pikkus, fti):
    kaal = (int(pikkus)**3 * fti/100)
    return(round(kaal))

fail = str(input("Sisesta failinimi: "))

alammõõt = int(input("Sisesta püügi alammõõt: "))

fti = float(input("Sisesta Fultoni tüsedusindeks: "))

f = open(fail, "r")

kaalud = []
for rida in f:
    if int(rida) < alammõõt:
        print("Kala lasti vette tagasi")
    else:
        kaal = kala_kaal(rida, fti)
        print(kaal)
        kaalud += [kaal]

print(round(max(kaalud)/1000, 3))