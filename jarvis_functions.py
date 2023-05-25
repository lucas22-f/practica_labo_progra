# 0 
def stark_normalizar_datos(lista: list)->None:
    """ Funcion que recibe como parametro una lista\n\n convierte los datos altura peso y fuerza en Floats y Entero. """
    # "altura": "79.349999999999994",
    # "peso": "18.449999999999999",
    # "fuierza": "2",
    if(len(lista)>0):
        i = 0
        for elementos in lista:
           
            if (type(elementos['altura'] != type(float()))):
                lista[i]['altura'] = float(elementos['altura'])
                
            if (type(elementos['peso'] != type(float()))):
                lista[i]['peso'] = float(elementos['peso'])
               
            if (type(elementos['fuerza'] != type(int()))):
                lista[i]['fuerza'] = int(elementos['fuerza']) 
            i+=1   
    else:
        print("Error: lista de heroes vacia.")

# 1.1 
def obtener_nombre(dic:dict)->str:
    """ recibe un dict: heroe \n\n retorna-> string con el nombre y un formato especifico  """
    return "nombre heroe:{}".format(dic['nombre'])

# 1.2
def imprimir_dato(string:str)->None:
    """ recibe un string : str \n\n imprime dicho string por pantalla """
    print(string)
    
# 1.3
def stark_imprimir_nombres_heroes(lista:list)-> None:
    """ recibe una lista : list \n\n itera los elementos e imprime en la variable datos lo retornado por obtener_nombre()"""
    for elementos in lista:
        datos = obtener_nombre(elementos)
        imprimir_dato(datos)

# 2
def obtener_nombre_y_dato(dic:dict,key:str)->str:
    """ recibe un dic: heroe y un str: key \n\n retorna un string con el campo de nombre + el campo de la key que llega por parametro """
    return "Nombre: {}     ||   {}: {}".format(dic['nombre'],key,dic[key])


# 3
def stark_imprimir_nombres_alturas(lista:list):
    """ recibe una lista: list validando que no este vacia\n\n itera los elementos e imprime utilizando imprimir_dato() """
    if(len(lista) > 0):
        for elementos in lista:
            imprimir_dato(obtener_nombre_y_dato(elementos,'altura'))
    else:
        return -1

# 4.1

def calcular_max(lista:list, key:str)->dict:
    """ recibe una lista: list y una key: str. \n\n guarda el primer dict de la lista luego compara buscando el maximo.\n\n 
 retorna un dict con el maximo guardado. """

    max = lista[0]
    for elementos in lista:
        if(float(elementos[key]) > float(max[key])):
            max = elementos

    return max



# 4.2
def calcular_min(lista:list, key:str)->dict:
    """ recibe una lista: list y una key: str. \n\n guarda el primer dict de la lista luego compara buscando el minimo.\n\n 
 retorna un dict con el minimo guardado.  """

    min = lista[0]

    for elementos in lista:
        if(float(elementos[key]) < float(min[key])):
            min = elementos

    return min


# 4.3
def calcular_min_max_dato(lista:list , maxmin:str , key:str)->dict:
    """ recibe una lista, la opcion que quiero buscar: 'maximo' o 'minimo'.
recibe la key de el campo que queremos comparar ej: ['altura']
 retorna un dict: con el resultado esperado. """

    if(maxmin == 'maximo'):
        maximo_minimo = calcular_max(lista,key)
    elif(maxmin == 'minimo'):
        maximo_minimo = calcular_min(lista,key)

    return maximo_minimo

# 4.4
def stark_calcular_imprimir_heroe(lista:list , maxmin:str , key:str):
    """ recibe una lista : list  , la opcion: 'maximo' o 'minimo'\n
    y una key: "str"  que indica lo que queremos buscar ej:['altura'] """
    if(len(lista) > 0):

        heroe = calcular_min_max_dato(lista,maxmin,key)
        salida = obtener_nombre_y_dato(heroe,key)

        imprimir_dato("{} {}:  {}".format(maxmin,key,salida))
    else:
        return -1
    

# 5.1
def sumar_dato_heroe(lista:list ,key:str) -> float:
    """ funcion que recibe una lista y una key y retorna la suma de los elementos de esa dicha key """
    if(key=="altura" or key =="fuerza" or key =="peso"):
        suma = 0
        for elementos in lista:
            suma += elementos[key]
        return suma
    else:
        return -1
# 5.2
def dividir(dividendo:int , divisor:int)->float:
    """ funcion que retorna la division de 1 dividendo y 1 divisor """
    if(divisor !=0 and type(dividendo) in [int,float] and type(divisor) in [int,float]):
        return dividendo/divisor
    else:
        return 0



# 5.3

def calcular_promedio(lista:list , key_a_promediar:str)->float:
    """ funcion que retorna el promedio,  recibe una lista , y la key del elemento a promediar """
    suma_alturas = sumar_dato_heroe(lista , key_a_promediar)
    promedio = dividir(suma_alturas,len(lista))

    return promedio



# 5.4
def stark_imprimir_promedio_altura(lista:list):
    """ funcion que imprime el promedio de una lista del campo especifico ['altura'] """
    if(len(lista) > 0):
        promedio = calcular_promedio(lista,'altura')
        dato = "Promedio de las alturas: {}  ".format(promedio)
        imprimir_dato(dato)
    else:
        return -1


# 6.1
def imprimir_menu():
    """ funcion que imprime el menu [texto plano] """
    imprimir_dato(" #opciones #00  \n\n ingresar a una opcion:\n1- nombres_heroes\n2- nombre_y_altura_heroe\n3- heroe_mas_alto"
                       "\n4- heroe_mas_bajo\n5- altura_promedio_heroes\n6- heroe_mas_y_menos_pesado\n0- salir \n\n")
    imprimir_dato("-------------------------------------------------------------------------------------------------------")
    imprimir_dato(" #opciones #01  \n\n ingresar a una opcion:\n7- Heroes masculinos \n8- Heroes femeninos \n9- heroe_mas_alto masculino"
                       "\n10- heroe_mas_alto femenino \n11- heroe_mas_bajo masculino \n12- heroe_mas_bajo femenino \n13- altura promedio masculino" 
                        "\n14- altura promedio femenino \n15- cantidad heroes colores de ojos\n16- cantidad heroes color de pelo"
                        "\n17- tipos de inteligencia \n18- color ojos heroes\n19- color pelo heroes \n14- heroes inteligencia\n0- salir\n\n")
# 6.2
def validar_entero(string:str)->bool:
    """ funcion que valida si la opcion que viene por parametro en este caso "string"  sea un digito o no """
    if(string.isdigit()):
        return True
    else:
        return False
    
# 6.3
def stark_menu_principal()->int:
    """ funcion que ejecuta el menu principal, pide una opcion por input y la valida si es una opcion valida retorna dicha opcion """
    imprimir_menu()
    opcion = input("ingrese una opcion\n\n")
    if(validar_entero(opcion)==True):
        return int(opcion)
    else:
        return -1
    



