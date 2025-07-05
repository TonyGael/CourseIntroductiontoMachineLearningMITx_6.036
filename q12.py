import numpy as np

# T superíndice= ᵀ

# Q12 resolviendo equivalentes (ab)ᵀ

a = np.array([
    [1],
    [5],
    [0]
])

b = np.array([
    [8],
    [2]
])

aT = a.T
bT = b.T
ab = a @ b

print(aT)
print(bT)
print(ab)