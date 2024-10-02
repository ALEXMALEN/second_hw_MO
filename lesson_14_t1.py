class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name}, last_name: {self.last_name}, age: {self.age}, gender: {self.gender}"


class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Record Book: {self.record_book}"


# власний виняток для обмеження кількості студентів
class StudentLimitExceededError(Exception):
    pass


class Group:
    MAX_STUDENTS = 10  # максимальна кількість студентів у групі

    def __init__(self, number):
        self.number = number
        self.group = []  # замінив на список для підтримки порядку

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise StudentLimitExceededError("Cannot add more than 10 students to the group.")
        self.group.append(student)
        self.group.sort(key=lambda s: (s.last_name, s.first_name))  # Сортування за прізвищем і ім'ям

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                break

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ''
        for student in self.group:
            all_students += str(student) + '\n'
        return f'Number: {self.number}\n{all_students}'



gr = Group('PD1')
try:
    # додаємо студентів до групи
    for i in range(11):  # додаємо 11 студентів
        student = Student('Male', 20 + i, f'FirstName{i}', f'LastName{i}', f'AN{100 + i}')
        gr.add_student(student)
except StudentLimitExceededError as e:
    print(e)  # виведе повідомлення про помилку якщо спробуємо додати більше 10 студентів

# кількість студентів в групі
print(gr)
