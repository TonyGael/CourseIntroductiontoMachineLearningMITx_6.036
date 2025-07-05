def add_two_lists(a: list, b: list) -> list:
    """
    suma dos lisas elemento a elemento:
        element-wise
    Args:
        a: la primera lista
        b: la segunda lista
    Returns:
        Una nueva lista con la suma elemento a elemento
        de las listas recibidas.
        Devuelve una lista vacía si las listas son de diferente longitud.
    """
    
    if len(a) != len(b):
        print('Las listas tienen longitudes diferentes.')
        return []
    
    resultado = []
    
    for i in range(len(a)):
        try:
            resultado.append(a[i] + b[i])
        except TypeError:
            print(f'Error: los elementos de la posición {i} no son sumables ({type(a[i])} y {type(b[i])}).')
            return []
    
    return resultado

lista_a = [1,2,3,4]
lista_b = [9,8,7,6]

print(add_two_lists(lista_a, lista_b))