

#CREANDO DICCIONARIO
paciente = {
    'nombre': 'Carlos',
    'apellido': 'Santana',
    'edad': 50,
    'ciudad': 'Quellón',
    'consultas': [14, 20, 40],
    'diagnostico': ('resfrio')
}

print(paciente)

#OTRA FORMA DE DICCIONARIO
medico = dict(
    nombre = 'Joaquin',
    apellido = 'Mansilla',
    edad = 21,
    Especialidad = 'Neurologo',
)

#IMPRESION DE DICCIONARIOS
print(paciente)
print(medico)

#CONSULTANDO UN ELEMENTO A TRAVES DE LA CLAVE DEL DICCIONARIO
print(medico['nombre'])

#ELIMINANDO UNA CLAVE DEL DICCIONARIO (METODO DEL)
del(paciente['nombre'])
print(paciente)