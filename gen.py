import pandas as pd
import random
from names import n
from cirugias import c
dias=['lunes','martes','miercoles','jueves','viernes']

print("cant de pacientes")
a=input()
#print("tipo de hospital")
#print("1. pequeño, 2. mediano, 3. grande")
#b=input


writer = pd.ExcelWriter('Libro2.xlsx', engine='xlsxwriter')

for j in dias:
    rut=list()
    pabellon=list()
    duracion=list()
    nombre=list()
    ap_paterno=list()
    ap_materno=list()
    intervencion=list()
    cirujano1=list()
    cirujano2=list()
    paramedica1=list()
    paramedica2=list()
    for i in range(int(a)):
        pabellon.append(random.randint(1,5))
        duracion.append(random.randint(1,4))
        rut.append(str(random.randint(4000000, 24000000))+"-"+str(random.randint(0,9)))
        nombre.append(n[random.randint(0,109)])
        ap_paterno.append(n[random.randint(110,218)])
        ap_materno.append(n[random.randint(219,327)])
        intervencion.append(c[random.randint(0,11)])
        cirujano1.append(n[random.randint(328,491)])
        cirujano2.append(n[random.randint(492,654)])
        paramedica1.append(n[random.randint(655,818)])
        paramedica2.append(n[random.randint(817,980)])
    
    datos = pd.DataFrame({'pabellon': pabellon,'duracion': duracion,'rut': rut,'nombre':nombre,'ap paterno':ap_paterno,'ap materno':ap_materno,'intervencion':intervencion,'cirujano-1':cirujano1,'cirujano-2':cirujano2,'paramedica-1':paramedica1,'paramedica-2':paramedica2})
    datos.to_excel(writer, sheet_name=j, index=0)

'''
print(len(n[:327])) #pacientes 0-109, 110-218, 219-327
print(len(n[328:654]))#doctores  491  (163)
print(len(n[655:981]))#paramedicas 818   (163)
print(len(c))
'''




writer.save()