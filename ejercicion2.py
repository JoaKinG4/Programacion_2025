alumnos = input("Ingrese cantidad de alumnos de esta asignatura")
try:
    numero = int(alumnos)
    print(f"{numero} alumnos")
except ValueError:
    print("Error al ingresar el valor, recuerde ingresarlo como entero")
except Exception as i:
    print("Error inesperado")
else:
    print("Registro de alumnos exitoso")
finally:
    print("Fin del proceso")

leer_nota = while True:
        try:
            nota = float(input("Ingrese la nota (entre 0.0 y 7.0): "))
            if 0.0 <= nota <= 7.0:
                return nota
            else:
                print("La nota debe estar entre 0.0 y 7.0.")
        except ValueError:
            print("Formato inválido. Ingrese un número flotante.")

def registrar_estudiantes():
    asignatura = input("Ingrese el nombre de la asignatura: ")
    alumnos = []

    try:
        N = int(input("Ingrese la cantidad de estudiantes: "))
    except ValueError:
        print("Cantidad inválida. Debe ser un número entero.")
        return

    for i in range(N):
        print(f"\nEstudiante {i+1}:")
        nombre = input("Nombre del estudiante: ")
        notas = [leer_nota() for _ in range(3)]
        alumnos.append({
            "nombre": nombre,
            "notas": notas
        })

    print(f"\nRegistro completo de la asignatura: {asignatura}")
    for est in alumnos:
        print(f"{est['nombre']}: Notas = {est['notas']}")