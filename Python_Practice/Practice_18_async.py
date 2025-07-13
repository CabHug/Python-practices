"""
El asincronismo ofrece varios beneficios clave:

Eficiencia: Permite manejar múltiples tareas simultáneamente sin esperar que una termine para comenzar otra, lo que reduce el tiempo de espera.

Mejor uso de recursos: Al no bloquear el flujo de ejecución, se puede utilizar más eficientemente la capacidad del servidor y la red.

Responsive: Mejora la experiencia del usuario al ofrecer respuestas más rápidas en aplicaciones interactivas.

Escalabilidad: Permite gestionar un mayor número de tareas concurrentes, lo que es esencial en aplicaciones modernas.
"""

import asyncio
# defino una funcion asincronica
async def function1(data: str, time: int):
    print(f'Procesando {data}...')
    #simular una operacion
    await asyncio.sleep(time)
    print(f'{data} procesado.')
    return 'process_'+data

async def main():
    print('Inicio del procesameinto...')
    data = [('file1.csv', 3), ('file2.csv', 30), ('file3.csv', 5)]
    tareas = [function1(d, t) for d, t in data]
    resultados = await asyncio.gather(*tareas)

    for resultado in resultados:
        print(resultado)


asyncio.run(main())