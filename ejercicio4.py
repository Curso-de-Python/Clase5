'''
-----------------------------
 EJERCICIO N°4
 Más sobre listas
-----------------------------
 Calcularemos la suma de todos los valores en la lista miLista
-----------------------------
'''
# MÉTODO 1
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in range(len(miLista)):
  suma += miLista[i]

print(suma)

'''
# MÉTODO 2
miLista = [10, 1, 8, 3, 5]
suma = 0

for i in miLista:
  suma += i

print(suma) 
'''
