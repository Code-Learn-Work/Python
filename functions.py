print("Hello World")

a = str(3)
print(a)

b = int("15")
print(b)

username = input("Enter user's name : ")
print("Hello {0}".format(username))

students = []

def get_students_titlecase():
    student_titlecase = []
    for student in students:
        student_titlecase = student.title()
    return student_titlecase

def print_student_titlecase():
    student_titlecase = get_students_titlecase()
    print(student_titlecase)

def add_student(name, student_id=332):
    student = {"name" : name, "student_id" : student_id}
    students.append(name)


def var_args(name, *kwargs):
    print(name)

students_list = get_students_titlecase()

add_student(name = "Mark", student_id = 15)

var_args("Mark","Loves python", None, "Hello", True)