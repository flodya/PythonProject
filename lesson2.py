class Student:
    def __init__(self, height=160):
        self.height = height
        print(self)



nick = Student()
kate = Student(height=170)
print(nick.height)
print(kate.height)

class Student:
    amount_of_students = 0
    def __init__(self, height=160):
        self.height = height
        Student.amount_of_students+=1
    def grow(self, height=1):
        self.height+=height

nick = Student()
kate = Student(height=170)
print(kate.height)
print(nick.height)
print("summer")
nick.grow(height=15)
print(kate.height)
print(nick.height)


class Student:
    def __init__(self, name=None):
        self.name = name
    def __str__(self):
        return f"I am a student. My name is {self.name}."

nick = Student(name="Nick")
ann = Student()
print(nick)
print(ann)