import pandas as pd
import random
from names import n
from cirugias import c
# Create some Pandas dataframes from some data.
dias=['lunes','martes','miercoles','jueves','viernes']

datos = pd.DataFrame({'pabellon': [11, 12, 13, 14],'duracion': [21, 22, 23, 24],'rut': [31, 32, 33, 34]})
rut = random.randint(4000000, 24000000)
dv= random.randint(0,9)

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
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_multiple.xlsx', engine='xlsxwriter')

# Write each dataframe to a different worksheet.
datos.to_excel(writer, sheet_name='lunes', index=0)


# Close the Pandas Excel writer and output the Excel file.
writer.save()