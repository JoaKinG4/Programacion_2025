#HACER QUE PASE
def nombre_funcion():
    pass
#LLAMAR A LA FUNCION
nombre_funcion()
#DEFINIR
def saludar(nombre):
    print("Hola", nombre)
#LLAMAR A LA FUNCION
saludar("Joaquin")

#CON VARIABLES
def media(num_1, num_2, num_3):
    resultado = num_1 + num_2 + num_3
    resultado = resultado/3
    return resultado    

llamada = media(2, 2, 5)
print(llamada)

#HACERLO CON UNA SOLA LINEA
def media(num_1, num_2, num_3):
    return(num_1 + num_2 + num_3)/3

llamada = media(2, 2, 5)
print(llamada)

#SCOPE
