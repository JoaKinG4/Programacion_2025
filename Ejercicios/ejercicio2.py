#DEFINIR VARIABLES
entero = int(input("Ingrese un numero entero: "))
flotante = float(input("Ingrese un numero con decimales: "))
complejo = complex(input("Ingrese un numero complejo (ej: 2j): "))

#CALCULOS
#POTENCIA COMPLEJA
a = entero + complejo
potencia_comp = a ** 2
print("Potencia Compleja: ", potencia_comp)

#SUMA MIXTA
b = complejo + flotante
print("La suma mixta es: ", b)

#PRODUCTO MIXTO

