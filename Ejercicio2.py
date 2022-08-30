acumulador_kilos = 0
acumulador_precio_total = 0
flag = 0 
precio_alimento_caro = 0
contador_prods = 0

while(True):
    while(True):
        peso_prod = input("ingrese el peso(entre 10 y 100 kilos)")
        peso_prod = int(peso_prod)
        if(peso_prod < 10 or peso_prod > 100):continue
        else: break
        
    while(True):
        precio_kilo = input("ingrese el precio por kilo")
        precio_kilo = int(precio_kilo)
        if(precio_kilo < 0): continue
        else: break

    while(True):
        tipo_prod = input("ingrese el tipo de producto ('v' para vegetal, 'a', para animal y 'm', para mezcla)")
        if(tipo_prod != "v" and tipo_prod != "a" and tipo_prod != "m"): continue
        else: break
    
    acumulador_kilos += peso_prod
    acumulador_precio_total += precio_kilo


    if(flag == 0 or precio_alimento_caro > precio_kilo):
        precio_alimento_caro = precio_kilo
        tipo_alimento_caro = tipo_prod
        flag = 1 

    
    respuesta = input("Quiere seguir ingresando productos?")
    if(respuesta != "no"): continue
    else: break

if(acumulador_kilos > 100):
    descuento = 0.15
elif(acumulador_kilos > 300):
    descuento = 0.25
else: 
    descuento = 1 

precio_con_descuento = acumulador_precio_total + (acumulador_precio_total * descuento)
precio_promedio_kilo = acumulador_precio_total / acumulador_kilos

print("el importe a pagar bruto es: " + str(acumulador_precio_total) + "$")
if(descuento != 1):
    print("el importe total con descuento es: " + str(precio_con_descuento))

print("el promedio de precio por kilo es: " + str(precio_promedio_kilo) + "$")