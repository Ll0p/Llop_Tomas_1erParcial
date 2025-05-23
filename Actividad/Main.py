from Actividad.Datos import valor, entrada
from Actividad.Funcion import calcular_promedio

# Invocacion a la función con los datos del modulo importado "entrada" y "valor"
retorno = calcular_promedio(entrada, valor) 

print(f'La respuesta es: "{retorno}"')