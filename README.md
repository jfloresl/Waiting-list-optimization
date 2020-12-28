# Optimizacion de lista de espera en hospitales con Pyomo

## Requerimientos
pip install -r requeriments.txt

numpy==1.19.4
pandas==1.2.0
python-dateutil==2.8.1
pytz==2020.5
six==1.15.0
xlrd==1.2.0
XlsxWriter==1.3.7

## Modo de uso
1. Usar excel Libro2.xlsx para la planificacion o usar el comando 'python gen.py' para crear una planificacion de prueba.

2.  Usar el comando 'python main.py' y selecciona la cantidad de pacientes que se espera atender en el dia sabado(Mientas mas pacientes se eligen mas tarda la solucion del modelo)

3. Resolver el problema con el comando:

'pyomo solve modelo.py file.dat --solver=glpk'

Para una solucion completa, contemplando la asignacion de paramedicas, usar el comando:

'pyomo solve modelo_paramedicas.py file.dat --solver=glpk'

4. Al final del archivo results.yml se encuentra la calendarizacion del dia sabado.
 
## Formato de la solucion

t[11576690-0,Aniana,Aniko,Ashley,Asteria,1]:

11576690-0  rut del paciente
Aniana      nombre del doctor 1
Aniko       nombre del doctor 2
Ashley      nombre de la paramedica 1
Asteria     nombre de la paramedica 2
1           numero de pabellon
