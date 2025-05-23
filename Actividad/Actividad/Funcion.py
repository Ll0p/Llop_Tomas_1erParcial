def calcular_promedio(lista: list, valor: int) -> bool:
    """ Calcula el promedio de una lista y la compara con un valor

    Argumentos:
        lista (list): Una lista con números enteros
        valor (int): Un valor a comparar con el promedio de la lista

    Retorno:
        retorno (bool): Devuelve True en caso de que el promedio sea mayor al valor y viceversa 
    """
    retorno = False
    acum = 0
    for i in range(len(lista)):
        acum += lista[i]

    promedio = acum / len(lista)
    if promedio > valor:
        retorno = True

    return retorno