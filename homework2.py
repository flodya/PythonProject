import random

class Forest:
    def __init__(self, name):
        self.name = name
        self.food_sources = 100

    def provide_food(self):
        if self.food_sources >= 10:
            self.food_sources -= 10
            print(f"Ліс '{self.name}' дав їжу тварині залишилось їжі: {self.food_sources}")
            return 10
        else:
            print(f"У лісі '{self.name}' закінчується їжа.")
            return 0

class Animal:
    def __init__(self, name, forest):
        self.name = name
        self.energy = 50
        self.hunger = 50
        self.forest = forest

    def eat(self):
        food = self.forest.provide_food()
        if food > 0:
            self.hunger -= food
            print(f"{self.name} поїв: {self.hunger}")
        else:
            self.hunger += 10
            print(f"{self.name}  Голод збільшився до: {self.hunger}")

    def rest(self):
        self.energy += 10
        print(f"{self.name} відпочинок Енергія: {self.energy}")

    def explore(self):
        self.energy -= 15
        self.hunger += 5
        print(f"{self.name} досліджує ліс. сила: {self.energy}, Голод: {self.hunger}")

    def live_day(self, day):
        print(f"\n=== День {day} для {self.name} ===")
        action = random.choice(["eat", "rest", "explore"])
        if action == "eat":
            self.eat()
        elif action == "rest":
            self.rest()
        elif action == "explore":
            self.explore()

        if self.hunger >= 100:
            print(f"{self.name} помер від голоду.")
            return False
        if self.energy <= 0:
            print(f"{self.name} не може рухатись")
            return False
        return True



forest = Forest(" ліс")
wolf = Animal("Вовк", forest)

for day in range(1, 11):
    if not wolf.live_day(day):
        break
