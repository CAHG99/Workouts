import os
os.system("clear")

# Muestra la bienvenida al sistema de compra
print("Hola Bienvenido al sistema de compra\n")

# Pide el nombre del producto
producto = input("Ingresa el nombre del producto: ")

# Validacion de datos
while True:  # se inicia un bucle que se repetira hasta que se ingrese un numero valido.
    try:
        cantidad = int(input("Ingresa la cantidad de productos adquiridos: "))
        if cantidad <= 0:
            print("la cantidad debe ser un numero mayor que 0. Intente nuevamente.")
        else:
            break

    except ValueError:  # si el valor ingresado no es valido, da error
        print("ingresa un numero valido.")
        
while True:
    try:
        precio = float(input("Ingresa el precio unitario: "))
        if precio <= 0:
            print("el precio debe ser un numero mayor que 0. Intente nuevamente.")
        else:
            break
    except ValueError:
        print("ingresa un numero valido.")
        
while True:
    try:
        descuento = float(
            input("Ingresa el porcentaje de descuento que se aplicará: "))
        if descuento < 0 or descuento > 100:
            print("El descuento debe estar entre 0 y 100.")
        else:
            break
    except ValueError:
        print("ingrese un número válido para el porcentaje.")


# Calcular costos
costo_sin_descuento = precio * cantidad
costo_con_descuento = costo_sin_descuento * (descuento/100)
costo_total = costo_sin_descuento - costo_con_descuento

print("\n\n")

# Muestra la informacion de la compra
print("Informacion de tu compra:")
print("\n")
print(
    f"Producto:-----------------------------------------------------------------------------{producto}")
print(
    f"Precio unitario:----------------------------------------------------------------------${precio:,.2f}")
print(
    f"Cantidad:-----------------------------------------------------------------------------{cantidad}")
print(
    f"costo sin descuento:------------------------------------------------------------------${costo_sin_descuento:,.2f}")
if descuento > 0:
    print(
        f"Descuento aplicado:-------------------------------------------------------------------{descuento}%")
    print(
        f"Costo total con descuento:------------------------------------------------------------${costo_total:,.2f}")
else:
    print("No se aplico descuento.")
    print(
        f"Costo total:--------------------------------------------------------------------------${costo_sin_descuento:,.2f}")
