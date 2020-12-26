import pandas as pd
import random
from names import n
from cirugias import c
dias=['lunes','martes','miercoles','jueves','viernes']

rut = random.randint(4000000, 24000000)
dv= random.randint(0,9)
rut_completo=str(rut)+"-"+str(dv)

datos = pd.DataFrame({'pabellon': rut,'duracion': rut_completo,'rut': rut,'nombre':rut,'ap paterno':rut,'ap materno':rut,'intervencion':c,'cirujano-1':rut,'cirujano-2':rut,'paramedica-1':rut,'paramedica-2':rut})


print(rut,"-",dv)
print(len(n[:327]))
print(len(n[328:654]))
print(len(n[655:981]))
print(len(c))

writer = pd.ExcelWriter('Libro2.xlsx', engine='xlsxwriter')

datos.to_excel(writer, sheet_name='lunes', index=0)


writer.save()