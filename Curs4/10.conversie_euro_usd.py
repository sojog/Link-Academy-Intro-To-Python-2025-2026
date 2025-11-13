# curs real
usd = 4.37
eur = 5.09

## while -> este o bucla (infinita)
while True:
    lei = int(input("Introduceti valoare in lei\n"))
    moneda = input("Introduceti moneda in care vreti sa convertiti\n")

    if moneda == "eur":
        valoare_convertita = lei / eur
        print("Valoare convertita este: ", round(valoare_convertita, 2))
    elif moneda == "usd":
        valoare_convertita = lei / usd
        print("Valoare convertita este: ", round(valoare_convertita, 2))
    else:
        print("Nu avem aceasta valuta")

    