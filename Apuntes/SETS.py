SETS

#CREANDO SETS
colores = {'Azul', 'Rojo', 'Azul', 'Verde'}
colorcitos = {'Azul', 'Naranjo'}

#IMPRIMIENDO EL SET COLORES
print(colores)

#AGREGANDO UN NUEVO ELEMENTO AL SET (METODO ADD)
colores.add('Blanco')
print(colores)

#ELIMINANDO UN ELEMENTO DEL SET
colores.discard('Blanco')
print(colores)

#APLICANDO EL METODO DIFFERENCE
diferencia = colores.difference(colorcitos)
print(diferencia)



