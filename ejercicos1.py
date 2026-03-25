menu = ["pizza","hamburguesa","empanada","sushi"]
opcion = ""
print("Selecciona la comida para llevar")
while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: "). lower()
    if opcion == menu:
        print(f"Excelente! Agregamos {opcion} a tu pedido")
    elif opcion == "terminar pedido":
        print("Cerrando pedido...")
    else:
        print(f"Lo siento, no tenemos {opcion}, prueba con otra cosa")
print("Pedido finalizado, gracias por confiar en nosotros")       