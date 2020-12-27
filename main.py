import random
import pandas as pd

dias=['lunes','martes','miercoles','jueves','viernes']
doc_1=[]
doc_2=[]
pab1=list()
dura1=list()
para_1=[]
para_2=[]
rut1=list()


for j in dias:
    print("\n")
    df = pd.read_excel('Libro2.xlsx', sheet_name=j)
    print(j)
    dura=df['duracion'].tolist()
    pab=df['pabellon'].tolist()
    doc1=df['cirujano-1'].tolist()
    doc2=df['cirujano-2'].tolist()
    para1=df['paramedica-1'].tolist()
    para2=df['paramedica-2'].tolist()
    rut=df['rut'].tolist()
    doc1_t=[0]*len(rut)
    doc2_t=[0]*len(rut)
    para1_t=[0]*len(rut)
    para2_t=[0]*len(rut)

    for i in range(len(rut)):
    
        if pab[i] not in pab1:
            pab1.append(pab[i])

        if doc1[i] not in doc_1:
            doc_1.append(doc1[i])
            doc1_t[i]+=dura[i]
        else:
            a=doc_1.index(doc1[i])
            doc1_t[i]+=dura[i]

        if doc2[i] not in doc_2:
            doc_2.append(doc2[i])
            doc2_t[i]+=dura[i]
        else:
            a=doc_2.index(doc2[i])
            doc2_t[i]+=dura[i]

        if para1[i] not in para_1:
            para_1.append(para1[i])
            para1_t[i]+=dura[i]
        else:
            a=para_1.index(para1[i])
            para1_t[i]+=dura[i]

        if para2[i] not in para_2:
            para_2.append(para2[i])
            para2_t[i]+=dura[i]
        else:
            a=para_2.index(para2[i])
            para2_t[i]+=dura[i]

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
    for k in range(len(doc_2)):
        if doc_2[k] not in doc_1:
            doc_1.append(doc_2[k])
            doc1_t.append(doc2_t[k])
'''



f = open('file.dat','w')

f.write("param Pab := \n")
for i in pab1:
    f.write(str(i))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param Doctores := \n")
for i in doc_1:
    f.write(str(i))
    f.write('\n')
for j in doc_2:
    f.write(str(j))
    f.write('\n')    
f.write(';')
f.write('\n')
f.write('\n')


f.write("param Paramedicas := \n")
for i in para_1:
    f.write(str(i))
    f.write('\n')
for j in para_2:
    f.write(str(j))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')


f.write("param HdocSem := \n")
for j in doc_1:
    f.write(str(j))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')


f.close()

