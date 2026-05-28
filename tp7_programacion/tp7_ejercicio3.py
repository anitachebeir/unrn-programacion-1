nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []
for nombre in nombres:
    normal = nombre.strip().capitalize()
    nombres_normalizados.append(normal)
print(nombres_normalizados)
