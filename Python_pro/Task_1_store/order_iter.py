class OrderIterator:

    def __init__(self, __products):
        self.__products = __products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.__products):
            raise StopIteration()
        temp_products = self.__products[self.index]
        self.index+=1
        return temp_products