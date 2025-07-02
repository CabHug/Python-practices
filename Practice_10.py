import statistics as stats
import csv

monthly_sales = {}
# Leer los datos de venta desde un archivo csv
with open('Month_sales.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        #print(row)
        month = row['Month']
        sales = int(row['Sales (USD)'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

#Hallar la media
mean_sales = stats.mean(sales)
print(f"La media es: {mean_sales}")

#Hallar la mediana
median_sales = stats.median(sales)
print(f"La mediana es: {mean_sales}")

#Hallar la moda
moda_sales = stats.mode(sales)
print(f"La moda es: {mean_sales}")

#Desviacion estandar
D_estandar = stats.stdev(sales)
print(f"La desviacion estandar es: {mean_sales}")

# Varianza
Varianza = stats.variance(sales)
print(f"La varianza es: {mean_sales}")

# Maximo
maximo = max(sales)
print(f"Venta maxima es:", maximo)

#Minimo
minimo = min(sales)
print(f"Venta maxima es:", minimo)