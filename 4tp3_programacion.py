lista = []
contador = 0
print("Bienvenido a tu lista! Escribi tus productos. Para finalizar tu lista, escribi -fin-")
while contador < 5:
    pedido = input("Que producto agregamos?: ").lower()
    contador += 1
    if pedido == "fin":
        break
    lista.append(pedido)
    
print("Lista completada, estos son tus productos: ") 
print(lista)
print(f"Cantidad de productos: {len(lista)}")
