#IF
edad = 19

if edad >= 18 and edad < 65:
    print('Es mayor de edad')
elif edad >= 65:
    print('Eres un adulto mayor')    
else:
    print('Eres menor de edad')       

#OPERADORES TERNARIOS
edad = 19
print("Usted puede votar" if edad >= 18 else "Usted no puede votar")

#GUIA RAPIDA CONDICIONALES PYTHON

from colorama import init, Fore
init()

#CONDICIONAL IF
print(Fore.GREEN + '############### 01 - UTILIZANDO IF Y ELSE ################')

licencia = False
edad = 19 
automovil = False

#¿Estara correcto este codigo?
#Incorrecto
print(Fore.YELLOW +'/n>>> Testeando los comparadores y el IF')
if licencia:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia')
else:
    print(Fore.WHITE + 'No tengo licencia para conducir')

#Sucede que la variable licencia se esta comparando con True,
#y se debe asignar directamente, es decir no se ocupa el ==, sino solamente el igual (=)

print(Fore.YELLOW + '/n>>> Utilizando el primer condicional IF')
if licencia:
    print(Fore.WHITE + 'Puedo conducir porque tengo licencia/n')



print(Fore.YELLOW + '>>> Utilizando el tercer condicional IF')




print(Fore.GREEN + '############## 02- UTILIZANDO IF, ELIF Y ELSE #############')
if licencia and edad >= 18:
    print(Fore.WHITE + 'Puedo conducir porque soy mayor de edad y tengo licencia')
elif automovil:
    print(Fore.WHITE + 'Tengo automovil, pero no tengo licencia ni la edad necesaria')
else:
    print(Fore.WHITE + 'No puedo conducir no tengo ni la edad, ni licencia de conducir')