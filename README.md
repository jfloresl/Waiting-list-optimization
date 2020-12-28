# Optimizacion de lista de espera en hospitales con Pyomo

pip install -r requeriments.txt

numpy==1.19.4
pandas==1.2.0
python-dateutil==2.8.1
pytz==2020.5
six==1.15.0
xlrd==1.2.0
XlsxWriter==1.3.7


1. usar excel Libro2.xlsx para la planificacion o usar el comando
python gen.py
para crear una planificacion de prueba.

2.  usar el comando
python main.py
y selecciona la cantidad de pacientes que se espera atender en el dia sabado

resolver el problema con el comando
pyomo solve grafos.py file.dat --solver=glpk
