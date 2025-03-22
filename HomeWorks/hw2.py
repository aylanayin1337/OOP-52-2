class Heroes:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def action(self):
        return print(f"{self.name} выполняет базовое действие")

    def attack(self):
        return print(f"{self.name} стреляет")


class Archer(Heroes):
    def __init__(self, name, hp, arrows, precision):
        super().__init__(name, hp)
        self.arrows = arrows
        self.precision = precision

    def attack(self):
        self.arrows -= 1
        if self.precision >= 50:
            return print("Атака успешна")
        else:
            return print("Атака не удалась")

    def rest(self):
        self.arrows += 5
        return print("Арсенал успешно пополнен на 5 стрел")

    def status(self):
        return print(f"Name: {self.name}, HP: {self.hp}, Arrows: {self.arrows}, Precision: {self.precision}")

archer1 = Archer("Skeleton", 100, 40, 55)
archer2 = Archer("Magic Archer", 200, 100, 90)
archer3 = Archer("Tower Archer", 150, 50, 30)

archer1.attack()
archer1.action()
archer1.rest()
archer1.status()
print("_________________________________")
archer2.attack()
archer2.action()
archer2.rest()
archer2.status()
print("_________________________________")
archer3.attack()
archer3.action()
archer3.rest()
archer3.status()