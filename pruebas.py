# Supongamos que tienes una función para insertar datos en una base de datos
def insertar_datos(nombre, edad):
    # Verifica si tanto el nombre como la edad no están en blanco
    if nombre.strip() != '' and edad.strip() != '':
        # Aquí realizarías la inserción en la base de datos
        print("Insertando datos:", nombre, edad)
    else:
        print("Por favor, ingrese valores válidos para nombre y edad.")

# Ejemplo de uso
nombre = input("Ingrese el nombre: ")
edad = input("Ingrese la edad: ")

# Llama a la función para insertar datos
insertar_datos(nombre, edad)
