"""concurrente: se crea diferentes hilos los cuales ejecutan una seccion de la tarea
luego continuan con otra porcion en otro hilo asi hasta terminar la accion
La concurrencia permite procesar varias tareas dividiendo cada una en fragmentos que se ejecutan de manera intercalada. 
En Python, esto se implementa utilizando hilos, donde cada hilo puede pausar su ejecución y permitir que otros hilos realicen su trabajo. 
Así, mientras un hilo está esperando, otro puede estar ejecutándose, lo que mejora la eficiencia en comparación con la ejecución secuencial. 
Esta técnica es especialmente útil para tareas que involucran entrada y salida de datos, donde el tiempo de espera puede ser significativo."""

import threading
import time

#funcion que simula el procesameinto de una solicitud
def process_request(request_id):
    print(f'Procesando solicitud {request_id}')
    time.sleep(6)
    print(f'Procesamiento completo! {request_id}')

# lista de los hilos que se van creando, a qui se van a ir guardando cuando terminen
threads = []

for i in range(3):
    #crear un nuveo hilo
    thread = threading.Thread(target=process_request, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    #el metodo join() permite esperar a que cada hilo termine su ejecucion asegurandome que todos termian 
    thread.join()

print(threads)