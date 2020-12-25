import random
import pandas as pd

xls = pd.ExcelFile('Libro1.xls')
dias=['lunes','martes','miercoles','jueves','viernes']

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
    doc_1=list()
    doc_2=list()
    pab1=list()
    dura1=list()
    para_1=list()
    para_2=list()
    rut1=list()
    for i in pab:
        if i not in pab1:
            pab1.append(i)

    for j in dura:
        if j not in dura1:
            dura1.append(j)

    for k in doc1:
        if k not in doc_1:
            doc_1.append(k)

    for l in doc2:
        if l not in doc_2:
            doc_2.append(l)

    for o in para1:
        if o not in para_1:
            para_1.append(o)

    for p in para2:
        if p not in para_2:
            para_2.append(p)

    for q in rut:
        if q not in rut1:
            rut1.append(q)

    print("cantida de operaciones:",len(rut1))
    print("pab",pab1)
    print("dura",dura1)
    print("doc1",doc_1)
    print("doc2",doc_2)
    print("para1",para_1)
    print("para2",para_2)
    print("pacientes",rut1)
    print("\n\n")



f = open('file.dat','w')
f.write("param Dura := \n")
print("numero de pacientes")
a=input()
for i in range(int(a)):
    num1 = random.randint(1, 5)
    print("Random integer: ", num1)
    f.write(str(num1))
    f.write('\n')
f.write(';')
f.close()

