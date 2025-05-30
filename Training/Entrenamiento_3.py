import os
os.system("clear")
# Anadir productos
# Consultar productos
# actualizar precios
# eliminar productos
# calcular el valor total del inventario


inventario = [
    {"nombre": "Detergente para lavar platos", "cantidad": 40, "precio": 10000},
    {"nombre": "Limpiador multiusos", "cantidad": 30, "precio": 12000},
    {"nombre": "Esponjas", "cantidad": 25, "precio": 5000},
    {"nombre": "Ollas y sartenes", "cantidad": 20, "precio": 80000},
    {"nombre": "Recipientes para almacenar alimentos",
        "cantidad": 8, "precio": 24000},
    {"nombre": "Papel higiénico", "cantidad": 22, "precio": 20000},
    {"nombre": "Shampoo", "cantidad": 12, "precio": 18000},
    {"nombre": "Camas y colchones", "cantidad": 4, "precio": 600000},
    {"nombre": "Aspiradora", "cantidad": 3, "precio": 350000},
    {"nombre": "Refrigerador", "cantidad": 2, "precio": 1200000},
    {"nombre": "Tabla de planchar", "cantidad": 8, "precio": 40000},
    {"nombre": "Botiquín de primeros auxilios", "cantidad": 5, "precio": 70000},
    {"nombre": "Tostadora", "cantidad": 4, "precio": 45000},
    {"nombre": "Microondas", "cantidad": 2, "precio": 250000},
    {"nombre": "Licuadora", "cantidad": 6, "precio": 80000},
    {"nombre": "Cortina de baño", "cantidad": 10, "precio": 25000},
    {"nombre": "Sofá", "cantidad": 3, "precio": 800000},
    {"nombre": "Mesa de comedor", "cantidad": 2, "precio": 400000},
    {"nombre": "Ventilador", "cantidad": 6, "precio": 120000},
    {"nombre": "Repuesto para aspiradora", "cantidad": 1, "precio": 30000}
]


def validacionn():
    nombre = input("Por favor, ingresa el nombre del producto: ")
    while nombre.strip() == "":
        print("⚠️ Por favor, ingresa un nombre de producto válido.")
        nombre = input("Por favor, ingresa el nombre del producto: ")

    while True:
        try:
            cantidad = int(
                input("Por favor, ingresa la cantidad del producto: "))
            if cantidad <= 0:
                print("⚠️ Por favor, ingresa una cantidad válida mayor a 0.")
            else:
                break
        except ValueError:
            print("⚠️ Por favor, ingresa un número válido para la cantidad.")
            continue

    while True:
        try:
            precio = float(
                input("Por favor, ingresa el precio del producto: "))
            if precio <= 0:
                print("⚠️ Por favor, ingresa un precio válido mayor a 0.")
            else:
                break
        except ValueError:
            print("⚠️ Por favor, ingresa un número válido para el precio.")

    # Si todos los datos son válidos, salimos del bucle
    return {"nombre": nombre, "cantidad": cantidad, "precio": precio}


def validacion(mensaje, tipo=float, condicion=lambda x: True, error="Ingresa un numero valido"):
    entrada = input(mensaje).strip()
    if not entrada:
        print("")


# Llamada a la función de validación
producto = validacion()
inventario.append(producto)
print("Inventario actual:", inventario)
