#Enunciado: 

"""
1. Muestra el primer elemento y el último elemento de la lista.
2. Agrega "café" al final.
3. Inserta "queso" en la posición 1 (segundo lugar).
4. Cambia "pan" por "pan integral".
5. Elimina "arroz" de la lista.
6. Elimina el último elemento con .pop() y guarda en una variable el elemento que se eliminó.
7. Muestra los dos primeros elementos usando slicing.
8. Comprueba con in si "leche" está en la lista y muestra True o False.
9. Ordena la lista alfabéticamente.
10. Muestra cuántos elementos tiene la lista con len().
"""

compras = ["leche", "pan", "huevos", "arroz"]


print(compras[0])  # Muestra el primer elemento
print(compras[3])  # Muestra el último elemento

compras.append("café")  
print(compras)

compras.insert(1, "queso")
print(compras)

indice = compras.index("pan")
compras[indice] = "pan integral"
print(compras)

compras.remove("arroz")
print(compras)


eliminado = compras.pop()
print(eliminado)
print(compras)

compras = compras [0:2]
print(compras)

print("leche" in compras)

compras.sort()
print(compras)

print(len(compras))