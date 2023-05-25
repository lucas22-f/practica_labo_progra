from jarvis_functions import *
from jarvis_functions01 import *
import re
import json



def imprimir_menu_desafio_5():
    imprimir_dato("\n\nA. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M\n"
                  "B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F\n"
                  "C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\n"
                  "D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\n"
                  "E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M\n"
                  "F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F\n"
                  "G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M\n"
                  "H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F\n"
                  "I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores\n"
                  "anteriores (ítems C a F)\n"
                  "J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\n"
                  "K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\n"
                  "L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener,\n"
                  "Inicializarlo con ‘No Tiene’).\n"
                  "M. Listar todos los superhéroes agrupados por color de ojos.\n"
                  "N. Listar todos los superhéroes agrupados por color de pelo.\n"
                  "O. Listar todos los superhéroes agrupados por tipo de inteligencia\n"
                  "Z. SALIR\n")


# 1.2
""" 1.2. Crear la funcion 'stark_menu_principal_desafio_5' la cual se encargará
de imprimir el menú de opciones y le pedirá al usuario que ingrese la
letra de una de las opciones elegidas, deberá validar la letra usando
RegEx y en caso de ser correcta tendrá que retornarla, Caso contrario
retornará -1. El usuario puede ingresar tanto letras minúsculas como
mayúsculas y ambas se deben tomar como válidas
Reutilizar la función 'imprimir_menu_Desafio_5' """


def stark_menu_principal_desafio_5() -> str:
    """ funcion que retorna la opcion ingresada por el usuario, validandola con Regex. """
    imprimir_menu_desafio_5()
    letra = input("\n\nIngresa una opcion\n\n")
    retorno = ''
    if re.search(r"[a-zA-Z]", letra):
        retorno = letra.upper()
    else:
        retorno = -1

    return retorno

print(stark_menu_principal_desafio_5())
# 1.3
""" Crear la función 'stark_marvel_app_5' la cual recibirá por parámetro la
lista de héroes y se encargará de la ejecución principal de nuestro
programa. (usar if/elif o match según prefiera) Reutilizar las funciones
con prefijo 'stark_' donde crea correspondiente. """


def stark_marvel_app_5(lista: list):

    opcion = stark_menu_principal_desafio_5()
    stark_normalizar_datos(lista)
    while (opcion != 'Z'):

        if (opcion == 'A'):
            imprimir_heroes_masculinos(lista)
        elif (opcion == 'B'):
            imprimir_heroes_femeninos(lista)
        elif (opcion == 'C'):
            imprimir_heroe_mas_alto_masculino(lista)
        elif (opcion == 'D'):
            imprimir_heroe_mas_alto_femenino(lista)
        elif (opcion == 'E'):
            imprimir_heroe_mas_bajo_masculino(lista)
        elif (opcion == 'F'):
            imprimir_heroe_mas_bajo_femenino(lista)
        elif (opcion == 'G'):
            calcular_altura_promedio_masculino(lista)
        elif (opcion == 'H'):
            calcular_altura_promedio_femenino(lista)
        elif (opcion == 'I'):
            print("implicito en cada funcion")
        elif (opcion == 'J'):
            cada_color_ojos_heroe(lista)
        elif (opcion == 'K'):
            cada_color_pelo_heroe(lista)
        elif (opcion == 'L'):
            cada_inteligencia_heroe(lista)
        elif (opcion == 'M'):
            crear_lista_ojos_segun_color(lista)
        elif (opcion == 'N'):
            crear_lista_pelo_segun_color(lista)
        elif (opcion == 'O'):
            listar_x_inteligencia(lista)
        elif (opcion == 'Z'):
            opcion = 'Z'
        else:
            print("Error")
        opcion = stark_menu_principal_desafio_5()


# 1.4
""" Crear la función 'leer_archivo' la cual recibirá por parámetro un string
que indicará el nombre y extensión del archivo a leer (Ejemplo:
archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
retornará la lista de héroes como una lista de diccionarios. """


