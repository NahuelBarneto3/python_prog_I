from data_stark import lista_personajes


'''
 {
   "nombre": "Howard the Duck",
   "identidad": "Howard (Last name unrevealed)",
   "empresa": "Marvel Comics",
   "altura": "79.349999999999994",
   "peso": "18.449999999999999",
   "genero": "M",
   "color_ojos": "Brown",
   "color_pelo": "Yellow",
   "fuerza": "2",
   "inteligencia": "average"
 },
'''
 
 #1.1) Crear la función ‘extraer_iniciales’ que recibirá como parámetro: 

def extraer_iniciales(string:str)->str:
    '''
    extrae iniciales de un nombre str

    recibe un strig como parametro

    si el string contiene "the" se omite si contiene guion pone espacio

    retorna N/A en caso de str vacio

    '''

    retorno = "N/A"

    if(len(string) > 0 ):
        if(string.count("the") > 0):
            string = string.replace("the ","")

        if(string.count("-")):
            string = string.replace("-"," ")

        lista1 = string.split(" ")

        inicial = "" #se pueden acumular strings wtf, para luego concatenarlos
        for palabra in lista1:
            inicial += palabra[0] + "."
            
        return inicial


def definir_iniciales_nombre(dic:dict)->bool:

    '''
        recibe heroe: un diccionario con los datos del personaje
        deberá agregar una nueva clave al diccionario 
        recibido como parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el 
        obtenido de llamar a la función ‘extraer_iniciales’

        valida que el tipo sea dic  
        que contenga la clave "nombre"

        En caso de encontrar algún error retornar False, caso contrario retornar True

    '''

    retorno = False

    if(type(dic) == type({})):
        iniciales = {}
        for clave in dic:
            if(clave.count("nombre") > 0):
                inicial = extraer_iniciales(dic["nombre"])
                iniciales["inicial"] = inicial

        print(iniciales)
        retorno = True
      
    return retorno



true_false = definir_iniciales_nombre(lista_personajes[0])
print(true_false)
# iniciales = extraer_iniciales("Thor")

# print(iniciales)