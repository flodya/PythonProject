# class Human:
#     height = 170
#     satiety = 50
#
# class Student(Human):
#     satiety = 0
#     height = 220
#
#
# class Worker(Human):
#     satiety = 100
#
# nick = Student()
# ann = Worker()
# print(nick.satiety)
# print(ann.satiety)
# print(nick.height)
# print(ann.height)
#
# class Grandparent:
#     height = 170
#     satiety = 100
#     age = 60
# class Parent(Grandparent):
#     age = 40
# class Child(Parent):
#     height = 50
#     def __init__(self):
#         print(self.height)
#         print(self.satiety)
#         print(self.age)
# #
# nick = Child()
#
# class Wow:
#     __names = "qwer"
#     def __wow(self):
#         print("Wow")
#     def _hello(self):
#         print("Hello")
#     def run(self):
#         print("run")
#         print(self.__names)
# #
#
# some_obj = Wow()
# some_obj.run()
# some_obj._hello()
# some_obj._Wow__wow()
#
# class Hello_world:
#     hello = "Hello"
#     _hello = "_Hello"
#     __hello = "__Hello"
#     def __init__(self):
#         self.world = "World"
#         self._world = "_World"
#         self.__world = "__World"
#     def printer(self):
#         print(self.hello)
#         print(self._hello)
#         print(self.__hello)
#         print(self.world)
#         print(self._world)
#         print(self.__world)
#
# class Hi(Hello_world):
#     def hi_print(self):
#         print(self.hello)
#         print(self.world)
#         print(self._hello)
#         print(self._world)
#         print(self._Hello_world__hello)
#         print(self._Hello_world__world)
# hello = Hello_world()
# hello.printer()
# hi = Hi()
# hi.hi_print()
#
# class lass Hello:
#     def __init__(self):
#         print("Hello!")
#
# class Hello_World(Hello):
#     def __init__(self):
#         super().__init__()
#         print("World!")
#
# # hello = Hello()
# hello_world = Hello_World()

try:
    print("start")
    # print(start)
    print("With so much material the house cannot be built!")
except (SyntaxError,NameError) as error:
    print(error)
    print()

