class Customer:
    #default_orders = []

    #def __init__(self, name, orders):
     #   if orders:
     #       self.orders = orders
     #   else:
     #       self.orders = Customer.default_orders
     #   self.name = name

  def __init__(self, name, orders):
      self.orders = orders
      self.name = name

  def __str__(self):
      return f"Клиент (Название={self.name}, Заказы={self.orders})"