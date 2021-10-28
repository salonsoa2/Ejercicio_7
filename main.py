nombretelefono = list()
while True:
    Nombre = input("nombre:")
    if Nombre == "fin":
        break
    telefono = input("numero de telefono:")
    cell_1 = {}
    cell_1["nombre:"] = Nombre
    cell_1["numero de telefono:"] = telefono
    nombretelefono.append(cell_1)
for cell_1 in nombretelefono:
    print("numero y telefono", cell_1)