def leer_archivo(string: str) -> list:
    """ funcion que lee un archivo y retorna una lista de diccionarios de ese archivo en concreto """

    # forma light
    """ with open(string,'r') as archivo:
        data = json.load(archivo)
    return data['heroes'] """

    # forma calorica:
    lista_final = []

    with open(string, 'r') as archivo:


        texto_general = archivo.read()


        nombres = re.findall(r"\"nombre\": \"([a-zA-Z- ]+)\"", texto_general)
        identidades = re.findall(r"\"identidad\": \"([a-zA-Z \(\)]+)\"", texto_general)
        empresas = re.findall(r"\"empresa\": \"([a-zA-Z ]+)\"", texto_general)
        alturas = re.findall(r"\"altura\": \"([0-9]+\.[0-9]+)\"", texto_general)
        pesos = re.findall(r"\"peso\": \"([0-9]+\.[0-9]+)\"", texto_general)
        generos = re.findall(r"\"genero\": \"([A-Z]+)\"", texto_general)
        colores_ojos = re.findall(r"\"color_ojos\": \"([a-zA-Z- \(\)]+)\"", texto_general)
        colores_pelo = re.findall(r"\"color_pelo\": \"([\"a-zA-Z /]{0,13})\"", texto_general)
        fuerzas = re.findall(r"\"fuerza\": \"([0-9]+)\"", texto_general)
        inteligencia = re.findall(r'"inteligencia": "([\"a-z]{0,7})"', texto_general)


        for i in range(len(nombres)):
            nuevo_dict = {}
            nuevo_dict['nombre'] = nombres[i]
            nuevo_dict['identidad'] = identidades[i]
            nuevo_dict['empresa'] = empresas[i]
            nuevo_dict['altura'] = alturas[i]
            nuevo_dict['peso'] = pesos[i]
            nuevo_dict['genero'] = generos[i]
            nuevo_dict['color_ojos'] = colores_ojos[i]
            nuevo_dict['color_pelo'] = colores_pelo[i]
            nuevo_dict['fuerza'] = fuerzas[i]
            nuevo_dict['inteligencia'] = inteligencia[i]
            lista_final.append(nuevo_dict)
        return lista_final

lista_personajes = leer_archivo("C:\\Users\\Lucas\\Desktop\\google-python-exercises\\clase 8\\data_stark.json")
# 1.5
def guardar_archivo(nombre: str, contenido: str) -> bool:
    if (type(contenido) == type(str()) and contenido!=""):
        with open(nombre, 'w+') as archivo:
            archivo.write(contenido)
            print(".Se creó el archivo: {}".format(nombre))
            return True
    else:
        return False        

# 1.6

def capitalizar_palabras(palabras:str):
    spliteados = palabras.split()
    nueva_list=[]
    for elementos in spliteados:
        capitalizados = elementos.capitalize()
        nueva_list.append(capitalizados)
        #nota mental... el join() se utiliza para unir en una string los elementos de una lista [SI,O,SI,UNA,LISTA] 
        # ['si','o','si','una','lista']  ---> join(lista) --->   "si o si una lista"
    retorno =" ".join(nueva_list)

    return retorno

# 1.7

def obtener_nombre_capitalizado(dicc:dict)->str:
    nombre_capitalizado = capitalizar_palabras(dicc['nombre'])
    return f"Nombre: {nombre_capitalizado}"

# 1.8

def obtener_nombre_y_dato(dicc:dict,key:str)->str:
    return " {} : | {} : {} ".format(obtener_nombre_capitalizado(dicc),key.capitalize(),dicc[key])


#2.1

def es_genero(heroe:dict,genero:str)->bool:
   
    if(type(genero) == type(str()) and genero=='M' or genero =='F' or genero == 'NB'):
        if(heroe['genero'] == genero ):
            return True
        else:
            return False
    else:
        return False



#2.2

def stark_guardar_heore_genero(lista:list,genero:str)->bool:
    retorno = 0
    if(len(lista) > 0):
        lista_encontrados = []
        for elementos in lista:
            if es_genero(elementos,genero):
                imprimir_dato(obtener_nombre_capitalizado(elementos))
                lista_encontrados.append(obtener_nombre_capitalizado(elementos))
        contenido_final = " , ".join(lista_encontrados)
        if guardar_archivo(f'heroes_{genero}.csv',contenido_final):
            retorno =  True
        else:
            retorno =  False
    else:
        retorno = False    
    return retorno



