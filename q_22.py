def dot(v1, v2):
    # Inicializamos una variable para acumular la suma de los productos.
    producto_escalar_total = 0

    # Iteramos sobre los vectores v1 y v2 simultáneamente usando zip().
    # zip(v1, v2) creará pares de elementos (v1_i, v2_i) de ambas listas.
    for elemento_v1, elemento_v2 in zip(v1, v2):
        # Multiplicamos los elementos correspondientes.
        producto_elementos = elemento_v1 * elemento_v2
        # Sumamos este producto al total acumulado.
        producto_escalar_total += producto_elementos # Esto es equivalente a producto_escalar_total = producto_escalar_total + producto_elementos
        
    # Devolvemos el valor escalar final.
    return producto_escalar_total

lista_a = [1,2,3,4]
lista_b = [4,3,2,1]

print(dot(lista_a, lista_b))

print(dot(list(range(100)), list(range(10,110))))
