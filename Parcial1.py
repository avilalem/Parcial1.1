def pedir_puntaje(mensaje):
    while True:
        try:
            nota = float(input(mensaje))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Ingrese un número entre 0 y 10.")
        except ValueError:
            print("Ingrese un número válido.")

def registrar_empleados(empleados):
    try:
        cantidad = int(input("¿Cuántos empleados desea registrar?: "))
    except ValueError:
        print("Ingrese un número válido.")
        return

    for _ in range(cantidad):
        codigo_empleado = input("\nIngrese el código del empleado: ")
        if codigo_empleado in empleados:
            print("El código de empleado ya existe.")
            continue

        nombre = input("Nombre del empleado: ")
        departamento = input("Departamento del empleado: ")

        try:
            antiguedad = int(input("Antigüedad: "))
        except ValueError:
            print("Ingrese un número válido para la antigüedad.")
            continue

        print("\n--- Evaluación del empleado ---")
        puntualidad = pedir_puntaje("Puntualidad (0-10): ")
        equipo = pedir_puntaje("Trabajo en equipo (0-10): ")
        productividad = pedir_puntaje("Productividad (0-10): ")
        observaciones = input("Observaciones: ")
        promedio = (puntualidad + equipo + productividad) / 3
        estado = "Satisfactorio" if promedio >= 7 else "Mejorar"

        evaluacion = {
            "puntualidad": puntualidad,
            "equipo": equipo,
            "productividad": productividad,
            "observaciones": observaciones,
            "promedio": promedio,
            "estado": estado
        }

        print("\n--- Información de contacto ---")
        while True:
            try:
                telefono = input("Ingrese el número de teléfono (8 dígitos): ")
                if len(telefono)==8:
                    return telefono
                else:
                    print("Ingrese un número válido de 8 dígitos.")
            except ValueError:
                print("Ingrese un numero de telefono valido")
                continue

        correo = input("Ingrese correo electrónico: ")
        contacto = {
            "telefono": telefono,
            "correo": correo
        }

        empleados[codigo_empleado] = {
            "nombre": nombre,
            "departamento": departamento,
            "antiguedad": antiguedad,
            "evaluacion": evaluacion,
            "contacto": contacto
        }

def mostrar_empleados(empleados):
    if not empleados:
        print("No hay empleados registrados.")
        return

    print("\n--- Lista de Empleados ---")
    for codigo, datos in empleados.items():
        print(f"\nCódigo: {codigo}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Departamento: {datos['departamento']}")
        print(f"Antigüedad: {datos['antiguedad']} años")
        print("Evaluación:")
        for clave, valor in datos["evaluacion"].items():
            print(f"  {clave.capitalize()}: {valor}")
        print("Contacto:")
        print(f"  Teléfono: {datos['contacto']['telefono']}")
        print(f"  Correo: {datos['contacto']['correo']}")

def menu():
    empleados = {}
    while True:
        print("\n--- Control de Empleados ---")
        print("1. Agregar Empleado")
        print("2. Mostrar Empleados")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_empleados(empleados)
        elif opcion == "2":
            mostrar_empleados(empleados)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()


















































def registrar_estudiantes(estudiantes):
    try:
        cantida=int(input("Cuantos estudiantes desea registrar?:"))
    except ValueError:
        print("Ingrese un numero valido")
        return

    for _ in range(cantida):
        print("Registrando estudiante...")
        carnet=input("Carnet: ")
        if carnet in estudiantes:
            print("El carnet ingresado ya existe. Intente nuevamente")
            continue
        nombre=input("Nombre Completo: ")
        try:
            edad=int(input("Edad: "))
        except ValueError:
            print("Ingrese un numero valido")
            return
        carrera=input("Carrera: ")
        try:
            num_cursos=int(input("Cuantos cursos desea registrar?: "))
        except ValueError:
            print("Ingrese un numero valido")
            return

        cursos={}
        for i in range (num_cursos):
            print(f"Curso {i+1}:")
            nombre_curso=input("Nombre Curso: ").strip()
            def pedir_nota(titulo):
                while True:
                    nota=float(input("Nota: "))
                    if 0<=nota<=100:
                        return nota
                    else:
                        print("Ingrese un numero valido")
            tarea=pedir_nota("Nota de tarea: ")
            parcial=pedir_nota("Nota de parcial: ")
            proyecto=pedir_nota("Nota de proyecto: ")

            cursos[nombre_curso]={
                "tarea":tarea,
                "parcial":parcial,
                "proyecto":proyecto
            }
        estudiantes[carnet]={
            "nombre":nombre,
            "edad":edad,
            "carrera":carrera,
            "cursos":cursos
        }
def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados")
        return
    print("Lista de estudiantes:")
    for carnet, datos in estudiantes.items():
        print(f"Carnet: {carnet} - Nombre: {datos['nombre']} - Edad: {datos['edad']} - Carrera: {datos['carrera']}")
        cursos=datos.get["cursos",{}]
        if cursos:
            for curso, notas in cursos.items():
                print(f"Curso: {curso}")
                print(f"Notas de tarea: {notas['tarea']}")
                print(f"Notas de parcial: {notas['parcial']}")
                print(f"Notas de proyecto: {notas['proyecto']}")
        else:
            print("No tiene cursos registrados ")

def buscar_carnet (estudiantes):
    carnet=input("Ingrese el numero de carnet que desea buscar: ").strip()
    estudiante=estudiantes[carnet]
    if estudiante:
        print(f"Nombre: {estudiante['nombre']} - Edad: {estudiante['edad']} - Carrera: {estudiante['carrera']}")
        cursos=estudiante.get("cursos",{})
        if cursos:
            for curso, notas in cursos.items():
                promedio=(notas['tarea']+notas['parcial']+notas['proyecto'])/3
                print(f"Curso: {cursos}")
                print(f"Notas de tarea: {notas['tarea']}")
                print(f"Notas de parcial: {notas['parcial']}")
                print(f"Notas de proyecto: {notas['proyecto']}")
                print(f"Promedio: {promedio}")
        else:
            print("No tiene cursos registrados ")
    else:
        print("No hay estudiantes registrados ")






def menu():
    estudiantes={}
    while True:
        print("\n ___ Menu ___")
        print("1. Registrar Estudiantes")
        print("2. Mostrar Estuiantes y cursos")
        print("3. Buscar estuiante por carnet")
        print("4. Salir")
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            registrar_estudiantes(estudiantes)
        if opcion=="2":
            mostrar_estudiantes(estudiantes)
        if opcion=="3":
            buscar_carnet(estudiantes)
        if opcion=="4":
            print("Gracias por usar el programa!")
        else:
            print("Opcion invalida")

menu()