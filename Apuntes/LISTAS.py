LISTAS

#FUNCION APPEND (AGREGANDO UN ELEMENTO)
ramos,append('Introduccion a la Matematica')
print(ramos)

#MODIFICAR ELEMENTOS DE LA LISTA
ramos[0] = 'Comunicacion'
print(ramos)

# OTRA FORMA DE INSERTAR UN ELEMTNO A LA LISTA (INSERT)
ramos.insert(0,'Algebra')
print(ramos)

# ELIMINAR EL ULTIMO ELEMENTO DE LA LISTA
ramos.pop()
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA
ramos.sort()
print(ramos)

# ORDENANDO ELEMENTOS DE UNA LISTA SEGUN SU CANTIDAD DE CARACTERES
# key es una propiedad del metodo sort y se pasa un valor que es el metodo len
ramos.sort(key=len)
print(ramos)

# OCUPANDO EL METODO EXTEND(EXTIENDO UNA LISTA A PARTIR DE OTRA)
ramitos = ['Cálculo', 'Autómatas'] #nueva lista creada
ramos.extend(n)
print(ramos)

