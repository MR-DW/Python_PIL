# Los import van arriba de todo, para mayor limpieza del codigo. y segmentarlos.
# formas de importar un modulo o funcion
# 1ra forma importar todo.
import pandas

pandas.DataFrame()

# poner un seudonimo (as pd)
import panda as pd

pd.DataFrame()

# 2da forma. cargar solo lo que necesito.

from pandas import DataFrame
DataFrame

from pandas import DataFrame as df
df()

# El entorno virtual me permite que ya esté instalado por unica vez el modulo. 
# si lo desactivo debo instalarlo nuevamnete.

# Para importar funciones desde otro archivo y poder utilizarlas.
from funciones import saludo

saludo()

from clase_3.funciones import saludo, orden
saludo()
orden()




