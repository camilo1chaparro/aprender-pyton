#Enunciado: 

"""
Escribe un programa que ayude a calcular la cuenta de un restaurante. El programa debe:

1. Pedir al usuario el nombre del cliente.
2. Pedir el valor total de la cuenta (número, puede tener decimales).
3. Pedir el porcentaje de propina que desea dejar (por ejemplo, 10).
4. Calcular el valor de la propina y el total a pagar.

"""

print("*** Bienvenido al calculador de cuentas del restaurante ***")

name = input("Ingrese el nombre del cliente: ")
valor_cuenta = float(input("Ingrese el valor total de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina que desea dejar: "))

propina =  valor_cuenta * (porcentaje_propina / 100)
total_a_pagar = valor_cuenta + propina

print(f"\nCliente: {name}")
print(f"Valor de la cuenta: ${valor_cuenta}")
print(f"Propina ({porcentaje_propina}%): ${propina}")
print(f"Total a pagar: ${total_a_pagar}")