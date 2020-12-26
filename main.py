import random
import pandas as pd

xls = pd.ExcelFile('Libro1.xls')
dias=['lunes','martes','miercoles','jueves','viernes']
doc_1=[]
doc_2=list()
pab1=list()
dura1=list()
para_1=list()
para_2=list()
rut1=list()

for i in dias:
    print("\n")

    print(i)
    df = pd.read_excel(xls, i)
    dura=df['duracion'].tolist()
    pab=df['pabellon'].tolist()
    doc1=df['cirujano-1'].tolist()
    doc2=df['cirujano-2'].tolist()
    para1=df['paramedica-1'].tolist()
    para2=df['paramedica-2'].tolist()
    rut=df['rut'].tolist()
    doc1_t=[0]*len(rut)

    for i in range(len(rut)):
    
        if pab[i] not in pab1:
            pab1.append(pab[i])

        if doc1[i] not in doc_1:
            doc_1.append(doc1[i])
            doc1_t[i]+=dura[i]
        else:
            a=doc_1.index(doc1[i])
            doc1_t[a]+=dura[i]


    #print("cantida de operaciones:",len(rut1))
    print("pab: ",pab1)
    print("doc1: ",doc_1)
    print("doc1_t: ",doc1_t[:len(doc_1)])
   # print(df)

    print("\n\n")


f = open('file.dat','w')

f.write("param Pab := \n")
for i in pab1:
    f.write(str(i))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param Doc1 := \n")
for j in doc_1:
    f.write(str(j))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')

f.write("param Doc2 := \n")
for j in doc_2:
    f.write(str(j))
    f.write('\n')
f.write(';')
f.write('\n')
f.write('\n')


f.close()

