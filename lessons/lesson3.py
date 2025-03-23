# Инкапсуляция и полиморфизм
# def some(self): - Открытый метод
# def _some(self): - Закрытый метод
# def __some(self): - Приватный метод

# self.some = Открытый атрибут
# self._some = Закрытый атрибут
# self.__some = Приватный атрибут

class BankAccount:

    def __init__(self, username, balance, pin_code):
        self.username = username
        self._balance = balance
        self.__pin_code = pin_code

    def deposit(self, amount):
        if amount > 0:
            self.__to_up_balance(amount)
            return print(f"Баланс {self.username} пополнен на {amount}. \n Текущий баланс: {self._balance}")
        else:
            return print("Сумма должна быть положительной")

    def __to_up_balance(self, amount):
        self._balance += amount

    def get_balance(self, pin_code):
        if self.__pin_code == pin_code:
            return print(f"Ваш баланс: {self._balance}")
        else:
            return print("Неверный пин-код")

user1 = BankAccount("Ardager", 1000, 1234)

# print(user1._balance)
# print(user1._BankAccount__pin_code)
# print(dir(user1))
#
# user1.get_balance(1234)
# user1.deposit(100)

# print(user1._balance)
# print(user1.__pin_code)



# Абстракция

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass #Определенный интерфейс для звука

    @abstractmethod
    def move(self):
        pass #Определенный интерфейс для движения


class Dog(Animal):

    def make_sound(self):
        return print("Gav Gav")

    def move(self):
        return print("Moving")

goofie = Dog()

# goofie.make_sound()
# goofie.move()


class SmsServiceAbc(ABC):

    @abstractmethod
    def send_sms(self):
        pass

import sqlite3
import datetime
import json

from datetime import datetime, date, time, timezone

from sqlite3 import connect

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')




