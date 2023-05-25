from jarvis_functions import calcular_min_max_dato
from jarvis_functions import calcular_promedio
from jarvis_functions import stark_normalizar_datos
from jarvis_functions import obtener_nombre_y_dato
from jarvis_functions import stark_calcular_imprimir_heroe
from jarvis_functions import stark_imprimir_nombres_alturas
from jarvis_functions import stark_imprimir_nombres_heroes
from jarvis_functions import stark_menu_principal
from jarvis_functions import stark_imprimir_promedio_altura
# Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M

# desafio 01 
def lista_segun_genero(lista:list,genero:str)->list:
    """ funcion que retorna una lista, segun el genero que se le pase por parametro """
    nueva_lista = []
    for elementos in lista:
        if(elementos['genero'] == genero):
            nueva_lista.append(elementos)
    return nueva_lista
 
# A
def imprimir_heroes_masculinos(lista:list):
    """ funcion que imprime los elementos de la lista que sean [masculinos] """
    lista_masculinos = lista_segun_genero(lista,'M')
    for elementos in lista_masculinos:
        print('Nombre heroe masculinos : {} '.format(elementos['nombre']))
            
# B
def imprimir_heroes_femeninos(lista:list):
    """ funcion que imprime los elementos de la lista que sean [femeninos] """
    lista_femeninos = lista_segun_genero(lista,'F')
    for elementos in lista_femeninos:
        print('Nombre heroe femenino : {}'.format(elementos['nombre']))
            

def encontrar_altura_segun_genero(lista:list,genero:str,estado:str)->dict:
    """ funcion que retorna un diccionario dependiendo las opciones que se le den
    recibe como parametro: la lista a iterar, el genero que se necesita operar, y si busca el maximo o el minimo [estado]"""
    lista_generar = lista_segun_genero(lista,genero)
    max_o_min = calcular_min_max_dato(lista_generar,estado,'altura')
    return max_o_min

def imprimir_salida_altura(dic:dict,estado:str,genero:str):
    """ funcion que imprime la salida formateada del diccionario que se recibe por parametro\n
     'maximo/minimo' , genero , nombre, altura """
    print("Heroe mas {} {} : {}  altura:  {}"
          .format(estado,genero,dic['nombre'],float(dic['altura'])))
# C 
def imprimir_heroe_mas_alto_masculino(lista:list):
    """ funcion que recibe la lista, e imprime el maximo de las alturas masculinas """
    maximo_alto_M = encontrar_altura_segun_genero(lista,'M','maximo')
    imprimir_salida_altura(maximo_alto_M,'alto','masculino')

# D
def imprimir_heroe_mas_alto_femenino(lista:list):
    """ funcion que recibe la lista, e imprime el maximo de las alturas femeninas """
    maximo_alto_F = encontrar_altura_segun_genero(lista,'F','maximo')
    imprimir_salida_altura(maximo_alto_F,'alto','femenino')

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
def imprimir_heroe_mas_bajo_masculino(lista:list):
    """ funcion que recibe la lista, e imprime el minimo de las alturas masculinas """
    maximo_bajo_M = encontrar_altura_segun_genero(lista,'M','minimo')
    imprimir_salida_altura(maximo_bajo_M,'bajo','masculino')

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
def imprimir_heroe_mas_bajo_femenino(lista:list):
    """ funcion que recibe la lista, e imprime el minimo de las alturas femeninas """
    maximo_bajo_F = encontrar_altura_segun_genero(lista,'F','minimo')
    imprimir_salida_altura(maximo_bajo_F,'bajo','femenino')


def calcular_promedio_segun_genero( lista:list, genero:str , key:str )->float:
    """ funcion que recibe la lista , el genero , y la key\n
    retorna el promedio de los elementos de la key seleccionada"""
    lista_nueva = lista_segun_genero(lista,genero) 
    return calcular_promedio(lista_nueva,key)


def calcular_altura_promedio_masculino(lista:list):
    """ funcion que recibe la lista , llama a calcular promedio de las alturas masculinas e imprime el resultado formateado """
    promedio = calcular_promedio_segun_genero(lista,'M','altura')
    print("promedio de alturas genero masculino: {}" .format(promedio))

