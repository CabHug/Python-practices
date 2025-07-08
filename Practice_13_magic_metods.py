def add(num1, num2):
  return num1+num2
def sustract(num1, num2):
  return num1-num2
def multiply(num1, num2):
  return num1*num2
def division(num1, num2):
  if num2 == 0:
    raise ValueError("No se puede dividir por cero")
  return num1/num2

if __name__ == '__main__':
  print(add(1,2))
  print(sustract(1,2))
  print(multiply(1,2))
  print(division(1,2))