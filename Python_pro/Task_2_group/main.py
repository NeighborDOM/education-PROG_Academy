import student
import group

x_1 = student.Student('Ivan', 'Ivanov1', 'male', '10.10.1991', 'KM156789')
x_2 = student.Student('Ivan', 'Ivanov2', 'male', '10.10.1992', 'KM156789')
x_3 = student.Student('Ivan', 'Ivanov3', 'male', '10.10.1993', 'KM156989')
x_4 = student.Student('Ivan', 'Ivanov4', 'male', '10.10.1994', 'KM146789')
x_5 = student.Student('Ivan', 'Ivanov5', 'male', '10.10.1995', 'KM158289')
x_6 = student.Student('Ivan', 'Ivanov6', 'male', '10.10.1996', 'KM158689')
x_7 = student.Student('Ivan', 'Ivanov7', 'male', '10.10.1997', 'KM153789')
x_8 = student.Student('Ivan', 'Ivanov8', 'male', '10.10.1998', 'KM156926')
x_9 = student.Student('Ivan', 'Ivanov9', 'male', '10.10.1999', 'KM156785')
x_10 = student.Student('Ivan', 'Ivanov10', 'male', '10.10.1990', 'KM156793')

y = group.Group('Python', max_students=10)
y.add_student(x_10)
y.add_student(x_1)
y.add_student(x_2)
y.add_student(x_3)
if __name__ == '__main__':
    print(y)

print(" ")
print(y[1])

group = y[:3]
for students in group:
    print(students)
print(" ")

for students in y:
    print(students)
