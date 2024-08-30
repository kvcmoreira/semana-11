import pickle

class Libro:
    def __init__(self, id_libro, titulo, autor, disponible=True):
        self.id_libro = id_libro
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"ID: {self.id_libro}, Título: {self.titulo}, Autor: {self.autor}, Estado: {estado}"

class Biblioteca:
    def __init__(self):
        self.libros = {}

    def añadir_libro(self, libro):
        if libro.id_libro in self.libros:
            print("El libro ya existe en la biblioteca.")
        else:
            self.libros[libro.id_libro] = libro

    def eliminar_libro(self, id_libro):
        if id_libro in self.libros:
            del self.libros[id_libro]
        else:
            print("Libro no encontrado.")

    def actualizar_disponibilidad(self, id_libro, disponible):
        if id_libro in self.libros:
            self.libros[id_libro].disponible = disponible
        else:
            print("Libro no encontrado.")

    def buscar_libro(self, titulo):
        for libro in self.libros.values():
            if libro.titulo == titulo:
                print(libro)
                return libro
        print("Libro no encontrado.")
        return None

    def mostrar_todos_los_libros(self):
        for libro in self.libros.values():
            print(libro)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'wb') as archivo:
            pickle.dump(self.libros, archivo)

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'rb') as archivo:
                self.libros = pickle.load(archivo)
        except FileNotFoundError:
            print("Archivo no encontrado. Comenzando con una biblioteca vacía.")

def menu():
    biblioteca = Biblioteca()
    biblioteca.cargar_desde_archivo('biblioteca.dat')

    while True:
        print("\nMenú de Biblioteca:")
        print("1. Añadir libro")
        print("2. Eliminar libro")
        print("3. Actualizar disponibilidad")
        print("4. Buscar libro")
        print("5. Mostrar todos los libros")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_libro = input("ID del libro: ")
            titulo = input("Título del libro: ")
            autor = input("Autor: ")
            libro = Libro(id_libro, titulo, autor)
            biblioteca.añadir_libro(libro)
        elif opcion == "2":
            id_libro = input("ID del libro a eliminar: ")
            biblioteca.eliminar_libro(id_libro)
        elif opcion == "3":
            id_libro = input("ID del libro a actualizar disponibilidad: ")
            disponible = input("¿Está disponible? (s/n): ").lower() == 's'
            biblioteca.actualizar_disponibilidad(id_libro, disponible)
        elif opcion == "4":
            titulo = input("Título del libro a buscar: ")
            biblioteca.buscar_libro(titulo)
        elif opcion == "5":
            biblioteca.mostrar_todos_los_libros()
        elif opcion == "6":
            biblioteca.guardar_en_archivo('biblioteca.dat')
            print("Biblioteca guardada. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

menu()
