
menu = {"pizza", "hamburguesa", "empanadas", "sushi", "carne"}
print(f"Bienvenido a Rotiseria Anita! Nuestro menu es: {menu}")
while opcion != "terminar pedido":
    opcion = input("Que desea ordenar?: ")
    if opcion == menu:
        print(f"Perfecto! se añadio {opcion} al pedido")
    elif opcion != menu:
        print(f"Lo sentimos, no tenemos {opcion}, proba con otra cosa ")
    else:
        print("Terminando pedido... ")
        
    
