# 1. Створіть клас, що описує людину (створіть метод, що виводить інформацію про людину).


class Human:
    def __init__(self, name, surname):
        """
        :param name:
        :param surname:
        """
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'name = {self.name}, surname = {self.surname}'
