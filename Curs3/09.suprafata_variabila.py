## DEZVOLARE
x0 = 4
y0 = 5
width = 2 
height = 3

user_x = input("Introdu valoarea lui x a punctului ")
user_y = input("Introdu valoarea lui y a punctului ")

user_x = int(user_x)
user_y = int(user_y)

## Varianta 1 
if (x0 <= user_x <= x0 + width) and (y0 <= user_y <= y0 + height):
    is_in_zone = True
else:
    is_in_zone = False

print("Se afla in zona:", is_in_zone)

## Varianta 2
print("Se afla in zona:", (x0 <= user_x <= x0 + width) and (y0 <= user_y <= y0 + height))


## Varianta 3
print("Se afla in zona:", (x0 <= int(input("Introdu valoarea lui x a punctului ")) <= x0 + width) and (y0 <= int(input("Introdu valoarea lui y a punctului ")) <= y0 + height))