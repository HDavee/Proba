szoveg = []

with open('fajl.txt', "r") as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip(";")
        szo = {f'évszám : {adatok[0]}, első : {adatok[1]}, második : {adatok[2]}, harmadik : {adatok[3]}'}
        szoveg.append(szo)

#print(szoveg)
print(f"Ez egy jó megoldás{szoveg}")
#for sor in forrasfajl:
#    print(sor)