#3.1
""" 

Basandote en la función 'calcular_min', crear la función
'calcular_min_genero' la cual recibirá como parámetro extra un string
que representa el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el mínimo (peso, altura u otro dato) 

"""
def calcular_min_genero(lista:list,key:str,genero:str)->dict:
    flag = True
    menor = {}
    for elementos in lista:
        if(elementos['genero'] == genero):
            if flag == True or float(elementos[key]) < float(menor[key]):
                menor = elementos
                flag = False

    return menor


calcular_min_genero(lista_personajes,'altura','M')

# 3.2
""" 
Basandote en la función 'calcular_max', crear la función
'calcular_max_genero' la cual recibirá como parámetro extra un string
que representará el género de la heroína/héroe a buscar. modificar un
poco la lógica para que dentro no se traiga por defecto al primer héroe
de la lista sino que mediante un flag, se traiga el primer héroe que
COINCIDA con el género pasado por parámetro. A partir de allí, podrá
empezar a comparar entre héroes o heroínas que coincidan con el
género pasado por parámetro. La función retornará el héroe o heroína
que cumpla la condición de tener el máximo (peso, altura u otro dato)
"""

def calcular_max_genero(lista:list,key:str,genero:str)->dict:
    flag = True
    mayor = {}

    for elementos in lista:
        if(elementos['genero'] == genero):
            if(flag == True or float(elementos[key]) > float(mayor[key])):
                mayor = elementos
                flag = False
    return mayor


# 3.3
"""

3.3. Basandote en la funcion 'calcular_max_min_dato', crear una funcion
con la misma lógica la cual reciba un parámetro string que
representará el género del héroe/heroína a buscar y renombrarla a
'calcular_max_min_dato_genero'. La estructura será similar a la ya
antes creada, salvo que dentro de ella deberá llamar a
'calcular_max_genero' y 'calcular_min_genero', pasandoles el nuevo
parámetro. Esta función retornará el héroe o heroína que cumpla con
las condiciones pasados por parámetro. Por ejemplo, si se le pasa 'F' y
'minimo', retornará la heroína que tenga el mínimo (altura, peso u otro
dato)

"""
def calcular_min_max_dato_genero( genero:str , lista:list , maxmin:str , key:str ):

    if(maxmin == 'maximo'):
        maximo_minimo = calcular_max_genero(lista,key,genero)
    elif(maxmin == 'minimo'):
        maximo_minimo = calcular_min_genero(lista,key,genero)

    return maximo_minimo

# 3.4
""" 
Basandote en la función 'stark_calcular_imprimir_heroe' crear la
función ‘stark_calcular_imprimir_guardar_heroe_genero’ que además
reciba un string el cual representará el género a evaluar. El formato de
mensaje a imprimir deberá ser estilo:
Mayor Altura: Nombre: Gamora | Altura: 183.65

"""
def stark_calcular_imprimir_guardar_heroe_genero(lista:list , maxmin:str , key:str ,genero:str):
    if(len(lista) > 0):

        heroe = calcular_min_max_dato_genero(genero,lista,maxmin,key)
        salida = obtener_nombre_y_dato(heroe,key)
        if guardar_archivo('heroes_{}_{}_{}.csv'.format(maxmin,key,genero),salida):
            imprimir_dato("{} {}:  {}".format(maxmin,key,salida))
            return True
        else:
            return False
    else:
        return False
    


# 4.1
""" 
Basandote en la función 'sumar_dato_heroe', crear la función llamada
'sumar_dato_heroe_genero' la cual deberá tener un parámetro extra
del tipo string que representará el género con el que se va a trabajar.
Esta función antes de realizar la suma en su variable sumadora,
deberá validar lo siguiente:

A. El tipo de dato del héroe debe ser diccionario.
B. El héroe actual de la iteración no debe estar vacío (ser
diccionario vacío)

C. El género del héroe debe coincidir con el pasado por
parámetro.

Una vez que cumpla con las condiciones, podrá realizar la suma. La
función deberá retornar la suma del valor de la key de los héroes o
heroínas que cumplan las condiciones o -1 en caso de que no se
cumplan las validaciones

"""

def sumar_dato_heroe_genero(lista:list , key:str , genero:str ) -> float:
     
     if(key=="altura" or key =="fuerza" or key =="peso"):
        suma = 0
        for elementos in lista:
            if type(elementos) == type(dict() and len(elementos) > 0 ):
                if(elementos['genero'] == genero):
                    suma += float(elementos[key])
        return suma
     else:
        return -1
     


