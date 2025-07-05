import numpy as np

# T superíndice= ᵀ

# Q11 dados w = [1 5 0]ᵀ y x = [8 2]ᵀ, cuál es el resultado de wxᵀ?

w = np.array([
    [1],
    [5],
    [0]
])

x = np.array([
    [8],
    [2]
])

xT = x.T

print(f'Vector columna w: \n{w}')

print('-_'*10)
print(f'Vector columna x: \n{x}')

print('-_'*10)
print(f'Transpuesta de x: \n{xT}')

print('-_'*10)
res_producto = w @ xT
print(f'Resultado del producto w xᵀ: \n{res_producto}')
print(f'Forma (shape) del producto w xᵀ: \n{res_producto.shape}')

# Para obtener el resultado como una lista de listas 
print('-_'*10)
res_lis_listas = res_producto.tolist()
print(f'Resultado como lista de lisas en Python: \n{res_lis_listas}')

print('FinQ11'*5)