def calcular_altura_promedio_femenino(lista:list):
    """ funcion que recibe la lista , llama a calcular promedio de las alturas femeninas e imprime el resultado formateado """
    
    promedio = calcular_promedio_segun_genero(lista,'F','altura')
    print("promedio de alturas genero femenino: {}" .format(promedio))



# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def contar_x_color(lista:list , color:str , pelo_ojos:str )->int:
    """ funcion que retorna la cantidad de heroes que tienen dicho color, 
     recibe por parametro la lista, el color a contar, y lo que se quiere contar si colores de ojos o colores de pelo """
    contador = 0
    if(pelo_ojos == 'ojos'):
        for elementos in lista:
            if(elementos['color_ojos'] == color):
                #print(obtener_nombre_y_dato(elementos,'color_ojos'))
                contador+=1
        return contador
    elif(pelo_ojos == 'pelo'):
        for elementos in lista:
            if(elementos['color_pelo'] == color):
                #print(obtener_nombre_y_dato(elementos,'color_pelo'))
                contador+=1
        return contador
#J
def cada_color_ojos_heroe(lista:list):
    """ funcion que imprime los heroes , su color de ojos y la cantidad que poseen ese color"""
    colores_ojos = ['Red', 'Blue', 'Silver', 'Brown', 'Hazel', 'Green', 'blue', 'Yellow', 'Yellow (without irises)']
    for elementos in colores_ojos:
        contador = contar_x_color(lista,elementos,'ojos')
        print("cuantos heroes tienen color {} : {}  \n ".format(elementos,contador))


#K
def cada_color_pelo_heroe(lista:list):
    """ funcion que imprime los heroes , su color de pelo y la cantidad que poseen ese color"""
    lista_colores_pelo = ['', 'No Hair', 'Black', 'Brown / White', 'Blond', 'White', 'Brown', 'Red', 'blond', 'Green', 'Yellow', 'Auburn', 'Red / Orange']
    for elementos in lista_colores_pelo:
        contador = contar_x_color(lista,elementos,'pelo')
        print("cuantos heroes tienen pelo color {} : {}  \n ".format(elementos,contador))


#L Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener,Inicializarlo con ‘No Tiene’).
    """ funcion que imprime los heroes y su inteligencia """
def cada_inteligencia_heroe(lista:list):
    for elementos in lista:
        if(elementos['inteligencia'] == ""):
            elementos['inteligencia'] = 'no tiene'
        print(obtener_nombre_y_dato(elementos,'inteligencia'))

def retornar_heroe_x_color(lista:list , buscar:str ,color:str )->list:
    """ funcion que retorna una lista de heroes que cumplan con el color que llega por parametro.\n
     recibe la lista de heroes , el elemento a buscar y el color a buscar """
    lista_vacia = []
    if(buscar == 'color_ojos'):
        for elementos in lista:
            if(elementos['color_ojos'] == color):
                lista_vacia.append(elementos)
    elif(buscar == 'color_pelo'):
        for elementos in lista:
            if(elementos['color_pelo'] == color):
                lista_vacia.append(elementos)
    return lista_vacia

#M. Listar todos los superhéroes agrupados por color de ojos.
def crear_lista_ojos_segun_color(lista:list):
    """ funcion que crea una lista de diccionarios donde cada diccionario es un color_de_ojos
  y dentro estan los heroes agrupados.\n\n al final se imprime dicha lista de diccionarios"""

    colores_ojos = ['Red', 'Blue', 'Silver', 'Brown', 'Hazel', 'Green', 'blue', 'Yellow', 'Yellow (without irises)']
    lista_x_color = []

    for elementos in colores_ojos:
        diccionario_a_guardar = {f"{elementos}":retornar_heroe_x_color(lista,'ojos',elementos)}
        lista_x_color.append(diccionario_a_guardar)
    return lista_x_color
    for elementos in lista_x_color:
        print("\n\n",elementos)
    
