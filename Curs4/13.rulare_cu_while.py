# curs real
usd = 4.37
eur = 5.09

## while -> este o bucla (infinita)
i = 0
while  i < 3:
    lei = int(input("Introduceti valoare in lei\n"))
   
    moneda = input("Introduceti moneda in care vreti sa convertiti\n")

    while moneda != "eur" and moneda != "usd":
        print("Nu avem aceasta valuta")
        moneda = input("Introduceti moneda in care vreti sa convertiti\n")

    if moneda == "eur":
        valoare_convertita = lei / eur
    elif moneda == "usd":
        valoare_convertita = lei / usd

    print("Valoare convertita este: ", round(valoare_convertita, 2))
    i += 1