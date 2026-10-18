# 1. Método eliminar(valor)
def eliminar(self, valor):
    self.raiz = self._eliminar_rec(self.raiz, valor)

def _eliminar_rec(self, nodo, valor):
    if nodo is None:
        return nodo
    if valor < nodo.valor:
        nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, valor)
    elif valor > nodo.valor:
        nodo.derecho = self._eliminar_rec(nodo.derecho, valor)
    else:
        # Caso 1: sin hijos
        if nodo.izquierdo is None and nodo.derecho is None:
            return None
        # Caso 2: un hijo
        elif nodo.izquierdo is None:
            return nodo.derecho
        elif nodo.derecho is None:
            return nodo.izquierdo
        # Caso 3: dos hijos
        sucesor = self._min_nodo(nodo.derecho)
        nodo.valor = sucesor.valor
        nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.valor)
    return nodo

def _min_nodo(self, nodo):
    actual = nodo
    while actual.izquierdo is not None:
        actual = actual.izquierdo
    return actual


# 2. Recorrido por niveles (BFS)
from collections import deque

def recorrido_niveles(self):
    if self.raiz is None:
        return []
    resultado = []
    cola = deque([self.raiz])
    while cola:
        nodo = cola.popleft()
        resultado.append(nodo.valor)
        if nodo.izquierdo:
            cola.append(nodo.izquierdo)
        if nodo.derecho:
            cola.append(nodo.derecho)
    return resultado


# 3. Suma de todos los elementos
def suma_elementos(self):
    return self._suma_rec(self.raiz)

def _suma_rec(self, nodo):
    if nodo is None:
        return 0
    return nodo.valor + self._suma_rec(nodo.izquierdo) + self._suma_rec(nodo.derecho)


# 4. Validar si es completo
def es_completo(self):
    if self.raiz is None:
        return True
    cola = deque([self.raiz])
    encontrado_hueco = False
    while cola:
        nodo = cola.popleft()
        if nodo.izquierdo:
            if encontrado_hueco: return False
            cola.append(nodo.izquierdo)
        else:
            encontrado_hueco = True
        if nodo.derecho:
            if encontrado_hueco: return False
            cola.append(nodo.derecho)
        else:
            encontrado_hueco = True
    return True


# 5. Balancear árbol
def balancear_arbol(self):
    elementos = self.inorden()
    self.raiz = self._construir_balanceado(elementos, 0, len(elementos)-1)

def _construir_balanceado(self, elementos, inicio, fin):
    if inicio > fin:
        return None
    medio = (inicio + fin) // 2
    nodo = NodoArbol(elementos[medio])
    nodo.izquierdo = self._construir_balanceado(elementos, inicio, medio-1)
    nodo.derecho = self._construir_balanceado(elementos, medio+1, fin)
    return nodo
