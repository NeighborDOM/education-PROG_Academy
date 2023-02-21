# 2) На його основі створіть клас Студент (перевизначте метод виведення інформації).
from human import Human


class Student(Human):
    def __init__(self, name, surname, sex, date_of_birth, passport):
        """
        :param name:
        :param surname:
        :param sex:
        :param date_of_birth:
        :param passport:
        """
        super().__init__(name, surname)
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.passport = passport

    def __str__(self):
        return super().__str__() + " " + f'sex = {self.sex}, ' \
                                         f'date_of_birth = {self.date_of_birth}, passport = {self.passport}'


x_1 = Student('Ivan', 'Ivanov1', 'male', '10.10.1991', 'KM156789')

if __name__ == '__main__':
    print(x_1)
