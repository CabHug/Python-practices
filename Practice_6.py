with open('Tale.txt','r') as file:
    for lines in file:
        #El metodo strip me permite eliminar caracteres no deseados a inicio o filas de una cadena de texto
        print(lines.strip())