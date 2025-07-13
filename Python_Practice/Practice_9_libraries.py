import os
import math
import random

# -> Practica con libreria OS
cwd = os.getcwd()
print("Directorio actual", cwd)

#listar los archivos
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("archivos txt son:", txt_files)

# -> practica con math
radio = 5
area = math.pi * radio**2
perimetro = 2*math.pi*radio

print("Area:", area, "Perimetro:", perimetro)

#-> PRactica con random

#generar numero entero aleatorio
rand_num = random.randint(1,10)
print(rand_num)