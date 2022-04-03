def problema_1(base,altura):
    #Consigna: calcular el área de un triangulo
    area = base*altura/2
    return(area)

def problema_2(lado):
    #Consigna: Calcular el area de un cuadrado
    area = lado**2
    return (area)

def problema_3(edad):
    #Consigna: decidir si una persona es mayor de edad o no devolviendo una variable booleana
    #return(edad >=18)
    if edad >= 18:
        mayor = True
    elif edad < 18 and edad > 0:
        mayor = False
    else:
        print('Se introdujo una edad no valida')
        return()
    return(mayor)

def problema_4(r,l):
    #consigna: decidir si un circulo de radio "r" entra dentro de un cuadrado de lado "l".
    # return(2*r <= l)
    if 2*r <= l:
        entra = True
    else:
        entra = False
    return(entra)
        
