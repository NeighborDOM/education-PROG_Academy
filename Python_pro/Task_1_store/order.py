# 3. Створіть клас "Замовлення".
# Замовлення може містити декілька товарів певної кількості.
# Замовлення має містити дані про користувача, який його здійснив.
# Реалізуйте метод обчислення сумарної вартості замовлення.
# Визначте метод str() для коректного виведення інформації про це замовлення.
from product import Product
from customer import Customer
import input_err
import order_iter

class Order:

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def add_product(self, product: Product, quantity=1):
        self.__products.append(product)
        self.__quantities.append(quantity)

    def total(self):
        summa = 0
        for index, product in enumerate(self.__products):
            summa += product.price * self.__quantities[index]

        if summa < 0:
            raise input_err.InputError('The price cannot be negative')

        return summa

    def __str__(self):
        res = ''
        for product, quantity in zip(self.__products, self.__quantities):
            res += f'{product} x {quantity} = {product.price * quantity} грн.\n'
        return f'{self.customer}\n' \
               f'{res}\n' \
               f'Total={self.total()} грн.'

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < len(self.__products):
                return self.__products[index]
            else:
                raise IndexError()

        if isinstance(index, slice):
            start = 0 if index.start == None else index.start
            stop = len(self.__products) if index.stop == None else index.stop
            step = 1 if index.step == None else index.step
            temp_students = []
            if start < 0 and stop >= len(self.__products):
                raise IndexError()
            for i in range(start, stop, step):
                temp_students.append(self.__products[i])
            return temp_students

        raise TypeError()

    def __len__(self):
        return len(self.__products)

    def __iter__(self):
        return order_iter.OrderIterator(self.__products)