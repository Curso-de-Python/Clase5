'''
-----------------------------
 EJERCICIO N°1
 Listas
-----------------------------
'''

numeros = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numeros)

numeros[0] = 111  # asignando un nuevo valor
print("\nPrevio contenido de la lista:", numeros)

numeros[1] = numeros[4]  # copiando el valor del quinto elemento al segundo
print("Nuevo contenido de la lista:", numeros) 

print("\nLongitud de la lista:", len(numeros)) # longitud de la lista

# ---------------------------

del numeros[1] # eliminando el 2do elemento de la lista

print("Longitud de la nueva lista:", len(numeros)) 
print("\nNuevo contenido de la lista:", numeros) 
