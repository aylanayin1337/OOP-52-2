class Hero:
    def __init__(self, name, lvl, HP):
        self.name = name
        self.lvl = lvl
        self.HP = HP
    def is_adult(self):
       if self.lvl >= 10:
           return True
       else:
           return False
    def introduce(self):
        return print(f"Привет меня зовут {self.name}. Мой уровень: {self.lvl}. Мое HP: {self.HP}")


hero1 = Hero("Spider Man", 10, 500)
hero1.introduce()
print(hero1.is_adult())

hero2 = Hero("Iron Man", 8, 400)
hero2.introduce()
print(hero2.is_adult())

hero3 = Hero("Black Widow", 11, 450)
hero3.introduce()
print(hero3.is_adult())