import json      #manipulacion de archivos json
import os        #metodos para trabajar con el SO

ruta = os.path.join("Jupyter", "datos.json")

#Leer el archivo json
#uft-8 es el encoding para trabajar idioma español
#la letra "r" es de read = lectura
with open(ruta, "r", encoding='utf-8') as archivo:
    datos = json.load(archivo) #Conversion de JSON a estructura python

# Mostrar los usuarios del archivo JSON
for usuarios in datos:
    print(f"ID: {usuarios['id']}, Nombre: {usuarios['nombre']}, Edad: {usuarios['edad']}")