import random

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

