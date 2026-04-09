def calcular_descuento(precio):
    if precio > 10000:
        return precio * 0.9
    else:
        return precio
precio = int(input("Ingrese el precio del producto: "))
print((calcular_descuento(precio)))
while precio > 10000:
    print("Descuento aplicado")
    break
else:
    print("No se aplica descuento")