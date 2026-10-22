#Tuples en Python

"""
Maneras de declarar tuplas en python. 
Estructura de datos que almacena una colección ordenada e inmutable de elementos.
"""
my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 1.70, "Juan", "Camilo")
my_other_tuple = (24, 33, 25, 40)
print (my_tuple)
print (type(my_tuple))


print (my_tuple[0]) 
print (my_tuple[-1])

print (my_tuple.count("Juan"))
print (my_tuple.index("Camilo"))

#Concatenando tuplas
my_suma_tuple = my_tuple + my_other_tuple
print (my_tuple + my_other_tuple) 
print (my_suma_tuple)

print(my_suma_tuple[3:6])

my_tupla_lista = list(my_tuple) #Convertimos una tupla en lista 
print (type(my_tupla_lista))

my_tupla_lista[3] = "Camilo"
my_tupla_lista.insert(4, "Chaparro")
my_tupla_lista.insert(1, "Rojo")
print (my_tupla_lista)

my_tupla_lista = tuple(my_tupla_lista) #Convertimos una lista en tupla 
print (my_tupla_lista)
print (type(my_tupla_lista))

del my_tupla_lista #Elimina la tupla 