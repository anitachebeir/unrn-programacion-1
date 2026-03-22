
clave_almacenada = "heladoconcrema3"
respuesta = input("¿Usa token? (si/no): ")
if respuesta == "si":
    usa_token = True
    print("Acceso permitido")
else:
    usa_token = False
    clave_ingresada = input("Ingrese su clave: ")
    if clave_ingresada == clave_almacenada:
        print("Acceso permitido")
    else:
        print("Acceso denegado")