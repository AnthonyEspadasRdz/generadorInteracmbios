## Definicion de la clase arbol, 
## usada para el manejor de los usuarios

import usuario_class
from nodo_class import Nodo

class Arbol:
    raiz = None

    def __init__(self, usuario, password):
        self.raiz = Nodo(usuario_class.Usuario(usuario, password))

    ## Funcion que agrega nuevos usaurios al arbol, no acepta repetidos
    def agregarUsuario(nodo, nombreUsuario, password):
        ## Para el caso que en que se este agregando la raiz
        if nodo == None: 
                nodo = Arbol(usuario_class.Usuario(nombreUsuario, password))
        ## En caso de que el nombre de ususario ya esta registrado
        elif nodo.usuario.nombre == nombreUsuario: 
            print("El usuario {} no esta disponible".format(nombreUsuario))
            return False
        ## Revisamos el subarbol izquierdo
        elif nodo.izquierdo != None and nombreUsuario < nodo.usuario.nombre:
            Arbol.agregarUsuario(nodo.izquierdo, nombreUsuario, password)
        ## Revisamos el subarbol derecho
        elif nodo.derecho != None and nombreUsuario > nodo.usuario.nombre:
            Arbol.agregarUsuario(nodo.derecho, nombreUsuario, password)
        ## Si se llego al final y el usuario no tuvo coincidencias, se agrega
        else:
            ## Si es menor, se coloca a la izquierda
            if nombreUsuario < nodo.usuario.nombre:
                nodo.izquierdo = Nodo(usuario_class.Usuario(nombreUsuario, password))
            ## De lo contrario, se guarda a la derecha
            else:
                nodo.derecho = Nodo(usuario_class.Usuario(nombreUsuario, password))

    ## Funcion usada para localizar un usuario dentro del arbol
    def localizarUsuario(nodo, nombreUsuario, usuario):
        ## Para el caso que se busque en un arbol vacio
        if nodo == None: 
                print("Aun no hay usuarios registrados")
        ## Si se localiza al usuario, se devuelve su guarda el apuntador
        elif nodo.usuario.nombre == nombreUsuario: 
            usuario = nodo.usuario
            return usuario
        ## Revisamos el subarbol izquierdo
        elif nodo.izquierdo != None and nombreUsuario < nodo.usuario.nombre:
            usuario = Arbol.localizarUsuario(nodo.izquierdo, nombreUsuario, usuario)
        ## Revisamos el subarbol derecho
        elif nodo.derecho != None and nombreUsuario > nodo.usuario.nombre:
            usuario = Arbol.localizarUsuario(nodo.derecho, nombreUsuario, usuario)
        ## Se corrobora si el valor de usuario fue captaado
        if usuario != None:
            return usuario

    ## Funcion que imprime todos los nodos en el arbol
    def imprimirArbol(nodo):
        ## Mientras no llegue a un nodo hoja, hara un recorrido recursivo en orden alfabetico
        if nodo != None: 
            Arbol.imprimirArbol(nodo.izquierdo)
            print(nodo.usuario.nombre)
            Arbol.imprimirArbol(nodo.derecho)