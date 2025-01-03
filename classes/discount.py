class Discount:

    def __init__(self, description, discount_percent):
            self.description = description
            self.discount_percent = discount_percent
            
    @staticmethod
    def calculate_discounted_price(description, discount_percent, price):
        return price * (1 - discount_percent / 100)

    def __str__(self):
        return f"Скидка (Описание={self.description}, Значение в процентах={self.discount_percent})"