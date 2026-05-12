
ESTUDIANTES = {
             "123":"Sofia Castillo",
             "456":"David Rodriguez",
             "789":"Jose Martinez",
             "101":"Santiago Nuñez",
             "112":"Martina Saniago"
             }

ASIGNATURAS=[
             "logica computacional",
             "introduccion a la igenieria",
             "calculo diferencial",
             "algebra lineal"
             ]
def buscar_estudiante(documento):
    return ESTUDIANES.get(documento, None)

def validar_nota(valor):
    try:
        nota = float(valor) 
        return 0 <=nota<=5
    except ValueError:
        return False
    
def validar_asistencia(valor):
    try:
        asistencia = float(valor) 
        return 0 <=asistencia<=100
    except ValueError:
        return False
def calcular_estado(nota,asistencia):
    promedio= sum(nota) / len(asistencia)

    if asistencia < 80:
        return promedio, "Reprobo por inasistencia","red"
    elif promedio>=3.0:
        return promedio, "Aprobado", "green"
    else:
        return promedio, "Reproboo por nota","red"
    
  

        