#N. Listar todos los superhéroes agrupados por color de ojos.
def crear_lista_pelo_segun_color(lista:list):
    """ funcion que crea una lista de diccionarios donde cada diccionario es un color_de_pelo
  y dentro estan los heroes agrupados.\n\n al final se imprime dicha lista de diccionarios"""

    lista_colores_pelo = ['', 'No Hair', 'Black', 'Brown / White', 'Blond', 'White', 'Brown', 'Red', 'blond', 'Green', 'Yellow', 'Auburn', 'Red / Orange']

    lista_x_color = []

    for elementos in lista_colores_pelo:
        diccionario_a_guardar = {f"{elementos}":retornar_heroe_x_color(lista,'pelo',elementos)}
        lista_x_color.append(diccionario_a_guardar)

    for elementos in lista_x_color:
        print("\n\n",elementos)

#O Listar todos los superhéroes agrupados por tipo de inteligencia
def crear_lista_segun_intelicense(lista:list , inteligencia:str)->list:
    """ funcion que retorna una lista de diccionarios que cumplan con la inteligencia que llega por parametro\n\n
    recibe una lista de heroes y una inteligencia a buscar"""
    lista_aux = []

    for elementos in lista:
        if(elementos['inteligencia'] == ''):
            elementos['inteligencia'] = 'no tiene'

        if(elementos['inteligencia'] == inteligencia):
            lista_aux.append(elementos)

    return lista_aux   



def listar_x_inteligencia(lista:list):
    """ funcion que crea una lista de diccionarios donde cada diccionario es una inteligencia
  y dentro estan los heroes agrupados.\n\n al final se imprime dicha lista de diccionarios"""
    lista_inteligencia = ['no tiene', 'good', 'average', 'high']
    lista_final = []
    for elementos in lista_inteligencia:
        dic_a_crear = {f'{elementos}':crear_lista_segun_intelicense(lista,elementos)}
        lista_final.append(dic_a_crear)
    
    for elementos in lista_final:
        print("\n\n",elementos)

def stark_marvel_app(lista:list):
    """ funcion que ejecuta la aplicacion principal """
    opcion = None
    stark_normalizar_datos(lista)

    while(opcion!=0):
        opcion = stark_menu_principal()

        if(opcion == 1): # desafio 00
            stark_imprimir_nombres_heroes(lista)
        elif(opcion == 2):
            stark_imprimir_nombres_alturas(lista)
        elif(opcion == 3):
            stark_calcular_imprimir_heroe(lista,'maximo','altura')
        elif(opcion == 4):
            stark_calcular_imprimir_heroe(lista,'minimo','altura')
        elif(opcion == 5):
            stark_imprimir_promedio_altura(lista)
        elif(opcion == 6):
            stark_calcular_imprimir_heroe(lista,'maximo','peso')
            stark_calcular_imprimir_heroe(lista,'minimo','peso')


        elif(opcion == 7):  # desafio  01
            imprimir_heroes_masculinos(lista)
        elif(opcion == 8):
            imprimir_heroes_femeninos(lista)
        elif(opcion == 9):
            imprimir_heroe_mas_alto_masculino(lista)
        elif(opcion == 10):
            imprimir_heroe_mas_alto_femenino(lista)
        elif(opcion == 11):
            imprimir_heroe_mas_bajo_masculino(lista)
        elif(opcion == 12):
            imprimir_heroe_mas_bajo_femenino(lista)
        elif(opcion == 13):
            calcular_altura_promedio_masculino(lista)
        elif(opcion == 14):
            calcular_altura_promedio_femenino(lista)
        elif(opcion == 15):
            cada_color_ojos_heroe(lista)
        elif(opcion == 16):
            cada_color_pelo_heroe(lista)
        elif(opcion == 17):
            cada_inteligencia_heroe(lista)
        elif(opcion == 18):
            crear_lista_ojos_segun_color(lista)
        elif(opcion == 19):
            crear_lista_pelo_segun_color(lista)
        elif(opcion == 20):
            listar_x_inteligencia(lista)
        elif(opcion == 0):
            break

