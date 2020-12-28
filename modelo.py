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

model.HDocSem = Param(model.J, within=NonNegativeIntegers) #horas que trabajo cada doctor en la semana
model.HDocMax = Param(model.J,within=NonNegativeIntegers) # maximas horas de trabajo semanales para doctor
model.HParSem = Param(model.K,within=NonNegativeIntegers) #horas que trabajo cada paramedica por semana
model.HParMax = Param(model.K,within=NonNegativeIntegers) #maximas horas de trabajo semanales para paramed

model.Jornada = Param(within=NonNegativeIntegers, initialize = 8) #duracion en horas de la jornada el dia sabado
model.Dura = Param(model.P,within=NonNegativeIntegers) # duracion de las intervenciones de los pacientes en minutos
model.Pri = Param(model.P,within=NonNegativeIntegers) # prioridades de los pacientes

model.paciente_cirugia = Param(model.P,within=Any) # operacion de los pacientes
model.paciente_nombre = Param(model.P,within=Any) #nombre del paciente
model.paciente_paterno = Param(model.P,within=Any) #apellido paterno del paciente
model.paciente_materno = Param(model.P,within=Any) #apellido materno del paciente



model.f1 = Param(model.J, model.cirugias, domain=Boolean) # si el medico j puede realizar la operacion "cirugias"

def coin_init(model, doc1, doc2):
  if doc1 == doc2:
    return 0
  else:
    return 1

model.Coin = Param(model.J, model.J, initialize=coin_init, domain=Boolean)

print("asdf")


model.t = Var(model.P, model.J, model.J,model.K,model.K, model.PAB, domain=Boolean)


def obj_expression(model):
    return sum(model.t[p,doc1,doc2,para1,para2,pab] * model.Pri[p] for p in model.P for doc1 in model.J for doc2 in model.J for para1 in model.K for para2 in model.K for pab in model.PAB)

model.OBJ = Objective(rule = obj_expression,sense=maximize)

'''   ejemplo de restriccion
def ax_constraint_rule(model, i):
    # return the expression for the constraint for i
    return sum(model.a[i,j] * model.x[j] for j in model.J) >= model.b[i]

# the next line creates one constraint for each member of the set model.I
model.AxbConstraint = Constraint(model.I, rule=ax_constraint_rule)
'''
#El doctor primario no puede ser el mismo que el secundario.
def coin_rule(model,p,doc1,doc2,para1,para2):
  return (None, sum(model.Coin[doc1,doc2] * model.t[p,doc1,doc2,para1,para2,PAB] for PAB in model.PAB), 0)

model.restCoincidencia = Constraint(model.P, model.J, model.J,model.K,model.K, rule=coin_rule)

#Las operaciones realizadas durante el d ́ıa no pueden durar m ́as de X hora en total (8 horas en total)
def max_jornada(model):
  return (None, sum(model.t[p,doc1,doc2,para1,para2,pab] * model.Dura[p] for p in model.P for doc1 in model.J for doc2 in model.J for para1 in model.K for para2 in model.K for pab in model.PAB), model.Jornada)

model.restJornada = Constraint(rule=max_jornada)

#un paciente no puede ser operado mas de una vez el dia sabado
def operacion_unica(model, p):
  return (None, sum(model.t[p,doc1,doc2,para1,para2,pab] for doc1 in model.J for doc2 in model.J for para1 in model.K for para2 in model.K for pab in model.PAB) , 1)

model.restOperacionUnica = Constraint(model.P, rule=operacion_unica)

#Un m ́edico no puedo trabajar m ́as de las horas permitidas. (suma sus horas como doctor principal y como secundario)
def max_horas_medico(model, doctor):
  return (None, sum(model.t[p,doctor,doc2,pab] * model.Dura[p] for p in model.P for doc2 in model.J  for pab in model.PAB) + \
  sum(model.t[p,doc1,doctor,pab] * model.Dura[p] for p in model.P for doc1 in model.J for pab in model.PAB) , model.HDocMax[doctor] - model.HDocSem[doctor])

#model.restMaxHorasMedico = Constraint(model.J, rule=max_horas_medico)

#Un m ́edico no puedo trabajar m ́as de las horas permitidas.

#Cada médico debe ser especialista en el área de la operación a realizar
def medicos_especialistas(model,p,doc1):
    return (None, sum(model.t[p,doc1,doc2,para1,para2,pab] for p in model.P for doc1 in model.J for doc2 in model.J for para1 in model.K for para2 in model.K for pab in model.PAB), model.f1[doc1, value(model.paciente_cirugia[p])])

#model.restEspecialista = Constraint(model.P, model.J, rule=medicos_especialistas)

#####################

instancia = model.create_instance("file.dat")

#opt = SolverFactory("glpk")

#resultados = opt.solve(instancia,tee=True, timelimit=None)


opt = SolverFactory("cplex")

solver_manager = SolverManagerFactory('neos')

resultados = solver_manager.solve(instancia, opt=opt)


#instancia.print()  
#instancia.display()
print(resultados)
