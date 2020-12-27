import pandas as pd
import random
from names import n
from cirugias import c
dias=['lunes','martes','miercoles','jueves','viernes']


print("tipo de hospital")
print("1. pequeño, 2. mediano, 3. grande")
b=input()
if b=='1':
    pacientes_a=3
    pacientes_b=19
    pab_a=1
    pab_b=4
    cirujano1_a=328
    cirujano1_b=333
    cirujano2_a=492
    cirujano2_b=497
    paramedica1_a=655
    paramedica1_b=660
    paramedica2_a=817
    paramedica2_b=822
elif b=='2':
    pacientes_a=20
    pacientes_b=35
    pab_a=1
    pab_b=9
    cirujano1_a=328
    cirujano1_b=336
    cirujano2_a=492
    cirujano2_b=500
    paramedica1_a=655
    paramedica1_b=663
    paramedica2_a=817
    paramedica2_b=825

elif b=='3':
    pacientes_a=36
    pacientes_b=50
    pab_a=1
    pab_b=14
    cirujano1_a=328
    cirujano1_b=338
    cirujano2_a=492
    cirujano2_b=502
    paramedica1_a=655
    paramedica1_b=668
    paramedica2_a=817
    paramedica2_b=830
writer = pd.ExcelWriter('Libro2.xlsx', engine='xlsxwriter')
duraciones=[1,2,3,4]
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
    for i in range(random.randint(pacientes_a,pacientes_b)):
        pabellon.append(random.randint(pab_a,pab_b))
        duracion.append(random.choices(duraciones, weights=(50, 25, 15, 10), k=1)[0])
        rut.append(str(random.randint(4000000, 24000000))+"-"+str(random.randint(0,9)))
        nombre.append(n[random.randint(0,109)])
        ap_paterno.append(n[random.randint(110,218)])
        ap_materno.append(n[random.randint(219,327)])
        intervencion.append(c[random.randint(0,11)])
        cirujano1.append(n[random.randint(cirujano1_a,cirujano1_b)])
        cirujano2.append(n[random.randint(cirujano2_a,cirujano2_b)])
        paramedica1.append(n[random.randint(paramedica1_a,paramedica1_b)])
        paramedica2.append(n[random.randint(paramedica2_a,paramedica2_b)])
    
    datos = pd.DataFrame({'pabellon': pabellon,'duracion': duracion,'rut': rut,'nombre':nombre,'ap paterno':ap_paterno,'ap materno':ap_materno,'intervencion':intervencion,'cirujano-1':cirujano1,'cirujano-2':cirujano2,'paramedica-1':paramedica1,'paramedica-2':paramedica2})
    datos.to_excel(writer, sheet_name=j, index=0)

'''
print(len(n[:327])) #pacientes 0-109, 110-218, 219-327
print(len(n[328:654]))#doctores  491  (163)
print(len(n[655:981]))#paramedicas 818   (163)
print(len(c))
'''




writer.save()