# 4.2
""" 
Crear la función 'cantidad_heroes_genero' la cual recibirá por
parámetro la lista de héroes y un string que representará el género a
buscar. La función deberá iterar y sumar la cantidad de héroes o
heroínas que cumplan con la condición de género pasada por
parámetro, retornará dicha suma.

"""
def cantidad_heroes_genero(lista:list,genero:str)->int:
    suma = 0
    for elementos in lista:
        if(elementos['genero'] == genero):
            suma+=1
    
    return suma
    
#4.3
""" 
Basandote en la función 'calcular_promedio', crear la función
'calcular_promedio_genero' la cual tendrá como parámetro extra un
string que representará el género a buscar. la lógica es similar a la
función anteriormente mencionada en el enunciado. Reutilizar las
funciones: 'sumar_dato_heroe_genero', 'cantidad_heroes_genero' y
'dividir'.
retornará el promedio obtenido, según la key y género pasado por
parámetro.

"""

def calcular_promedio_genero(lista:list , key_a_promediar:str, genero:str)->float:
    suma_alturas = sumar_dato_heroe_genero(lista , key_a_promediar, genero)
    promedio = dividir(suma_alturas,cantidad_heroes_genero(lista,genero))

    return promedio

# 4.4

""" 
Basandote en la función ‘stark_calcular_imprimir_promedio_altura',
desarrollar la función 'stark_calcular_imprimir_guardar_
promedio_altura_genero' la cual tendrá como parámetro extra un string
que representará el género de los héroes a buscar.
La función antes de hacer nada, deberá validar que la lista no esté
vacía. En caso de no estar vacía: calculará el promedio y lo imprimirá
formateado al estilo:
Altura promedio género F: 178.45
En caso de estar vacía, imprimirá como mensaje:
Error: Lista de héroes vacía.

Luego de imprimir la función deberá guardar en un archivo los mismos
datos. El nombre del archivo debe tener el siguiente formato:
heroes_promedio_altura_genero.csv
Donde:
A. genero: será el género de los héroes a calcular, siendo M y F
únicas opciones posibles.
Ejemplos:
heroes_promedio_altura_F.csv
heroes_promedio_altura_M.csv

Reutilizar las funciones: 'calcular_promedio_genero', 'imprimir_dato' y
'guardar_archivo'.
Esta función retornará True si pudo la lista tiene algún elemento y
pudo guardar el archivo, False en caso de que esté vacía o no haya
podido guardar el archivo.
"""

def stark_calcular_imprimir_guardar_promedio_altura_genero(lista:list,genero:str):
    if len(lista) > 0:

        altura_promedio = calcular_promedio_genero(lista,'altura',genero)
        string = "Altura promedio género {}: {}".format(genero,altura_promedio)
        imprimir_dato(string)
        if guardar_archivo("heroes_promedio_altura_{}.csv".format(genero),string):
            return True
        else:
            return False
    else:
        print("Error: Lista de héroes vacía.")
        return False

# 5.1

""" 
5.1. Crear la función 'calcular_cantidad_tipo' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc)
Antes de hacer nada, deberá validar que la lista no esté vacía. En caso
de estarlo devolver un diccionario con la siguiente estructura:
La función deberá retornar un diccionario con los distintos valores del
tipo de dato pasada por parámetro y la cantidad de cada uno (crear un
diccionario clave valor).
"""

def calcular_cantidad_tipo(lista:list,key:str)->dict:

    if len(lista) > 0:
        dic = {}
        for elementos in lista:
            color = elementos[key]
            if color in dic:
                dic[capitalizar_palabras(color)]+=1
            else:
                dic[capitalizar_palabras(color)]=1
        return dic
        
    else:
        return {"Error": "La lista se encuentra vacia"}
    

# 5.2.

