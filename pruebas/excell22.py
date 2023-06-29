import pandas as pd
from openpyxl import Workbook
wb=Workbook()
archivo="D:\\2021\INFORME_DEL_22.xlsx"
dicc = {}

def activarHoja(name):
    activa = pd.read_excel(archivo,sheet_name=name)
    carga = wb.
    return activa

def guardarHoja(name, guardar):
    actual=activarHoja(name)
    print(dicc)
    a



need=activarHoja("mes")
for contenido in need.values:
    if contenido[1] == 221:
        desc=contenido[2]
        salida=contenido[3]
        entrada=contenido[4]
        dicc[desc]=entrada
        guardarHoja("nueva",dicc)
