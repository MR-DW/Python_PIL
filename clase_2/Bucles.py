# dos tipos de bucles. Su diferencia es la cantidad de veces que se ejecuta
# For. Yo debo indicarle cuantas veces se va a ejecutar/ iterar.
# in para indicar en donde queremos que itere.
# En un string va a tomar el valor de cada posición del string y la va a imprimir a todas por el print. 
# Hasta que el string se termine.
# el incrementador i++ se ejecuta automaticamente, no hay que ponerlo.
# for i in "Python":
#     print(i)
# lista = [True, False, 1,2,3,4, "Hola"]
# for i in lista:
#     print(i)
# lista=[]
# for i in range(0,10, 2):
#     print(i)
# la función range nos permite crear un rango desde el num que le pasamos 
# como 1er arg hasta el segundo num como arg sin incluirlo. El 3er num de arg es el step, 
# que va a contar de cuanto en cuanto queiro que vaya el conteo.
# Si coloco solo un arg va a contar hasta llegar a ese mismo.
# De esta manera el for va a iterar todo el largo del rango.
# lista=[]
# for i in range(10):
#      lista.append(i)
# print(lista)     
# .append() este metodo permite guardar los valores que se iteran en la lista, declarada.
# lista=[]
# for i in range(3):
#     numero_usuario = int(input("Ingrese un numero: "))
#     lista.append(i)
# print(lista)
# for i in range(3):
    # Ingreso de datos
    # dato_ingreso = input('Ingrese un numero: ')

    # Validación
    # if dato_ingreso.isnumeric():
        # Si el dato que ingreso es numerico 
    #     lista.append(int(dato_ingreso))
    # else:
    #     print("El dato ingresado no es un numero")
    #     break
        #el break corta con la iteración. 
# print(lista)
# Los for se pueden anidar pero gasta mas recursos.


# While. Se ejecuta eternamente hasta que yo lo pare. Enunciado Mientras que la var tenga tal valor, ejecutar.
# No colocar true porque si no nunca para.
# x=10
# while x > 0:
#     print(x)
# Me daría un bucle infinito porque no hago nada para que x decrmente y llegue a ser 0.
# Se debe crear condición para que rompa la iteración.
# x=10
# while x > 0:
#     print(x)
#     x-=1
# x-=1 es la condición para que decremente y x inicial llegue a 0.


















