clave_ingresada = input("Ingrese su clave: ")
clave_almacenada = "heladoconcrema3"
respuesta = input("¿Usa token? (si/no): ")
if respuesta == "si":
    usa_token = True
else:
    usa_token = False
if usa_token == True or clave_ingresada == clave_almacenada:
    print("Acceso permitido")
else:
    print("Acceso denegado")
