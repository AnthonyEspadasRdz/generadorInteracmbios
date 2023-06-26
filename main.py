import funciones
from arbol_class import Arbol
from usuario_class import Usuario

arbolUsuarios = funciones.leerXML("usuarios")

print("Los usuarios registrados son:")
Arbol.imprimirArbol(arbolUsuarios.raiz)

opcionUsuarios = 1
while opcionUsuarios:

    print("\nQue quieres hacer:\n(1) Agregar Nuevo usuario\n(2) Consultar informacion de un usuario\n(3) ver lista de usuarios\n(0) Salir del programa")
    opcionUsuarios = funciones.capturarSeleccion(0, 3)

    if opcionUsuarios == 1:
        print("\nIntroduce al nuevo usuario: ", end="")
        nuevoUsuario = str(input())
        exito = Arbol.agregarUsuario(arbolUsuarios.raiz, nuevoUsuario, "password")
    elif opcionUsuarios == 2:
        seguirConsultando = 1
        while seguirConsultando:
            Usuario.consultarArbolUsuarios(arbolUsuarios)
            print("\n(1) Revisar otro usuario   (0) Volver al menu")
            seguirConsultando = funciones.capturarSeleccion(0, 1)
    elif opcionUsuarios == 3:
        print("\nLos usuarios registrados son:")
        Arbol.imprimirArbol(arbolUsuarios.raiz)


## Al finalizar se guardan los cambios
funciones.escribirXML(arbolUsuarios)