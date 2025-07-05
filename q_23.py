def add_n(n):
    def add_val_to_vector(v):
        return [elemento + n for elemento in v]
         
    return add_val_to_vector

sumar_cinco = add_n(5)
vector = [10, 20, 30]
resultado = sumar_cinco(vector)
print(f'La suma de {vector} más 5 es: {resultado}')
