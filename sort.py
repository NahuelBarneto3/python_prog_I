lista = [1,2,5,0,3,7,6,4]

def buscar_minimo(lista_a_buscar:list)->int:
    minimo = 0
    for i in range(len(lista_a_buscar)):
        if(lista_a_buscar[i] < lista_a_buscar[minimo]):
            minimo = i
    return minimo

def sort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar.copy() #Shallow copy*
    #lista_recibida = lista_a_ordenar[:] #Shallow copy**
    #lista_recibida =list(lista_a_ordenar) #Shallow copy***
    lista_ordenada = []

    while (len(lista_recibida) > 0):
        minimo = buscar_minimo(lista_recibida)
        lista_ordenada.append(lista_recibida.pop(minimo))
        

    return lista_ordenada

def qsort(lista_a_ordenar:list)->list:
    lista_recibida = lista_a_ordenar[:]
    lista_der = []
    lista_izq = []
    
    if(len(lista_a_ordenar) <= 1):
        return lista_a_ordenar
    else:
        pivot = lista_recibida[0]
        for elemento in lista_recibida[1:]:
            if (elemento > pivot):
                lista_der.append(elemento)
            else:
                lista_izq.append(elemento)
    lista_izq = qsort(lista_izq)
    lista_izq.append(pivot)
    lista_der = qsort(lista_der)

    return lista_izq + lista_der


lista_resultado = qsort(lista)

#print(lista)
print (lista_resultado)