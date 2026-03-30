colores = ["rojo", "rosa", "celeste", "violeta"]
c = 0
consulta = input("Ingrese un color: ")
encontrado = False
while c < len(colores):
    if colores [c] == consulta:
        print("El color esta en la lista")
        print(f"Su posicion es: {c}")
        encontrado = True
        break
    c += 1
if encontrado == False:
    print("El color no esta en la lista")   