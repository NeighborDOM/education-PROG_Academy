# 2. Створіть клас "Покупець".
# У якості атрибутів можна використовувати прізвище, ім'я, по батькові, мобільний телефон тощо.

class Customer:

    def __init__(self, surname: str, name: str):
        """

        :param surname:
        :param name:
        """
        self.surname = surname
        self.name = name

    def __str__(self):
        return f'{self.surname} {self.name[0]}.'
