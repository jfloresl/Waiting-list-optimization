from pyomo.environ import *

model = AbstractModel()

#model.p = Param(within=NonNegativeIntegers) #cant de pacientes
#model.j = Param(within=NonNegativeIntegers) #cant de doctores
#model.k = Param(within=NonNegativeIntegers) #cant de paramedicas
#model.pab = Param(within=NonNegativeIntegers) #cantidad pabellones

model.P = Set() #lista de ruts pacientes (usado como indice)
model.J = Set() #lista de nombres doctores (usado como indice)
model.K = Set() #lista de nombres de paramedicas (usado como indice)
model.PAB = Set() #lista de nombres de pabellones (usado como indice)
model.cirugias = Set() #lista de operaciones

model.HDocSem = Param(model.J) #horas que trabajo cada doctor en la semana 
model.HDocMax = Param(model.J) # maximas horas de trabajo semanales para doctor
model.HParSem = Param(model.K) #horas que trabajo cada paramedica por semana
model.HParMax = Param(model.K) #maximas horas de trabajo semanales para paramed

model.Jornada = Param(NonNegativeIntegers, initialize = 8) #duracion en horas de la jornada el dia sabado
model.Dura = Param(model.P) # duracion de las intervenciones de los pacientes en minutos
model.Pri = Param(model.P) # prioridades de los pacientes

model.paciente_cirugia = Param(model.P) # operacion de los pacientes
model.paciente_nombre = Param(model.P) #nombre del paciente
model.paciente_paterno = Param(model.P) #apellido paterno del paciente
model.paciente_materno = Param(model.P) #apellido materno del paciente

model.doc1= RangeSet(1,model.J) #doctor primario
model.doc2= RangeSet(1,model.J) #doctor secundario


model.f1 = Param(model.J, model.cirugias, domain=Boolean) # si el medico j puede realizar la operacion "cirugias"

def coin_init(model, doc1, doc2):
  if doc1 == doc2:
    return 1
  else:
    return 0

model.Coin = Param(model.doc1, model.doc2, initialize=coin_init, domain=Boolean)

model.t = Var(model.P,model.doc1,model.doc2,model.PAB, domain=Boolean)


def obj_expression(model):
    return sum(model.t[p,doc1,doc2,pab] * model.Pri[p] for p in model.P for doc1 in model.J for doc2 in model.J for pab in model.PAB)

model.OBJ = Objective(rule=obj_expression,sense=maximize)

print("end")

"""#RESTRICCIONES

"""
#El doctor primario no puede ser el mismo que el secundario.
def coin_rule(model,p,doc1,doc2):
  return sum(model.Coin[doc1,doc2] * model.t[p,doc1,doc2, PAB] for PAB in model.PAB) <= 0

model.restCoincidencia = Constraint(model.P,  model.J, model.J, rule=coin_rule)

#Las operaciones realizadas durante el d ́ıa no pueden durar m ́as de X hora en total (8 horas en total) 
def max_jornada(model):
  return sum(model.t[p,doc1,doc2,pab] * model.Dura[p] for p in model.P for doc1 in model.J for doc2 in model.J for pab in model.PAB) <= model.Jornada * 60

model.restJornada = Constraint(rule=max_jornada)

#un paciente no puede ser operado mas de una vez el dia sabado
def operacion_unica(model, p):
  return sum(model.t[p,doc1,doc2,pab] for doc1 in model.J for doc2 in model.J for pab in model.PAB) <= 1

model.restOperacionUnica = Constraint(model.P, rule=operacion_unica)

#Un m ́edico no puedo trabajar m ́as de las horas permitidas. (suma sus horas como doctor principal y como secundario)
def max_horas_medico(model, doctor):
  return sum(model.t[p,doctor,doc2,pab] * model.Dura[p] for p in model.P for doc2 in model.J for pab in model.PAB) + \
  sum(model.t[p,doc1,doctor,pab] * model.Dura[p] for p in model.P for doc1 in model.J for pab in model.PAB) <= model.HDocMax[doctor] - model.HDocSem[doctor]

model.restMaxHorasMedico = Constraint(model.J, rule=max_horas_medico)

#Un m ́edico no puedo trabajar m ́as de las horas permitidas. 

#Cada médico debe ser especialista en el área de la operación a realizar
def medicos_especialistas(model,p,doc1):
    return sum(model.t[p,doc1,doc2,pab] for p in model.P for doc1 in model.J for doc2 in model.J for pab in model.PAB) <= model.f1[doc1, value(model.paciente_cirugia[p])]

model.restEspecialista = Constraint(model.P, model.J, rule=medicos_especialistas)


print("end")

"""##datos

#EJECUTAR MODELO
"""

#pyomo solve modelo.py file.dat --solver=glpk