""" 
Crear la función 'guardar_cantidad_heroes_tipo' la cual recibirá como
parámetro un diccionario que representará las distintas variedades del
tipo de dato (distintos colores de ojos, pelo, etc) como clave con sus
respectivas cantidades como valor. Como segundo parámetro recibirá
el dato (color_pelo, color_ojos, etc) el cual tendrás que usarlo
únicamente en el mensaje final formateado. Esta función deberá iterar
cada key del diccionario y variabilizar dicha key con su valor para
luego formatearlos en un mensaje el cual deberá guardar en archivo.
Por ejemplo:
"Caracteristica: color_ojos Blue - Cantidad de heroes: 9"
Reutilizar la función 'guardar_archivo'. El nombre del archivo final
deberá respetar el formato:
heroes_cantidad_tipoDato.csv
Donde:
● tipoDato: representará el nombre de la key la cual se está
evaluando la cantidad de héroes.
Ejemplo:
heroes_cantidad_color_pelo.csv

heroes_cantidad_color_ojos.csv
La función retornará True si salió todo bien, False caso contrario.

"""
def guardar_cantidad_heroes_tipo(dic:dict,key:str):
    string_final = ""
    datos = []
    for clave,valor in dic.items():
        string_final = f"Caracteristica: {key}  {clave} - Cantidad de heroes : {valor}"
        datos.append(string_final)
    retorno = "\n".join(datos)
    if guardar_archivo(f'heroes_cantidad_{key}.csv',retorno):
        return True
    else:
        return False

# 5.3
""" 
Crear la función 'stark_calcular_cantidad_por_tipo' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato/key a buscar (color_ojos, color_pelo, etc). Dentro deberás
reutilizar 'calcular_cantidad_tipo' y 'guardar_cantidad_heroes_tipo' con
la lógica que cada una de esas funciones manejan.
Esta función retornará True si pudo guardar el archivo, False caso
contrario.

"""

def stark_calcular_cantidad_por_tipo(lista:list,key:str):

    cantidad_tipo = calcular_cantidad_tipo(lista,key)
    if guardar_cantidad_heroes_tipo(cantidad_tipo,key):
        return True
    else:
        return False
    
# 6.1
""" 
Crear la función 'obtener_lista_de_tipos' la cual recibirá por parámetro
la lista de héroes y un string que representará el tipo de dato/key a
buscar (color_ojos, color_pelo, etc).
Esta función deberá iterar la lista de héroes guardando en una lista las
variedades del tipo de dato pasado por parámetro (sus valores).
En caso de encontrar una key sin valor (o string vacío), deberás
hardcodear con el valor 'N/A' y luego agregarlo a la lista donde irás
guardando todos los valores encontrados, si el valor del héroe no tiene
errores, guardarlo tal cual viene.
Finalmente deberás eliminar los duplicados de esa lista y retornarla
como un set.
Reutilizar 'capitalizar_palabras' para guardar cada uno de los datos
con la primera letra mayúscula.
"""
def obtener_lista_de_tipos(lista:list,key:str)->set:

    lista_nueva = []
    for elementos in lista:
        if elementos[key] == "":
            elementos[key] = 'N/A'

        lista_nueva.append(elementos[key])
    
    return set(lista_nueva)

# 6.2
""" 
Crear la función 'normalizar_dato' la cual recibirá por parámetro un
dato de héroe (el valor de una de sus keys, por ejemplo si la key fuese
color_ojos y su valor fuese Verde, recibira este ultimo) y tambien una
variable como string la cual representará el valor por defecto a colocar
en caso de que el valor está vacío. Deberá validar que el dato no esté
vacío, en caso de estarlo lo reemplazará con el valor default pasado
por parámetro y lo retornará, caso contrario lo retornará sin
modificaciones.
"""

def normalizar_dato(valor:str,valor_defecto:str):
    if(valor==''):
        valor = valor_defecto
        return valor
    else:
        return valor

#6.3. 
"""
Crear la función 'normalizar_heroe' la cual recibirá dos parámetros. el
primero será un diccionario que representará un solo héroe, el
segundo parámetro será el nombre de la key de dicho diccionario la
cual debe ser normalizada.
La función deberá capitalizar las palabras que tenga dicha key como
valor, luego deberá normalizar el dato (ya que si viene vacío, habrá
que setearlo con N/A).
Finalmente deberá capitalizar todas las palabras del nombre del héroe
y deberá retornar al Hero con cada palabra de su nombre
capitalizados, cada palabra del valor de la key capitalizadas y
normalizadas (con N/A en caso de que estuviesen vacías por defecto).
Reutilizar: 'capitalizar_palabras' y 'normalizar_dato'  
"""
def normalizar_heroe(dicc:dict,key:str):

    if dicc[key] == '':
        dicc[key] = normalizar_dato(dicc[key],'N/A')
    else:
        dicc[key] = capitalizar_palabras(dicc[key])
        dicc['nombre'] = capitalizar_palabras(dicc['nombre'])
    
    return dicc

