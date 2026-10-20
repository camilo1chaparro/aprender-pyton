#Listas en python 

empy_list = list() #Esta es una lista vacía usando la función list()
print (len(empy_list)) 

empty_list1 = [] #Esta es una lista vacía usando corchetes
print (len(empty_list1)) 

my_int_list = [1, 2, 3] #Esta es una lista de enteros
my_string_list = ['a', 'b', 'c'] #Esta es una lista de cadenas de texto
fruits = ['banana', 'orange', 'mango', 'lemon']  #Esta es una lista de frutas
my_float_list = [1.5, 2.5, 3.5] #Esta es una lista de números flotantes 

number_of_lists = len(my_int_list) + len(my_string_list) + len(fruits) + len(my_float_list) #Esta es la suma de los tamaños de las listas

#Imprimir listas
print (my_int_list)
print (my_string_list)
print (fruits)
print (my_float_list)

print (number_of_lists)