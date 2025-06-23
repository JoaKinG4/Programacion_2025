#BUCLE WHILE
contador = 3
while contador != 0:
    contador = contador - 1
    print("El contenido de contador es", contador)

#BUCLE WHILE 2
x = 1
while(x <= 1000):
    print(x)
    x = x + 1
    

#BUCLE FOR
lista = list((2, 1, 0))
tupla = tuple((2, 1, 0))
conjunto= set((2, 1, 0))
diccionario = dict(((2, "Dos"),(1, "Uno"), (0, "Cero")))

for iterador in diccionario.items():
    print(iterador)

#FUNCION RANGE LEN
lista2 = ["Vamos", "a", "acceder", "a", "esta", "lista", "por", "indices"]

for indice in range(len(lista)):
    print("Indice:", indice, "Elemento", lista[indice])

#BREAK (DETIENE)
for numero in range(5):
    if numero == 3:
        break
    print(numero)

#CONTINUE (SALTA 1)
for numero2 in range(5):
    if numero2 == 3:
        continue
    print(numero2)



intentos = 3
while intentos > 0:
    if input(">>> Escriba la contraseña:") == "Joaquin":
        print("Correcta")
        break
    intentos = intentos - 1
    print("Contraseña Incorrecta")
else:
    print("Se te acabaron los intentos")