# 6.4
""" 
Crear la funcion 'obtener_heroes_por_tipo' el cual recibira por
parámetro:
A. La lista de héroes
B. Un set de tipos/variedades (colores de ojos, de pelo, etc)
C. El tipo de dato a evaluar (la key en cuestion, color_ojos,
color_pelo, etc)
PRESTAR ATENCIÓN:
A. Deberá iterar el set de tipos/variedades y por cada tipo tendrá evaluar
si ese tipo existe como key en un diccionario el cual deberás armar.
(contendrá cada variedad como key y una lista de nombres de héroes
como valor de cada una de ellas).
B. En caso de no existir dicha key en el diccionario, agregarla con una
lista vacía como valor.
C. Dentro de la iteración de variedades, iterar la lista de héroes (for
anidado) 'normalizando' el posible valor que tenga la key evaluada, ya
que podría venir vacía (qué función usarias aca? guiño guiño)
D. Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo
pasado por parámetro.
E. En caso de que coincida, agregarlo a la lista (inicialmente vacía) de la
variedad iterada en el primer bucle.

Esta función retornará un diccionario con cada variedad como key y
una lista de nombres como valor.
Por ejemplo:
{
"Celestes": ["Capitan America", "Tony Stark"],
"Verdes": ["Hulk", "Viuda Negra"]
....
}

"""

def obtener_heroes_por_tipo(lista:list,tipos:set,key:str):
    dicc_nuevo = {}
    
    for elementos in tipos:
      dicc_nuevo[elementos] = []
      for heroes in lista:
        heroes[key] = normalizar_dato(heroes[key],'N/A')
        if heroes[key] == elementos:
            dicc_nuevo[elementos].append(heroes['nombre'])

    return dicc_nuevo
        
    

# 6.5

""" 
Crear la funcion 'guardar_heroes_por_tipo' la cual recibira por
parámetro un diccionario que representará los distintos tipos como
clave y una lista de nombres como valor (Lo retorna la función anterior)
y además como segundo parámetro tendrá un string el cual
representará el tipo de dato a evaluar (color_pelo, color_ojos, etc).
Deberá recorrer cada key y cada valor (lista) que esta contenga para
finalmente crear un string el cual será un mensaje que deberás
imprimir formateado.
Por ejemplo:
"color_ojos Green: Black Widow | Hulk"
Reutilizar la función 'guardar_archivo'. El archivo final deberá respetar
el formato:
heroes_segun_TipoDato.csv
Donde:

● TipoDato: es la key la cual indicará qué cosas se deben guardar
en el archivo.
Ejemplo:
heroes_segun_color_pelo.csv (Agrupados por color de pelo)
heroes_segun_color_ojos.csv (Agrupados por color de ojos)
Esta función retorna True si salió todo bien, False caso contrario.
"""

def guardar_heroes_por_tipo(dicc:dict,key:str)->bool:
    string_final =""
    string_nombres = " | "
    datos = []
    for clave,valor in dicc.items():
        string_final = key +' ' + clave + ' | ' + string_nombres.join(valor)
        datos.append(string_final)
    retorno = "\n".join(datos)
    if guardar_archivo(f'heroes_segun_{key}.csv',retorno):
        return True
    else:
        return False

# 6.6
""" 
Crear la función 'stark_listar_heroes_por_dato' la cual recibirá por
parámetro la lista de héroes y un string que representará el tipo de
dato a evaluar (color_pelo, color_ojos, etc). Dentro deberás reutilizar
las funciones:
A. 'obtener_lista_de_tipos'
B. 'obtener_heroes_por_tipo'
C. 'guardar_heroes_por_tipo'
Pasando por parámetro lo que corresponda según la lógica de las
funciones usadas.
Esta función retornará True si pudo guardar el archivo, False caso
contrario.

"""
def stark_listar_heroes_por_dato(lista:list,key:str):
    tipos = obtener_lista_de_tipos(lista,key)
    heroes_x_tipo = obtener_heroes_por_tipo(lista,tipos,key)
    if guardar_heroes_por_tipo(heroes_x_tipo,key):
        return True
    else:
        return False


stark_marvel_app_5(lista_personajes)