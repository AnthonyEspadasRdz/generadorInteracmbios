"""
Definicion de las funciones de apoyo usadas a lo largo de la ejecucion
"""

## Funcion que captura la eleccion del usuario, verificando que este en los
## parametros adecuados

from arbol_class import Arbol
from usuario_class import Usuario

def capturarSeleccion(minimo, maximo):
    while True: # Ciclo while que se ejecute indefinidamente
        try:
            print("\nSeleccion: ", end="")
            seleccion = int(input())
        
            if seleccion >= minimo and seleccion <= maximo:
                return seleccion # Se sale solo cuando el numero es valido
            else:
                print("La seleccion debe estar entre {} y {}".format(minimo, maximo))
        
        except: # Cuando se introduce algo distinto a un entero
            print("El valor debe ser un numero entero")

## Funcion de busqued lineal que corrobora si en una lista ya existe un elemento
def corroborarExistencia(Arreglo, elementoBuscado):
    for i in range(0, len(Arreglo)):
        if Arreglo[i] == elementoBuscado:
            return True
        
    return False

## Funciones de merge sort para que ordenar las listas de los usuarios
def partir(arreglo, indIzq, indDer):
    return arreglo[indIzq:indDer+1]

def ordenar(arreglo, minimo, medio, maximo):
    izq = partir(arreglo, minimo, medio)
    der = partir(arreglo, medio+1, maximo)

    i = j = 0

    for k in range(minimo, maximo+1):
        if (j >= len(der)) or (i < len(izq) and izq[i] < der[j]):
            arreglo[k] = izq[i]
            i += 1
        else:
            arreglo[k] = der[j]
            j += 1

def merge(arreglo, minimo, maximo):
    if maximo-minimo > 0:
        medio = int((minimo+maximo)/2) 
        merge(arreglo, minimo, medio)
        merge(arreglo, medio+1, maximo)
        ordenar(arreglo, minimo, medio, maximo)

## Funcion encargada de escribir cada usuario en el XML
def escribirUsuario(usuario, archivo):
    archivo.write("<usuario>\n")
    archivo.write("<nombre>")
    archivo.write(usuario.nombre)
    archivo.write("</nombre>\n")
    archivo.write("<password>")
    archivo.write(usuario.password)
    archivo.write("</password>\n")

    if usuario.destinatario == None:
        archivo.write("<destinatario>")
        archivo.write("")
        archivo.write("</destinatario>\n")
    else:
        archivo.write("<destinatario>\n")
        archivo.write(usuario.destinatario)
        archivo.write("</destinatario>\n")
    
    archivo.write("<deseados>\n")
    
    for item in usuario.deseados:
        archivo.write("<item>")
        archivo.write(item)
        archivo.write("</item>\n")
        
    archivo.write("</deseados>\n")
    
    archivo.write("<seleccionado>")
    archivo.write(str(usuario.seleccionado))
    archivo.write("</seleccionado>\n")
    archivo.write("</usuario>\n")

##funcion encargada de iterar en el arbol de usuarios
def escribirNodo(nodo, archivo):
    ## Se escribe el nodo actual
    escribirUsuario(nodo.usuario, archivo)
    ## Se escribe la rama izquierda
    if nodo.izquierdo != None:
        escribirNodo(nodo.izquierdo, archivo)
    ## Se escribe la rama derecha
    if nodo.derecho != None:
        escribirNodo(nodo.derecho, archivo)

## Funcion que inizializa la escritura del archivo
def escribirXML(usuarios):
    archivo = "usuarios.xml"

    with open(archivo, "w", encoding='utf-8') as archivo:
        archivo.write("<dataset>\n")
        escribirNodo(usuarios.raiz, archivo)
        archivo.write("</dataset>")

## Funcion que lee los datos del archivo
def obtenerDataset(archivo):
    archivo += ".xml"

    with open(archivo, "r", encoding='utf-8') as archivo:
        informacion = archivo.read()
        dataset = informacion[informacion.find("<dataset>")+10:informacion.find("</dataset>")]
    
    return dataset

## Funcion que separa a cada uno de los usuarios
def obtenerUsuarios(dataset):
    usuarios = [] # Lista para guardar los registro encontrados
    apuntador = dataset.find("<usuario>") # Apuntador para controlar el recorrido por el archivo

    while apuntador != -1: # Se ejecuta hasta obtener todos los registros
        finRegistro = dataset.find("</usuario>", apuntador+8) # Se busca el fin del registro
        usuarios.append(dataset[apuntador+8:finRegistro]) # Se agrega el registro a la lista
        apuntador = dataset.find("<usuario>", finRegistro) # Se busca un nuevo registros

    return usuarios # Se devuelven los registros

## Funcion que se encarga de crear el arbol
def generarArbol(usuarios):
    arbolUsuarios = None # Se crea el arbol vacio

    for registro in usuarios:
        ## Se captura los atributos de cada usuario
        usuario = registro[registro.find("<nombre>")+8:registro.find("</nombre>")] # Se agrega el usuario
        password = registro[registro.find("<password>")+10:registro.find("</password>")] # Se agrega la contraseña
        destinatario = registro[registro.find("<destinatario>")+14:registro.find("</destinatario>")] # Se agrega el destinatario
        seleccionado = registro[registro.find("<seleccionado>")+14:registro.find("</seleccionado>")] # Se agrega el destinatario

        ## Se genera la lista de items en la lista de deseados del usuario
        items = []
        apuntador = registro.find("<item>")

        while apuntador != -1: 
            finRegistro = registro.find("</item>", apuntador+6) 
            items.append(registro[apuntador+6:finRegistro]) 
            apuntador = registro.find("<item>", finRegistro)

        ## Si es el primer registro, se inicia el arbol
        if arbolUsuarios == None:
            arbolUsuarios = Arbol(usuario, password)
        ## En caso contrario solo se agrega
        else:
            Arbol.agregarUsuario(arbolUsuarios.raiz, usuario, password)
        
        usuarioActual = None
        usuarioActual = Arbol.localizarUsuario(arbolUsuarios.raiz, usuario, usuarioActual)

        ## Se agrega el destinatario
        if destinatario == "":
            usuarioActual.destinatario = None
        else: ## Se busca la direccion al nuevo usuario
            usuarioActual.destinatario = Arbol.localizarUsuario(arbolUsuarios.raiz, destinatario, usuarioActual.destinatario)

        ## Se agrega si ya fue seleccionado
        if seleccionado == True:
            usuarioActual.seleccionado = True
        else:
            usuarioActual.seleccionado = False

        usuarioActual.deseados = items
    
    return arbolUsuarios # Se devuelve el arbol

## Funcion llamada en el main para la lectura del XML con los datos
def leerXML(archivo):
    dataset = obtenerDataset(archivo)
    usuarios = obtenerUsuarios(dataset)
    arbolUsuarios = generarArbol(usuarios)

    return arbolUsuarios
