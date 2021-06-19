import numpy as np

arr = np.array([
    [
        [[1, 2, 3], [4, 5, 6]], 
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2, 3], [4, 5, 6]], 
        [[1, 2, 3], [4, 5, 6]]
    ]
])
a = np.array(42)

d = np.array([
    [
        [1, 2, 3], [4, 5, 6]
    ], 
    [
        [1, 2, 3], [4, 5, 6]
    ]
])

c = np.array([
    [1, 2, 3], [4, 5, 6]
])
print(c.shape)

b = np.array([1, 2, 3, 4, 5])
print(c.sum(axis = 0))


cs = np.arange(2,11)
print(cs.sum())


print(np.multiply(2,4))

""" SELECCIONAR ELEMENTOS DE UN ARRAY """

# print(b[0])
# print("..")
# print(c[0])
# print("..")
# print(d[1])
# print("..")
# print(d[1][0][2])
# print("..")
# print(d[0][0][2])
#Cada subsista tiene 2 listas de 3 elementos


a = np.array([1,2,3])
bd = np.array([3,4,5]) 

for _ in b:
    print(_)