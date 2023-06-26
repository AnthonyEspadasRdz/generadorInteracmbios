## Definicion de la clase nodo usada en los arboles

class Nodo:
    usuario = None ## informacion del usuario que guarda
    izquierdo = None ## hijo izquierdo
    derecho = None ## hijo derecho

    def __init__(self, usuario):
        self.usuario = usuario
        self.izquierdo = None
        self.derecho = None