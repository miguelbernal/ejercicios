# VERSION 3
# Usando substring
while True:  
    numero = input("Introduzca un número (Vacio=Salir): ")
    if numero == "":
        break
    decena = numero[-2:]
    digito_1 = decena[0:1]
    rango_1 = digito_1+"0"
    rango_2 = digito_1+"9"
    print("El mínimo es %s y el máximo %s" % (rango_1,rango_2))
    rango_3 = numero[0:-2] + rango_1
    rango_4 = numero[0:-2] + rango_2
    print("El mínimo es %s y el máximo %s" % (rango_3,rango_4))
print("Fin del programa")

# Usando calculos matematicos
while True:  
    numero = input("Introduzca un número (Vacio=Salir): ")
    if numero == "":
        break
    rango_1 = int(numero)
    rango_2 = int(numero)
    digito_ultimo = int(numero[-1:])
    
    rango_1 = rango_1 - digito_ultimo
    rango_2 = rango_2 + (9 - digito_ultimo)
    
    print("El mínimo es %s y el máximo %s" % (rango_1,rango_2))
print("Fin del programa")

# VERSION 2
# Usando substring
while True:  
    numero = str(input("Introduzca un numero (0=Salir): "))
    if numero == "0":
        break
    decena = numero[-2:]
    digito_1 = decena[0:1]
    rango_1 = digito_1+"0"
    rango_2 = digito_1+"9"
    print("El minimo es %s y el maximo %s" % (rango_1,rango_2))
    rango_3 = numero[0:-2] + rango_1
    rango_4 = numero[0:-2] + rango_2
    print("El minimo es %s y el maximo %s" % (rango_3,rango_4))
print("Fin del programa")

# Usando calculos matematicos
while True:  
    numero = str(input("Introduzca un numero (0=Salir): "))
    if numero == "0":
        break
    rango_1 = int(numero)
    rango_2 = int(numero)
    digito_ultimo = int(numero[-1:])
    
    rango_1 = rango_1 - digito_ultimo
    rango_2 = rango_2 + (9 - digito_ultimo)
    
    print("El minimo es %s y el maximo %s" % (rango_1,rango_2))
print("Fin del programa")

