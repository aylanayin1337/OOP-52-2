# class MathUtils:
#
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#
# print(MathUtils.add(1, 4))


class Person:

    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    def test(self):
        pass


p1 = Person("Alice")
p2 = Person("John")
p3 = Person("Oleg")


# print(Person.get_count())



class Person:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        first, last = value.split()
        self.first_name = first
        self.last_name = last

# p = Person("John", "Doe")
# print(p.full_name)
#
# p.full_name = "Ardager Dev"
# print(p.first_name)
# print(p.last_name)


# Пример простого декоратора

def my_decorator(func):

    def wrapper():
        print("Перед выполнением функции")
        func()
        print("После выполнения функции")

    return wrapper


@my_decorator
def hello():
    print("Привет")

# hello()

# Декоратор с аргументами

def repeat(n):

    def decorator(func):

        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)


        return wrapper

    return decorator

# amount = int(input("Введите количество"))
# @repeat(amount)
# def greet():
#     print("Привет!!!")

# greet()


# Декораторы для классов

def class_decorator(cls):

    class NewClass(cls):

        def new_method(self):
            return print("Новый метод!")

    return NewClass

@class_decorator
class MyClass:

    def old_method(self):
        return print("Старый метод!")


obj = MyClass()

obj.old_method()
obj.new_method()