nombres = ['Jose',
           'Roberto',
           'Maria',
           'Gambino',
           'Gerardo',
           'Manolo',
           'Raul',
           'Cristina',
           'Jenifer',
           'Karina']  # Se agregaron mas nombres

edades = [17, 23, 25, 20, 29, 34, 36, 40, 43, 47] # Se agragron mas edades

nombres_dict = {nombre.lower(): edad for nombre, edad in zip(nombres, edades)}

user_nombre = input("Indique un nombre: ").lower()

if user_nombre in nombres_dict:
    print(f"{user_nombre.capitalize()} tiene {nombres_dict[user_nombre]} años")
else:
    print(f"{user_nombre} no se encuentra en el diccionario")
