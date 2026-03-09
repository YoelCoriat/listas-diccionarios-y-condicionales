nombres = ['Jose',
           'Roberto',
           'Maria',
           'Gambino',
           'Gerardo']

nombres_dict = dict(zip(nombres, [
    17,
    23,
    25,
    20,
    29]))

user_nombre = input("Indique un nombre: ")
for nombre, edad in nombres_dict.items():
    if user_nombre.lower() == nombre.lower():
        print(f"{nombre} tiene {edad} años")
        break
else:
    print(f"{user_nombre} no se encuentra en el diccionario")
