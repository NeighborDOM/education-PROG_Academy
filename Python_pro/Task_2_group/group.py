# 3) Створіть клас Група, який містить масив із 10 об'єктів класу Студент.
# Реалізуйте методи додавання, видалення студента та метод пошуку студента за прізвищем.
# Визначте для Групи метод str() для повернення списку студентів у вигляді рядка.
import student
import input_err
import group_iterator

class Group:

    def __init__(self, title, max_students=10):
        self.student = student.Student
        self.max_students = max_students
        self.title = title
        self.__students = []

    def add_student(self, student):
        if len(self.__students) >= self.max_students:
            raise input_err.InputError('The limit of students in the group has been exceeded')
        if student in self.__students:
            raise input_err.InputError('This student has already been added')
        self.__students.append(student)

    def remove_student(self, student):
        if student in self.__students:
            self.__students.remove(student)

    def search(self, surname):
        res = []
        for item in self.__students:
            if item.surname == surname:
                res.append(item)
        return res

    def __str__(self):
        return f'{self.title}\n\t' + '\n\t'.join(map(str, self.__students))

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index < len(self.__students):
                return self.__students[index]
            else:
                raise IndexError()

        if isinstance(index, slice):
            start = 0 if index.start == None else index.start
            stop = len(self.__students) if index.stop == None else index.stop
            step = 1 if index.step == None else index.step
            temp_students = []
            if start < 0 and stop >= len(self.__students):
                raise IndexError()
            for i in range(start, stop, step):
                temp_students.append(self.__students[i])
            return temp_students

        raise TypeError()

    def __len__(self):
        return len(self.__students)

    def __iter__(self):
        return group_iterator.GroupIterator(self.__students)