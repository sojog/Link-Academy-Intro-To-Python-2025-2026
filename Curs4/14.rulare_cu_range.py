# curs real
usd = 4.37
eur = 5.09

## for este o bucla finita care se executa de un numar de ori
for i in range(2):
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
