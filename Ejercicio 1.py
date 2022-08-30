flag = 0 
barbijo_mas_caro = 0
unidades_barbijo_mas_caro = 0
item_mas_unidades = 0
cant_jabon = 0

for i in range(1):
    while (True):
        tipo_prod = input("Ingrese tipo de prod(barbijo, jabon o alcohol)")
        if (tipo_prod != "barbijo" and tipo_prod != "jabon" and tipo_prod != "alc\ohol"): continue
        else: break

    while (True):
        precio = input("Ingrese precio(entre 100 y 300)")
        precio = int(precio)

        if (precio < 100 or precio > 300): continue
        else: break

    while (True):
        cant_unidades = input("Ingrese cantidad de unidades(entre 0 y 1000)")
        cant_unidades = int(cant_unidades)
        if (cant_unidades < 0 or cant_unidades > 1000): continue
        else: break

    marca = input("ingrese en marca")
    fabricante = input("ingrese fabricante")
    
    
    if (flag == 0 or barbijo_mas_caro < precio):
        barbijo_mas_caro = precio
        unidades_barbijo_mas_caro = cant_unidades
        fabricante_caro = fabricante
    
    if (flag == 0 or item_mas_unidades < cant_unidades):
        item_mas_unidades = cant_unidades
        fabricante_mas_unidades = fabricante
        tipo_mas_unidades = tipo_prod
        flag = 0
    
    if(tipo_prod == "jabon"):
        cant_jabon += 1


print("El barbijo mas caro lo fabrico " + fabricante_caro + 
" y la cantidad de unidades que se compraron fueron: " + str(unidades_barbijo_mas_caro))
print("El item con mas unidades fue : " + tipo_mas_unidades + " y el fabricante fue: "+ fabricante_mas_unidades)
print("hay " + str(cant_jabon) + " unidades de jabon")