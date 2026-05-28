codigo = input("Ingrese el codigo de materia: ")
codigo_limpio = codigo.strip()
partes = codigo_limpio.split("-")
if len(partes) == 2:
    if partes[0].isalpha() and partes[1].isnumeric():
        print(f"Codigo valido: {codigo_limpio.upper()}")
    else:
        print("Codigo no valido")
else:
    print("Codigo no valido")