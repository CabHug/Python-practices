import numpy as np

array = np.array([1,3,5,4,2,23,56,7,8,9])

print("Cuarto elemento:",array[-7])
print("penultimo elemento:",array[8])

array2 = np.random.randint(1,20, size=(10))
print(array2[3:8])
print(array2[-5:])

array3 = np.random.randint(1,100, size=(10))
print(array)
print(array > 50)

array4 = np.array([1,2,3,4,5,6,7,8])
index= [1,4,6]
print(array4[index])

matriz = np.random.randint(10,50,size=(3,3))
print("Matriz:\n",matriz)
print("SubMatriz:\n",matriz[-2:,-2:])