
class Animal:
    def action(self):
        return print("Some action")


class Flyable(Animal):
    def action(self):
        super().action()
        # return print("Fly")


class Swimmable(Animal):
    def action(self):
        super().action()
        # return print("Swim")


class Duck(Swimmable, Flyable): # change classes to change line 24 output
    def make_sound(self):
        return print("Quack")


donald_duck = Duck()

# donald_duck.action() # Line 17, first class used in subclass
# donald_duck.make_sound()

# print(Duck.mro()) # Порядок наследования (MRO - Method Resolution Order)


"""Big O Notation"""

# O(1) Константная сложность

def get_element(list, index):
    return list[index]

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_element(list1, 3))


# O(n) Линейная сложность

def find_element(lst, target):
    for i in lst:
        if i == target:
            return i

print(find_element(list1, 4))


#O(log n) Логарифмическая сложность

def binary_search(lst, target):
    left, right = 0, len(lst)-1

    while left <= right:
        middle = (left + right) // 2
        if lst[middle] == target:
            return middle
        elif lst[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


print(binary_search(list1, 6))


# O (n^2) Квадратичная сложность
"""Bubble Sort"""
def bubble_sort(lst):
    n = len(lst)

    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


list2 = [9, 2, 5, 66, 11, 77, 334, 12, 99, 221, 33, 99, 12, 33, 455]
bubble_sort(list2)
print(list2)

"""Стандартная сортировка"""
list2.sort()
print(list2)

