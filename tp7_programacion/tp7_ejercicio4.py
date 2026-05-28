edad = input("Ingrese una edad: ")
edad_limpia = edad.strip()
if edad_limpia.isnumeric():
    edad_limpia = int(edad_limpia)
    if edad_limpia > 120 or edad_limpia < 0:
        print("Edad no valida")
    else:
        print(f"Edad registrada: {edad_limpia}")
else:
    print("Por favor, ingrese un numero valido")