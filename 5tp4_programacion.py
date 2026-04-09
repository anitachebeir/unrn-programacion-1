def obtener_estado(nota):
    if nota >= 8:
        return "Promociona"
    elif nota >= 6:
        return "Aprueba"
    else:
        return "Desaprueba"
nota = float(input("Ingrese su nota: "))
print(obtener_estado(nota))
