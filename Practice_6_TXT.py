#Leeer un archivo linea por linea
""""
with open('Tale.txt','r') as file:
    for lines in file:
        #El metodo strip me permite eliminar caracteres no deseados a inicio o filas de una cadena de texto
        print(lines.strip())
"""

# leer una archivo en una lista
"""
with open('Tale.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
"""

#Leer un txt y modificar una linea en espesifico
with open('Tale.txt', 'r') as file:
    lines = file.readlines()

#Cantidad de lineas
print("Lines number:", len(lines))
#modifico la linea dos del texto
lines[1] = "Hi I'm Hugo, updated from python"

with open('Tale.txt', 'w') as file:
    file.writelines(lines)

with open('Tale.txt','r') as file:
    for lines in file:
        #El metodo strip me permite eliminar caracteres no deseados a inicio o filas de una cadena de texto
        print(lines.strip())
