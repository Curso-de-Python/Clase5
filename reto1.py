'''
-----------------------------
 RETO N°1
 Lo básico de listas
-----------------------------
Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4 y 5.

Tu tarea es escribir un programa que:
 1. Solicite al usuario que reemplace el número central en la lista con un número entero de su elección.
 2. Elimine el último elemento.
 3. Imprima la longitud de la lista final.
-----------------------------
'''

listaSombrero = [1, 2, 3, 4, 5] 

# Reemplazo del número central
reemplazo = int(input("Nuevo número central: "))
listaSombrero[2] = reemplazo

# Eliminar el último elemento
del listaSombrero[4]

# Imprimir longitud
print("La longitud final es de ", len(listaSombrero))

print(listaSombrero)
