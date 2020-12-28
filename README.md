# Optimizacion de listas de espera en hospitales con Pyomo

## Requerimientos
* Python 3

pip install -r requeriments.txt

* numpy==1.19.4
* pandas==1.2.0
* python-dateutil==2.8.1
* pytz==2020.5
* six==1.15.0
* xlrd==1.2.0
* XlsxWriter==1.3.7
* Pyomo

## Modo de uso
1. Usar excel **Libro2.xlsx** para la planificacion o usar el comando **python gen.py** para crear una planificacion de prueba.

2.  Usar el comando **python main.py** y selecciona la cantidad de pacientes que se espera atender en el dia sabado(Mientas mas pacientes se eligen mas tarda la solucion del modelo)

3. Resolver el problema con el comando:

* pyomo solve modelo.py file.dat --solver=glpk

Para una solucion completa, contemplando la asignacion de paramedicas, usar el comando:

* pyomo solve modelo_paramedicas.py file.dat --solver=glpk 

4. Al final del archivo results.yml se encuentra la calendarizacion del dia sabado.
 
## Formato de la solución

### results.yml
```
Solution: 
- number of solutions: 1
  number of solutions displayed: 1
- Gap: 0.0
  Status: optimal
  Message: None
  Objective:
    OBJ:
      Value: 21
  Variable:
    t[11576690-0,Aniana,Aniko,Ashley,Asteria,1]:
      Value: 1
    t[18765718-2,Aniria,Annabel,Ascla,Aranzazu,1]:
      Value: 1
    t[19221026-9,Aniana,Aniko,April,Arabela,2]:
      Value: 1
    t[21911416-7,Aniko,Aniana,April,Arabela,2]:
      Value: 1
    t[6015320-7,Aniana,Aniko,April,Arabela,2]:
      Value: 1
    t[7877593-2,Aniko,Aniana,April,Arabela,2]:
      Value: 1
  Constraint: No values
```
### Formato de variable t
Dato  | Significado
------------- | -------------
11576690-0 | Rut del paciente
Aniana     | Nombre del doctor 1
Aniko      | Nombre del doctor 2
Ashley     | Nombre de la paramedica 1
Asteria    | Nombre de la paramedica 2
1          | Numero de pabellon
