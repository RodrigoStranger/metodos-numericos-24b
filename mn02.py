import math

vector_resultados = []
vector_error_iterativo = []

contador = 1
cifras_significativas = 4  #modificables
tolerancia_porcentual = 0.5 * math.pow(10, 2 - cifras_significativas)
exponente = 0.7  #modificables

while True:
    if contador == 1:
        vector_resultados.append(1)
        vector_error_iterativo.append(0)  
        contador += 1
    elif contador == 2:
        aproximacion_anterior = vector_resultados[-1]
        aproximacion_actual = aproximacion_anterior + exponente
        vector_resultados.append(aproximacion_actual)
        error_iterativo = ((aproximacion_actual - aproximacion_anterior) / aproximacion_actual) * 100
        vector_error_iterativo.append(error_iterativo)
        if abs(error_iterativo) < tolerancia_porcentual:
            break
        contador += 1
    else:
        aproximacion_anterior = vector_resultados[-1]
        termino = (math.pow(exponente, contador - 1)) / math.factorial(contador - 1)
        aproximacion_actual = aproximacion_anterior + termino
        vector_resultados.append(aproximacion_actual)
        error_iterativo = ((aproximacion_actual - aproximacion_anterior) / aproximacion_actual) * 100
        vector_error_iterativo.append(error_iterativo)
        if abs(error_iterativo) < tolerancia_porcentual:
            break
        contador += 1

print(" ")
print("                  Error iterativo ")
print("          Error aproximado iterativo porcentual")
print(f"{'Terminos de Taylor':<20}{'Resultados':<20}{'Error Iterativo (%)':<20}")
for i in range(len(vector_resultados)):
    print(f"{i + 1:<20}{vector_resultados[i]:<20.10f}{vector_error_iterativo[i]:<20.10f}")

print(" ")

epsilon = math.e

valor_verdadero = math.pow(epsilon,exponente)
valor_aproximado = vector_resultados[-1]
error_verdadero = (valor_verdadero - valor_aproximado)



error_verdadero_relativo = (error_verdadero / valor_verdadero) 
error_verdadero_relativo_porcentual = error_verdadero_relativo * 100

print(f"Valor verdadero: {valor_verdadero:.10f}")
print(f"Valor aproximado: {valor_aproximado:.10f}")
print(f"Error verdadero: {error_verdadero:.10f}")

error_verdadero_relativo = error_verdadero / valor_verdadero
error_verdadero_relativo_porcentual = error_verdadero_relativo * 100

print(f"Error verdadero relativo: {error_verdadero_relativo:.10f}")
print(f"Error verdadero relativo porcentual: {error_verdadero_relativo_porcentual:.10f}")
