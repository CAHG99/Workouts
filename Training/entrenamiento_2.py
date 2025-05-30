import os
os.system("clear")

# Variables de control
quialificationList = []
qualification = 0
approved = 60
addition = 0
index = 0
count1 = 0
count2 = 0


# Función de validación
def validation(menssage, type=float, condition=lambda x: x > 0, bug="El valor no es válido"):
    while True:
        try:
            value = type(input(menssage))
            if condition(value):
                return value
            else:
                print(bug)
        except ValueError:
            print("Ingresa un número válido.")


# Función para ingresar y validar calificaciones
def pqualification(amount, list):
    for i in range(1, amount + 1):
        note = validation(f"  Ingrese la calificación #{i}: ", float, lambda x: 0 <= x <=
                          100, "\n⚠️ La calificación debe estar entre 0 y 100. Intenta nuevamente.")
        list.append(note)


specificRating = validation(
    "Por favor, ingresa una nota específica para comparar : ",
    float,
    lambda x: x > 0,
    "\n📚 Por favor, ingresa un número válido.")

amount = validation(
    "Por favor, ingresa la cantidad de notas que deseas registrar : ",
    int,
    lambda x: x > 0,
    "\n⚠️ La cantidad debe ser un número mayor que 0. Intenta nuevamente.")

pqualification(amount, quialificationList)


# Calcular el promedio de las calificaciones # Contar cuántas veces aparece la calificación específica
for i in quialificationList:
    addition += i
    if specificRating == i:
        count2 += 1
        continue


# Calcular el promedio
average = addition / len(quialificationList)
print(f"\n📊 Tu promedio es: {average:.2f}")


# Evaluar si aprobaste o reprobaste
if average >= approved:
    print(
        f"\n🎉 ¡Felicitaciones! Has aprovado con un promedio de {average:.2f}.")
else:
    print(f"\n😔 Lo sentimos, has reprobado con un promedio de {average:.2f}.")


# Contar las calificaciones mayores a la calificación específica
while index < len(quialificationList):
    if quialificationList[index] > specificRating:
        count1 += 1
    index += 1

print(
    f"\n📈 La cantidad de calificaciones mayores a {specificRating} es: {count1}.")
print(
    f"\n🔍 La calificación {specificRating} aparece {count2} {'veces' if count2 > 1 else 'vez'}.")
