import os
os.system("clear")

# Variables de control
lista_De_Calificacion = []
calificion = 0
aprobado = 60
suma = 0
indice = 0
count = 0
contador = 0

# Bucle para validar la calificación específica
while True:
    try:
        calificacion_Especifica = float(input("\n📚 Por favor, ingresa una nota específica para comparar: "))
        if calificacion_Especifica >= 0:
            print("\n✔️ ¡Nota válida ingresada!")
            break
        else:
            print("\n⚠️ Por favor, ingresa un número válido. Intenta nuevamente.")
    except ValueError:
        print("\n⚠️ Por favor, ingresa un dato válido.")

# Bucle para ingresar la cantidad de notas
while True:
    try:
        cantidad = int(input("\n🔢 Por favor, ingresa la cantidad de notas que deseas registrar: "))
        if cantidad > 0:
            print("\n✔️ ¡Cantidad de notas aceptada!")
            break
        else:
            print("\n⚠️ La cantidad debe ser un número mayor que 0. Intenta nuevamente.")
    except ValueError:
        print("\n⚠️ Por favor, ingresa un dato válido.")

# Ingreso de las calificaciones
print("\n📝 Ingreso de calificaciones entre 0 y 100 ")
for i in range(1, cantidad + 1):
    while True:
        try:
            calificion = float(input(f"  Ingrese tu calificación #{i}: "))
            if 0 <= calificion <= 100:
                lista_De_Calificacion.append(calificion)
                break
            else:
                print("\n⚠️ La calificación debe estar entre 0 y 100. Intenta nuevamente.")
        except ValueError:
            print("\n⚠️ Por favor, ingresa un dato válido.")

# Calcular el promedio de las calificaciones
for i in lista_De_Calificacion:
    suma += i

promedio = suma / len(lista_De_Calificacion)

# Presentación del promedio con un estilo más claro
print(f"\n📊 Tu promedio es: {promedio:.2f}")

# Evaluar si aprobaste o reprobaste
if promedio >= aprobado:
    print(f"\n🎉 ¡Felicitaciones! Has aprobado con un promedio de {promedio:.2f}.")
else:
    print(f"\n😔 Lo sentimos, has reprobado con un promedio de {promedio:.2f}.")

# Contar las calificaciones mayores a la calificación específica
while indice < len(lista_De_Calificacion):
    if lista_De_Calificacion[indice] > calificacion_Especifica:
        count += 1
    indice += 1

print(f"\n📈 La cantidad de calificaciones mayores a {calificacion_Especifica} es: {count}.")

# Contar cuántas veces aparece la calificación específica
for i in lista_De_Calificacion:
    if calificacion_Especifica == i:
        contador += 1
        continue

# Mostrar la cantidad de veces que aparece la calificación específica
print(f"\n🔍 La calificación {calificacion_Especifica} aparece {contador} {'veces' if contador > 1 else 'vez'}.")


            
