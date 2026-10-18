### Operadores aritméticos en python 

#Operaciones con numeros enteero 

print ("Suma: ", 10 + 5) 
print ("Resta: ", 10 - 5)
print ("Multiplicación: ", 10 * 5)
print ("División: ", 10 / 5)
print ("División entera: ", 10 // 5)
print ("Módulo: ", 10 % 5)
print ("Exponente: ", 10 ** 5)

#Operacion de cadenas de texto
print ( "Hola" + "Mundo")
print ( " Hola " * 3) #Repetición de cadenas de texto


#Operadores de comparación

print ("4 es mayor que 5: ", 4 > 5)
print ("4 es menor que 5: ", 4 < 5)
print ("4 es mayor o igual que 5: ", 4 >= 5)
print ("4 es menor o igual que 5: ", 4 <= 5)
print ("4 es igual a 5: ", 4 == 5)
print ("4 es diferente de 5: ", 4 != 5) 


#Operadores lógicos
# and = y lógico
# or = o lógico
# not = no No lógico / Negación

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))