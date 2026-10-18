#En este archivo vamos a ver como declarar variables en python

my_string_variable = "Hola, soy juan"
print (my_string_variable)

my_int_variable = 10
print (my_int_variable) 

my_bool_variable = True
print (my_bool_variable) 

#Concanetación de variables 
print (my_string_variable, my_int_variable, my_bool_variable) 

#Variables en una sola linea
name, surname, age = "Juan", "Camilo", 24
print ("Mi nombre es:", name, surname, "y tengo", age, "años.")

#Inputs para capturar datos del usuario

name = input("Ingrese su nombre: ")
surname = input("Ingrese su apellido: ")

print ("Mi nombre es:", name)
print ("Mi apelldio es:", surname)
