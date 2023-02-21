# 1. Створіть клас для опису товару.
# У якості атрибутів товару можете використовувати значення ціни товару, опису товару, габарити товару.
# Створіть пару екземплярів вашого класу та протестуйте їхню роботу.
class Product:

    def __init__(self, title: str, price: float | int):
        """

        :param title:
        :param price:
        """
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price}'
