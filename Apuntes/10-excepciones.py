
entrada = input("Ingrese un valor entero") ## valor ingresado es un str

try:
    numero = int(entrada)
    print(f"Numero ingresado: {numero}")
except ValueError: # error por tipo de dato
    print("Error de valor: el valor ingresado no es entero")
except Exception as e: #errores genericos e inesperados
    print("Error inesperado: {e}")
else:
    print("Conversion fue exitosa!")
finally: 
    print("Finalizacion del bloque")
