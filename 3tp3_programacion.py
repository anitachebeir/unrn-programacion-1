lista = []
print("Bienvenido a tu lista! Escribi tus productos. Para finalizar tu lista, escribi -fin-")
while True:
    pedido = input("Que producto agregamos?: ").lower()
    if pedido == "fin":
        break
    lista.append(pedido)
    
print("Lista completada, estos son tus productos: ") 
print(lista)
print(f"Cantidad de productos: {len(lista)}")
