
## DEZVOLARE
x0 = 4
y0 = 5
width = 2 
height = 3

user_x = input("Introdu valoarea lui x a punctului ")
user_y = input("Introdu valoarea lui y a punctului ")

user_x = int(user_x)
user_y = int(user_y)

## Varianta 1 - preferata
if (x0 <= user_x <= x0 + width) and (y0 <= user_y <= y0 + height):
    print("Se afla in cadran")
else:
    print("Nu se afla in cadran")


## Varianta 2 - cu if-uri
if (x0 <= user_x <= x0 + width): 
    if (y0 <= user_y <= y0 + height):
        print("Se afla in cadran")
    else:
        print("Nu se afla in cadran")
else:
    print("Nu se afla in cadran")

## Varianta 3 - cu multe if-uri
if (x0 <= user_x ):
    if user_x <= x0 + width: 
        if (y0 <= user_y <= y0 + height):
            print("Se afla in cadran")
        else:
            print("Nu se afla in cadran")
    else:
        print("Nu se afla in cadran")
else:
    print("Nu se afla in cadran")