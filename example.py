# Пример использования статических методов и методов класса в интернет-магазине
# Предположим, у нас есть интернет-магазин с классом Product, который представляет товар, и классом Order, который представляет заказ. 
# Мы будем использовать статические методы для расчета скидок и методы класса для подсчета общего количества заказов.
from classes.order import Order
from classes.product import Product
from classes.customer import Customer
from classes.discount import Discount
#1
# Создаем продукты
product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Tablet", 700)

# Создаем клиентов
customer1 = Customer("Romashka", [])
customer2 = Customer("Vasilek", [])
customer3 = Customer("Astra", [])
customer_list = [customer1, customer2, customer3]

# Создаем функцию для добавления заказов к клиентам 
def add_list_order(empty_list: Customer):
    while input("Введите следующий заказ (для выхода введите q):") != 'q':
        order_create = Order([])
        empty_list.orders.append(order_create)
        product_name = ""
        while product_name != 'q':
            product_name = input("Введите следующий продукт (для выхода введите q):")
            match product_name:
               case "product1":
                    empty_list.orders[-1].products.append(list())
                    empty_list.orders[-1].products[-1] = product1
               case "product2":
                    empty_list.orders[-1].products.append(product2)
               case "product3":
                    empty_list.orders[-1].products.append(product3) 
    return empty_list
#2
#Добавляем заказы к клиентам
for i in range(len(customer_list)):
    print()
    print(f"Введите заказы клиента {customer_list[i].name}:")
    add_list_order(customer_list[i])
    
for i in range(len(customer_list)):
    print(f"Клиент:{customer_list[i].name}:")
    for j in range(len(customer_list[i].orders)):
        print(f"Заказ {j+1}:")
        for k in range(len(customer_list[i].orders[j].products)):
            print(f"     Продукт {k+1}: {customer_list[i].orders[j].products[k]}")
            
# Создаем систему скидок
discount1 = Discount('сезонная скидка', 10)
discount2 = Discount('промокод', 20)

#3
# Рассчитываем цену с учетом скидки
total_sum_price = 0
total_sum_discount_price = 0
for i in range(len(customer_list)):
   print(f"Клиент:{customer_list[i].name}:")
   for j in range(len(customer_list[i].orders)):
        print(f"Заказ {j+1}:")
        for k in range(len(customer_list[i].orders[j].products)):
            match customer_list[i].name:
                case "Romashka":
                    discounted_price = Discount.calculate_discounted_price(discount1.description, discount1.discount_percent, customer_list[i].orders[j].products[k].price)
                    print(f"     Продукт {k+1}: {customer_list[i].orders[j].products[k]} Сниженная цена на {customer_list[i].orders[j].products[k].name} - {discounted_price}")
                case "Vasilek":
                    discounted_price = Discount.calculate_discounted_price(discount2.description, discount2.discount_percent, customer_list[i].orders[j].products[k].price)
                    print(f"     Продукт {k+1}: {customer_list[i].orders[j].products[k]} Сниженная цена на {customer_list[i].orders[j].products[k].name} - {discounted_price}")
                case _:
                    print(f"     Продукт {k+1}: {customer_list[i].orders[j].products[k]} Скидка не применена")
                    discounted_price = customer_list[i].orders[j].products[k].price
            total_sum_discount_price = total_sum_discount_price + discounted_price
        total_sum_price = total_sum_price + customer_list[i].orders[j].total_price()   
#4
# Выводим общее количество заказов
print(f"Всего заказов: {Order.total_orders()}")  
 
# Выводим общие суммы заказов  
print(f" Общая сумма всех заказов для всех клиентов без скидки: {total_sum_price}")
print(f" Общая сумма всех заказов для всех клиентов: {total_sum_discount_price}")

#5
# Выводим информацию о заказах
for i in range(len(customer_list)):
    print(customer_list[i])  # Вывод: Заказ (Общая цена = 1000)
    for j in range(len(customer_list[i].orders)):
        print(customer_list[i].orders[j])
        for k in range(len(customer_list[i].orders[j].products)):
            print(customer_list[i].orders[j].products[k])