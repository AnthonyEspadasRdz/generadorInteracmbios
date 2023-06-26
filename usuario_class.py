## Definicion de la clase usario, 
## que se usara en los nodos para las estructuras de arbol 
## y para la construccion del grafos 

import funciones    
import arbol_class

class Usuario:
    nombre = ""
    password = ""
    destinatario = None # Guarda el apuntador de la persona a la que regalara
    deseados = [] # Guarda la lista de posibles regalos para el usuario
    seleccionado = False # Para determinar si el usuario ya tiene quien le regale

    def __init__(self, nombre, password):
        self.nombre = nombre
        self.password = password
        self.deseados = []
        self.destinatario = None
        self.seleccionado = False

    ## Funcion para mostrar el destinatario de un
    def consultarDestinatario(usuario):
        if usuario.destinatario == None:
            print("Destinatario aun no asignado")
        else:
            print("Tu destinatario es {}".format(usuario.destinatario))

    ## Funcion para mostrar la lista de posibles regalos para un usuario
    def mostrarLista(usuario):
        if usuario.deseados == []:
            print("\nEl usuario {} no tiene regalos registrados".format(usuario.nombre))
        else:
            print("\nLa lista del usuario {} es:".format(usuario.nombre))
            for articulo in usuario.deseados:
                print(articulo)

    ## Funcion para aregar un nuevo articulo a la lista de deseados del usuario
    def agregarElemento(usuario):
        print("Introduce lo que quieres agregar a la lista: ", end="")
        nuevoArticulo = str(input())
        ## En listas vacias se agrega sin hacer modificaciones
        if usuario.deseados == []:
            usuario.deseados.append(nuevoArticulo)
            print("\n{} se ha agregado a tu lista de deseados".format(nuevoArticulo))
        ## En listas con al menos un elemento se revisa que no este registrado ya
        else:
            if funciones.corroborarExistencia(usuario.deseados, nuevoArticulo):
                print("\n{} ya se encuentra en tu lista".format(nuevoArticulo))
            else:
                usuario.deseados.append(nuevoArticulo)
                print("\n{} se ha agregado a tu lista de deseados".format(nuevoArticulo))
                funciones.merge(usuario.deseados, 0, len(usuario.deseados)-1)

    ## Funcion para aregar un eliminar articulo a la lista de deseados del usuario
    def eliminarElemento(usuario):
        ## En listas vacias no se hace nada
        if usuario.deseados == []:
            print("\nLa lista no contiene articulos")
        ## En listas con al menos un elemento se revisa que el articulo existe
        else: ## Si existe, se elimina
            print("Introduce lo que quieres eliminar de la lista: ", end="")
            articuloEliminado = str(input())
            
            if funciones.corroborarExistencia(usuario.deseados, articuloEliminado):
                ## Para suprimir el elemento se recorren los valores a la siguiente posicion
                for i in range(usuario.deseados.index(articuloEliminado), len(usuario.deseados)-1):
                    usuario.deseados[i] = usuario.deseados[i+1]
                # Y se elimina el ultimo
                usuario.deseados.pop(len(usuario.deseados)-1)
                print("\n{} se elimino de la lista".format(articuloEliminado))
            else: ## De no existir se noticia
                print("\n{} no se encuentra en la lista".format(articuloEliminado))

    ## Funcion con la cual el usuario realiza sus acciones
    def opcionesUsuario(usuarioActual):
        print("\nSelecciona una opcion:")
        print("(1) Ver a quien regalo")
        print("(2) Ver mi lista de deseados")
        print("(3) Agregar opcion a mi lista")
        print("(4) Quitar opcion de mi lista")
        
        seleccionAccion = funciones.capturarSeleccion(1, 4)

        if seleccionAccion == 1:
            Usuario.consultarDestinatario(usuarioActual)
        elif seleccionAccion == 2:
            Usuario.mostrarLista(usuarioActual)
        elif seleccionAccion== 3:
            Usuario.agregarElemento(usuarioActual)
        elif seleccionAccion == 4:
            Usuario.eliminarElemento(usuarioActual)

    ## Funcion para consultar informacion de los usuarios dentro del arbol
    def consultarArbolUsuarios(arbolUsuarios):
        print("\nIntroduce el nombre de usuario: ", end="")
        nombreBuscao = str(input())
        usuarioActual = None # Se registra como None para tener un valor por default
        ## Si se encontro una coincidencia, su valor cambiara
        usuarioActual = arbol_class.Arbol.localizarUsuario(arbolUsuarios.raiz, nombreBuscao, usuarioActual)

        if usuarioActual == None:
            print("\nEl usuario {} no esta registrado".format(nombreBuscao))
        else:
            print("Introduce el password de {} (todos los password son ""password""): ".format(usuarioActual.nombre), end="")
            passwordIntroducido = str(input())
            ## Si el password no coincide no es posible realizar las operaciones
            if passwordIntroducido == usuarioActual.password:
                continuarOperando = 1
                
                while continuarOperando:
                    Usuario.opcionesUsuario(usuarioActual)
                    print("\nQuieres realizar otra operacion: (1) Si  (0) No", end="")
                    continuarOperando = funciones.capturarSeleccion(0, 1)
                
            else:
                print("Password Incorrecto")