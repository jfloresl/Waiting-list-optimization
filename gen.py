import pandas as pd
import random
from names import n
from cirugias import c
dias=['lunes','martes','miercoles','jueves','viernes']

rut = random.randint(4000000, 24000000)
dv= random.randint(0,9)
rut_completo=str(rut)+"-"+str(dv)
datos = pd.DataFrame({'pabellon': [11, 12, 13, 14],'duracion': rut_completo,'rut': [31, 32, 33, 34]})

'''nombre
ap_paterno
ap_materno
intervencion
cirujano1
cirujano2
paramedica1
paramedica2
'''
print(rut,"-",dv)
print(len(n[:327]))
print(len(n[328:654]))
print(len(n[655:981]))
print(len(c))
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

datos.to_excel(writer, sheet_name='lunes', index=0)


writer.save()