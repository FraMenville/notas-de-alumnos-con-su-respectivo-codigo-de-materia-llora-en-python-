import json
#esta funcion es para que pueda abrir el archivo json y leerlo
def cargar_datos():
    try:
        with open("notas2.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"alumnos": []}
    
    return data
#esta funcion es para poder modificar el archivo json por medio de la consola de python
def guardar_datos(data):
    with open("notas2.json", "w") as file:
        json.dump(data, file, indent=2)
#en esta funcion por medio del dni del alumno, en este caso la cedula y ademas el codigo de la materia, me da la nota del alumno
def mostrar_notas(data):
    dni = input("Ingrese la Cedula del alumno: ")
    materia = input("Ingrese el codigo de la materia: ")
    for alumno in data["alumnos"]:
        if alumno["DNI"] == dni:
            if materia in alumno["notas"]:
                print(f"La nota del alumno con la Cedula {dni} en la materia {materia} es: {alumno['notas'][materia]}")
                return
            else:
                print(f"No se encontró la materia {materia} para el alumno con la Cedula {dni}")
                return
    print("No se encontró un alumno con esa Cedula")
#esta funcion es para agregar un nuevo alumno en el archivo json
def agregar_alumno(data):
    dni = input("Ingrese la Cedula del nuevo alumno: ")
    nombre = input("Ingrese el nombre del nuevo alumno: ")
    apellido = input("Ingrese el apellido del nuevo alumno: ")
    notas = {}
    nueva_materia = input("Ingrese el codigo de la materia: ")
    nueva_nota = int(input(f"Ingrese la nota de {nueva_materia}: "))
    notas[nueva_materia] = nueva_nota
    nuevo_alumno = {"DNI": dni, "nombre": nombre, "apellido": apellido, "notas": notas}#esta parte del codigo me crea una seccion nueva en el diccionario creado anteriormente en el archivo json
    data["alumnos"].append(nuevo_alumno)
    guardar_datos(data)
    print("Nuevo alumno agregado con éxito")
#esta funcion elimina la nota del alumno
def eliminar_nota(data):
    dni = input("Ingrese la Cedula del alumno: ")
    materia = input("Ingrese el codigo de la materia para eliminar la nota: ")
    for alumno in data["alumnos"]:
        if alumno["DNI"] == dni:
            if materia in alumno["notas"]:
                del alumno["notas"][materia]
                guardar_datos(data)
                print(f"Nota de la materia {materia} eliminada para el alumno con la Cedula {dni}")
                return
            else:
                print(f"No se encontró la materia {materia} para el alumno con la Cedula {dni}")
                return
    print("No se encontró un alumno con esa Cedula")
#esta funcion es para reemplazar la nota del alumno ingresando el codigo de la materia a reemplazar
def reemplazar_nota(data):
    dni = input("Ingrese la Cedula del alumno: ")
    materia = input("Ingrese el codigo de la materia que desea reemplazar: ")
    nueva_nota = int(input(f"Ingrese la nueva nota de {materia}: "))
    for alumno in data["alumnos"]:
        if alumno["DNI"] == dni:
            if materia in alumno["notas"]:
                alumno["notas"][materia] = nueva_nota
                guardar_datos(data)
                print(f"Nota de la materia {materia} reemplazada para el alumno con la Cedula {dni}")
                return
            else:
                print(f"No se encontró la materia {materia} para el alumno con la Cedula {dni}")
                return
    print("No se encontró un alumno con ese DNI")
#a continuacion, se define el menu que se mostrara en la terminal de python
def menu():
    print("\n.............",
          "Seleccione una opción: ",
          "1 - Mostrar Notas",
          "2 - Agregar Alumno",
          "3 - Eliminar Nota",
          "4 - Reemplazar Nota",
          "0 - Salir",
          sep="\n")

data = cargar_datos()
#esto a continuacion es para que el menu funcione correctamente conectando los numeros a las funciones ya descritas anteriormente
while True:
    menu()
    option = input("Ingrese el número de la opción seleccionada: ")
    
    functionlist = {
        "1": lambda: mostrar_notas(data),
        "2": lambda: agregar_alumno(data),
        "3": lambda: eliminar_nota(data),
        "4": lambda: reemplazar_nota(data),
        "0": exit
    }
    
    if option in functionlist.keys():
        functionlist[option]()
        
    else:
        print("La opción seleccionada no es correcta")