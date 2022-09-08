# Funciones

# def sumar(a,b):
#     resultado= a+b
#     return resultado

# resultado_suma = sumar(2,3)
# print(resultado_suma)
# print(sumar(2,3))

# def resta():
#     resultado = 2 - 3
#     return resultado

# print(resta())

# Funcion 3

# def saludo(nombre):
#     print("Hola",nombre)
# saludo('Valentin')

#
# nombre=input('Ingrese su nombre')
# def saludo(nombre):
#     print("Hola",nombre)
# saludo(nombre)


def saludo(cantidad_saludos):
    
# lista_nombres Es local porque le pertenece a la función. si esta var se pone por fuera
#de la funcion es global porque cualquier archivo puede acceder a esa var.
    lista_nombres=[]

    for i in range(cantidad_saludos):
        
        nombre=input('Ingrese su nombre:  ')
        
        print("Hola" + nombre)
        
        lista_nombres.append(nombre)

        print(lista_nombres)

    return lista_nombres

# nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar:   ')))

def prueba(a,b,c):
    print(a,b,c)

a=420
b=3
c=5

# prueba(b,c,a)
# el 1er parametro que le pase va a pertenecer al a y asi sucecivamente. 
# Los arg se deben pasar en el orden que se declaran.
# 
# prueba(a=a, b=b, c=c)
# De esta manera yo defino los valores de los arg sin importar el orden de como los
# declare.
# prueba(c=a,a=b,b=c)

def saludo(cantidad_saludos):
#La triple comilla funciona como documentación, no comentario. 
    
    """Esta función permite ingresar nombres, saludar a esos nombres 
    y luego generar una lista ordenada alfabeticamente con ellos."""

    lista_nombres=[]
# Bucle de ingreso de nombres.
    for i in range(cantidad_saludos):
        
        nombre=input('Ingrese su nombre:  ')
        
        print("Hola" + nombre)
        
        lista_nombres.append(nombre)

        print(lista_nombres)

    return lista_nombres

def orden(lista, sentido):

    """_summary_: ordenada alfabeticamente la lista generada en base a un sentido.

    Args:
        lista(list): lista generica
        sentido (bool): Define si ordena de mayor a menor o viceversa.
    
    Returns:
        list: lista ordenada.
    """

    lista.sort(reverse=sentido)
    
    return lista

nombres = saludo(int(input('Ingrese la cantidad de saludos a efectuar:   ')))

print(
    orden(nombres, False)
)



























