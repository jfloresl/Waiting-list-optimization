import random
import pandas as pd
from names import n as names
from cirugias import c

dias=['lunes','martes','miercoles','jueves','viernes']
doc_1=[]
doc_2=[]
doctores=[]
doctores_t=[]
pab1=list()
dura1=[]
para_1=[]
para_2=[]
paramedicas=[]
paramedicas_t=[]
rut1=[]
doc1_t=[]
doc2_t=[]
para1_t=[]
para2_t=[]
intervencion=[]
intervencion_doc1=[]
intervencion_doc2=[]
intervenciones=[]
for j in dias:
    print("\n")
    df = pd.read_excel('Libro2.xlsx', sheet_name=j)
    #print(j)
    dura=df['duracion'].tolist()
    pab=df['pabellon'].tolist()
    doc1=df['cirujano-1'].tolist()
    doc2=df['cirujano-2'].tolist()
    para1=df['paramedica-1'].tolist()
    para2=df['paramedica-2'].tolist()
    rut=df['rut'].tolist()
    intervencion=df['intervencion'].tolist()


    for i in range(len(rut)):
    
        if pab[i] not in pab1:
            pab1.append(pab[i])

        if doc1[i] not in doc_1:
            doc_1.append(doc1[i])
            doc1_t.append(dura[i])
            intervencion_doc1.append(str(c.index(intervencion[i])))
        else:
            a=doc_1.index(doc1[i])
            doc1_t[a]+=dura[i]
            intervencion_doc1[a]+=" "+str(c.index(intervencion[i]))

        if doc2[i] not in doc_2:
            doc_2.append(doc2[i])
            doc2_t.append(dura[i])
            intervencion_doc2.append(str(c.index(intervencion[i])))
        else:
            a=doc_2.index(doc2[i])
            doc2_t[a]+=dura[i]
            intervencion_doc2[a]+=" "+str(c.index(intervencion[i]))

        if para1[i] not in para_1:
            para_1.append(para1[i])
            para1_t.append(dura[i])
        else:
            a=para_1.index(para1[i])
            para1_t[a]+=dura[i]

        if para2[i] not in para_2:
            para_2.append(para2[i])
            para2_t.append(dura[i])
        else:
            a=para_2.index(para2[i])
            para2_t[a]+=dura[i]
#print("sssss:",intervencion_doc1)
#print("ttttt: ",intervencion_doc2)
'''
    print("pab: ",pab1)
    print("doc1: ",doc_1)
    print("doc1_t: ",doc1_t[:len(doc_1)])
    print("doc2: ",doc_2)
    print("doc2_t: ",doc2_t[:len(doc_2)])
    print("para1: ",para_1)
    print("para1_t: ",para1_t[:len(para_1)])
    print("para2: ",para_2)
    print("para2_t: ",para2_t[:len(para_2)])
    print("\n\n")
'''
for k in range(len(doc_1)):
    doctores.append(doc_1[k])
    doctores_t.append(doc1_t[k])
    intervenciones.append(intervencion_doc1[k])
for l in range(len(doc_2)):
    if doc_2[l] not in doctores:
        doctores.append(doc_2[l])
        doctores_t.append(doc2_t[l])
        intervenciones.append(intervencion_doc2[l])
    else:
        a=doctores.index(doc_2[l])
        doctores_t[a]+=doc2_t[l]
        intervenciones[a]+=" "+str(c.index(intervencion[l]))


for m in range(len(para_1)):
    paramedicas.append(para_1[m])
    paramedicas_t.append(para1_t[m])

for n in range(len(para_2)):
    if para_2[n] not in paramedicas:
        paramedicas.append(para_2[n])
        paramedicas_t.append(para2_t[n])
    else:
        a=paramedicas.index(para_2[n])
        paramedicas_t[a]+=para2_t[n]

#print(doctores)
#print(doctores_t)
#print(paramedicas)
#print(paramedicas_t)

#print("\n\n\n")
print("ingrese cantidad de pacientes que se espera atenter")
paciente=input()

paciente_rut=[]
paciente_nombre=[]
paciente_ap_paterno=[]
paciente_ap_materno=[]
paciente_pri=[]
paciente_cirugia=[]

for i in range(1,int(paciente)+1):
    paciente_pri.append(i)

random.shuffle(paciente_pri)

for i in range(int(paciente)):
    paciente_rut.append(str(random.randint(4000000, 24000000))+"-"+str(random.randint(0,9)))
    paciente_nombre.append(names[random.randint(0,109)])
    paciente_ap_paterno.append(names[random.randint(110,218)])
    paciente_ap_materno.append(names[random.randint(219,327)])
    paciente_cirugia.append(c[random.randint(0,11)])

#print(paciente_pri)

f1 = [[0 for col in range(12)] for row in range(len(doctores))]
for i in range(len(doctores)):
    a=(intervenciones[i].split())
    res = [] 
    for k in a: 
        if k not in res: 
            res.append(k) 
    for j in range (len(res)):
        f1[i][int(res[j])]=1
#print(f1)
f = open('file.dat','w')

f.write("set Pab := \n")
for i in pab1:
    f.write(str(i))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("set J := \n") #doctores
for i in doctores:
    f.write(str(i))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')


f.write("set K := \n") #Paramedicas
for i in paramedicas:
    f.write(str(i))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("set cirugias := \n") #cirujias
for j in c:
    f.write(str(j))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')


f.write("param HDocSem := \n")
u=0
for j in doctores_t:
    f.write(str(doctores[u])+" "+str(j))
    u+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param HParSem := \n")
w=0
for j in paramedicas_t:
    f.write(str(paramedicas[w])+" "+str(j))
    w+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

u=0
f.write("param HDocMax := \n")
for j in doctores_t:
    f.write(str(doctores[u])+" "+str(45))
    u+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param HParMax := \n")
w=0
for j in paramedicas_t:
    f.write(str(paramedicas[w])+" "+str(45))
    w+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')



f.write("param f1 := \n")
t=0
for i in f1:
    for j in range(12):
        f.write(str(doctores[t])+" "+str(c[j])+" "+str(i[j])+"\n")
    t+=1

f.write(';')
f.write('\n')
f.write('\n')

f.write("set P := \n")
for j in paciente_rut:
    f.write(str(j))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param paciente_paterno := \n")
r=0
for j in paciente_ap_paterno:
    f.write(str(paciente_rut[r])+" "+str(j))
    r+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param paciente_materno := \n")
r=0
for j in paciente_ap_materno:
    f.write(str(paciente_rut[r])+" "+str(j))
    r+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param paciente_nombre := \n")
r=0
for j in paciente_nombre:
    f.write(str(paciente_rut[r])+" "+str(j))
    r+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param paciente_cirugia := \n")
r=0
for j in paciente_cirugia:
    f.write(str(paciente_rut[r])+" "+str(j))
    r+=1
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')



f.close()

