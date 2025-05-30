# # Lista de productos
# productos = [
#     {"nombre": "Producto1", "precio": 100, "cantidad": 50},
#     {"nombre": "Producto2", "precio": 200, "cantidad": 30},
#     {"nombre": "Producto3", "precio": 150, "cantidad": 70}
# ]

# # Función para buscar un producto por nombre
# def buscar_producto(nombre):
#     for producto in productos:
#         if producto['nombre'].lower() == nombre.lower():  # Comparación insensible a mayúsculas/minúsculas
#             return producto['precio'], producto['cantidad']
#     return None  # Si no se encuentra el producto

# # Solicitar al usuario que ingrese el nombre del producto
# nombre = input("Por favor, ingresa el nombre del producto: ")

# # Buscar el producto
# resultado = buscar_producto(nombre)

# if resultado:
#     precio, cantidad = resultado
#     print(f'Producto encontrado: {nombre}')
#     print(f'Precio: ${precio}')
#     print(f'Cantidad disponible: {cantidad}')
# else:
#     print(f'No se encontró el producto: {nombre}')

calificaciones = []
# Solicitar al usuario que ingrese calificaciones separadas por comas
entrada = input("Ingrese una lista de calificaciones separadas por comas: ")

# Dividir la entrada en una lista de cadenas
calificaciones_str = entrada.split(',')
calificaciones.append(calificaciones_str)

for calificacion in calificaciones:
    print(calificacion)
    
    # Solicitar al usuario que ingrese calificaciones separadas por comas
entrada = input("Ingrese una lista de calificaciones separadas por comas: ")

# Dividir la entrada en una lista de cadenas y convertir a números
calificaciones = [float(c.strip()) for c in entrada.split(',')]

# Imprimir cada calificación
for calificacion in calificaciones:
    print(calificacion)

# Sumar las calificaciones
suma = sum(calificaciones)
print("Suma total de calificaciones:", suma)

   
