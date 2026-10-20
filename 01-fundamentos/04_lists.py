#Listas en python 

empy_list = list() #Esta es una lista vacía usando la función list()
print (len(empy_list)) 

empty_list1 = [] #Esta es una lista vacía usando corchetes
print (len(empty_list1)) 

my_int_list = [1, 2, 3] #Esta es una lista de enteros
my_string_list = ['a', 'b', 'c'] #Esta es una lista de cadenas de texto
fruits = ['banana', 'orange', 'mango', 'lemon']  #Esta es una lista de frutas
my_float_list = [1.5, 2.5, 3.5] #Esta es una lista de números flotantes 
my_other_list = [24, 1.70, "Juan", "Camilo"] #Esta es una lista de elementos mixtos

number_of_lists = len(my_int_list) + len(my_string_list) + len(fruits) + len(my_float_list) #Esta es la suma de los tamaños de las listas

#Imprimir listas
print (my_int_list)
print (my_string_list)
print (fruits)
print (my_float_list)

print (number_of_lists)

#Accediendo a elementos de la lista
print (fruits[0]) #Accediendo al primer elemento de la lista
print (my_string_list[1]) #Accediendo al segundo elemento de la lista
print (my_other_list[-2]) #Accediendo al penúltimo elemento de la lista
print (fruits[-1]) #Accediendo al último elemento de la lista
print (fruits.count('banana')) #Contando cuantas veces aparece el elemento en la lista

#desempaquetando listas
edad, estatura, nombre, segundo_nombre = my_other_list 
print (segundo_nombre) 

print (my_int_list + my_string_list) #Concatenando listas


#Creacion, insercion, actualizacion y eliminación de elementos en listas

my_other_list.append("Chaparro") #Agregando un elemento al final de la lista
print (my_other_list)

fruits.insert(1, "grape") #Insertando un elemento en la posición 1 de la lista
print (fruits)

fruits[0] = "strawberry" #Actualizando el primer elemento de la lista
print (fruits)

fruits.remove("strawberry") #Eliminando un elemento de la lista
print (fruits)

#Eliminando elementos de la lista usando pop() y del() y vaciar los elementos de la lista usando clear()
colors = ['red', 'green', 'blue', 'yellow', 'purple']
colors.pop() #Eliminando el último elemento de la lista
print (colors)

colors.pop(1) #Eliminando el segundo elemento de la lista
print (colors)

my_numero_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del my_numero_list[0] 
print (my_numero_list)

del my_numero_list[1:3] 
print (my_numero_list)

my_numero_list.clear() #Vacia todos los elementos de la lista
print (my_numero_list)


my_num_list_copy = my_int_list.copy() #Copia de una lista
print (my_num_list_copy)

#Encontrando elementos en una lista con index() que devuelve el índice de un elemento en la lista
my_nombre_list = ['Juan', 'Camilo', 'Chaparro']
print (my_nombre_list.index('Camilo')) #Encontrando el índice de un elemento en la lista

ages = [22, 25, 30, 35, 40]
print (ages.index(30)) #Encontrando el índice de un elemento en la lista

my_letras_list = ['A', 'B', 'C', 'D', 'E']
my_letras_list.reverse() #Invierte el orden de los elementos en la lista
print (my_letras_list)

my_letras_list.sort() #Ordena los elementos de la lista en orden ascendente
print (my_letras_list)
my_letras_list.sort(reverse=True) #Ordena los elementos de la lista en orden descendente
print (my_letras_list)