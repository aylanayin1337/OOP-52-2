# Наследование


# Родительский/Супер/Базовый класс
class Hero:

    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp


    def intoduce(self):
        return print(f"Я {self.name}, мой уровень {self.lvl}")

    def action(self):
        return print(f"{self.name} выполняет базовое действие")


# warrior = Hero("Kirito", 100, 1000)

# Дочерний класс
class WarriorHero(Hero):

    def __init__(self, name, lvl, hp, st):
        super().__init__(name, lvl, hp)
        self.st = st

    def attack(self):
        if self.st >= 10:
            self.st -= 1
            return print(f"{self.name} атакует мечом!")
        else:
            return print(f"{self.name} мало стамины")

    # Полиморфизм
    def intoduce(self):
        return print(f"Name: {self.name}, ST: {self.st}")


class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp



kirito_hero = WarriorHero("Kirito", 100, 1000, 10)
gandalf_hero = MageHero("Gandalf", 100, 1000, 10)


gandalf_hero.intoduce()
gandalf_hero.action()


kirito_hero.action()
kirito_hero.intoduce()
kirito_hero.attack()