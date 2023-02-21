from product import Product
from customer import Customer
from order import Order

if __name__ == '__main__':
    pr_1 = Product('apple', 10)
    pr_2 = Product('orange', 21)
    pr_3 = Product('banana', 23)

    customer_1 = Customer('Ivanov1', 'Ivan1')
    customer_2 = Customer('Ivanov2', 'Ivan2')
    customer_3 = Customer('Ivanov3', 'Ivan3')
    customer_4 = Customer('Ivanov4', 'Ivan4')

    order_1 = Order(customer_1)
    order_2 = Order(customer_2)
    order_3 = Order(customer_3)
    order_1.add_product(pr_1)
    order_1.add_product(pr_2)
    order_1.add_product(pr_3)
    print(order_1)
    print(" ")

    print(order_1[:2])
    print(" ")
    for product in order_1:
        print(product)
