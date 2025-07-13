"""
El paralelismo en Python permite ejecutar múltiples tareas simultáneamente utilizando varios núcleos de procesamiento. 
A diferencia de la concurrencia, donde las tareas se dividen en fragmentos y se gestionan de manera intercalada, 
el paralelismo ejecuta las tareas al mismo tiempo en diferentes hilos o procesos. Esto es útil para tareas que requieren mucho 
tiempo de procesamiento, como cálculos intensivos. En Python, se puede implementar el paralelismo utilizando la librería multiprocessing, 
que facilita la creación de procesos independientes.
"""
import multiprocessing
import time

# funcion que calcula el cuadrado de un numero

def fucntion(n):
    time.sleep(6)
    return n*n


if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    # crearmos un pool de procesos,esto seran los que ejecuten en paralelo
    with multiprocessing.Pool() as pool:
        result = pool.map(fucntion, numbers)
    
    print(result)