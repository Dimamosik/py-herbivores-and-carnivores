class Animal:
    alive = []
    def __init__(self, name,  health = 100):
        self.health = health
        self.name = name
        self.hidden = False

        if self.health > 0:
            Animal.alive.append(self)

    def take_damage(self, damage):
        if self.health <= 0:
            return "already dead"

        self.health -= damage

        if self.health <= 0:
            self.health = 0
            self.die()
        return None

    def die (self):
        if self in Animal.alive:
            Animal.alive.remove(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

class Herbivore(Animal):
    def hide(self):
        if self.health > 0:
            self.hidden = not self.hidden

class Carnivore(Animal):
    def bite(self, other):
        if self.health <= 0:
            return

        if isinstance(other, Carnivore):
            return

        if other.hidden:
            return

        if other.health > 0:
            other.take_damage(50)
