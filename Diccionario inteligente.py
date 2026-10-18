class Palabra:
    def __init__(self, texto, definicion):
        self.texto = texto
        self.definicion = definicion

    def __lt__(self, other):
        return self.texto < other.texto

    def __gt__(self, other):
        return self.texto > other.texto

    def __eq__(self, other):
        return self.texto == other.texto


class DiccionarioBST(ArbolBinarioBusqueda):
    def insertar_palabra(self, texto, definicion):
        palabra = Palabra(texto, definicion)
        self.insertar(palabra)

    def buscar_palabra(self, texto):
        return self._buscar_palabra_rec(self.raiz, texto)

    def _buscar_palabra_rec(self, nodo, texto):
        if nodo is None:
            return None
        if nodo.valor.texto == texto:
            return nodo.valor.definicion
        elif texto < nodo.valor.texto:
            return self._buscar_palabra_rec(nodo.izquierdo, texto)
        else:
            return self._buscar_palabra_rec(nodo.derecho, texto)

    def buscar_por_prefijo(self, prefijo):
        resultado = []
        self._buscar_prefijo_rec(self.raiz, prefijo, resultado)
        return resultado

    def _buscar_prefijo_rec(self, nodo, prefijo, resultado):
        if nodo is not None:
            if nodo.valor.texto.startswith(prefijo):
                resultado.append(nodo.valor.texto)
            self._buscar_prefijo_rec(nodo.izquierdo, prefijo, resultado)
            self._buscar_prefijo_rec(nodo.derecho, prefijo, resultado)


# Interfaz de consola
def interfaz_diccionario():
    dicc = DiccionarioBST()
    # Cargar palabras iniciales
    palabras = [
        ("auto", "Vehículo de cuatro ruedas"),
        ("autonomía", "Capacidad de gobernarse por sí mismo"),
        ("aurora", "Fenómeno luminoso en el cielo"),
        ("barco", "Vehículo que navega en el agua"),
        ("casa", "Lugar donde habita una persona"),
        # Agregar más hasta llegar a 50...
    ]
    for texto, definicion in palabras:
        dicc.insertar_palabra(texto, definicion)

    while True:
        print("\n--- Diccionario Inteligente ---")
        print("1. Buscar palabra exacta")
        print("2. Buscar por prefijo")
        print("3. Ver diccionario completo (ordenado)")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            palabra = input("Ingresa la palabra: ")
            definicion = dicc.buscar_palabra(palabra)
            if definicion:
                print(f"Definición: {definicion}")
            else:
                print("Palabra no encontrada.")
        elif opcion == "2":
            prefijo = input("Ingresa el prefijo: ")
            resultados = dicc.buscar_por_prefijo(prefijo)
            print("Coincidencias:", resultados)
        elif opcion == "3":
            ordenadas = [p.texto for p in dicc.inorden()]
            print("Diccionario completo:", ordenadas)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")
