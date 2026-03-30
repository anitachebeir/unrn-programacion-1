opcion = ""
total = 0
cantidad = 0
menu = {"pizza": 20,
        "hamburguesa": 15,
        "empanadas": 25,
        "sushi": 30,
        "carne": 40}
print("Bienvenido a Rotiseria Anita! Nuestro menu es:")
for comida in menu:
    print(f"{comida}: ${menu[comida]}")
while opcion != "terminar pedido":
    opcion = input("Que desea ordenar?: ").lower()

    if opcion in menu:
        precio = menu[opcion]
        total += precio
        cantidad += 1
        print(f"Perfecto! se añadio {opcion} al pedido")
    elif opcion == "terminar pedido":
       print("Terminando pedido... ")
       print(f"El total de su pedido es: ${total}")
       print(f"Total de items: {cantidad}")
    else:
        print(f"Lo sentimos, no tenemos {opcion}, proba con otra cosa ")
print("Gracias por comprar en Rotiseria Anita, Que lo disfrutes!")