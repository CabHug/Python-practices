class BackAccount:
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance
    self.status = True

  def deposit(self, amount):
    if self.status:
      self.balance += amount
      print(f"Deposito exitoso! balance actial {self.balance}")
    else:
      print("Cuenta desactivada")

  def retirar(self, amount):
    if self.status:
      if self.blanance >= amount:
        self.balance -= amount
        print(f"Retiro exitoso! balance actual {self.balance}")
      else:
        print(f"Balance actual {self.balance} insuficiente")

    else:
      print("Cuenta inactiva")

  def accountStatus(self):
    if self.status:
      print("Cuenta actva")
    else:
      print("Cuetna incativa")

  def setStatus(self):
    print(f"""
    estado actual de su cuenta {"Activa" if self.status else "Inactiva"}
    Desea cambiar su estado?
    1. Si
    2. No
    3. Salir
    """)
    while True:
      try:
        choice = int(input("Ingrese su opcion: "))
        if choice == 1:
          self.status = not self.status
          print(f"Nuevo estatus: {"Activa" if self.status else "Inactiva"}")
      except ValueError:
        print("Opçion invalida, ingrese un numero")