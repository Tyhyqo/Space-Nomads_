from random import randint
import pygame

difficult = 50


class Ship:
    def __init__(self, sprite, coords, hull, armor, equipment):
        self.sprite = sprite
        self.coords = coords  # list
        self.hull = hull
        self.armor = armor
        self.mass = hull
        self.equipment = equipment  # list of classes
        self.hold = list()
        self.space = hull


    def fly(self, coords, speed):
        pass

    def shoot(self):
        pass

    def death(self):
        pass

    def get_hull(self):
        return self.hull

    def get_damage(self, dmg):
        self.hull -= dmg + self.armor

    def overmass(self):
        return 'Ваш корабль не может поднять столько груза!'


class WarriorShip(Ship):
    def __init__(self, sprite, coords, hull, armor, equipment):
        super().__init__(sprite, coords, hull, armor, equipment)
        self.slot_equipment = [(1, 1),  # engine and fuel tank
                               (1, 1, 1, 1, randint(0, 1)),  # guns
                               (randint(0, 1), 1),  # grab and shield
                               (1, randint(0, 1)),  # locator and scanner
                               randint(0, 1)]  # afterburner
        self.armor += 2

        # equipment setting up
        for i in self.equipment:
            if not self.slot_equipment[i.get_type()[0]][i.get_type()[1]]:
                self.equipment.remove(i)
                self.hold.append(i)
                self.mass += i.get_mass()
                self.space -= i.get_mass()


class PirateShip(Ship):
    def __init__(self, sprite, coords, hull, armor, equipment):
        super().__init__(sprite, coords, hull, armor, equipment)
        self.slot_equipment = [(1, 1),  # engine and fuel tank
                               (1, 1, 1, randint(0, 1), 0),  # guns
                               (1, randint(0, 1)),  # grab and shield
                               (1, 1),  # locator and scanner
                               1]  # afterburner
        self.mass *= 0.75
        self.hull *= 0.8

        # equipment setting up
        for i in self.equipment:
            if not self.slot_equipment[i.get_type()[0]][i.get_type()[1]]:
                self.equipment.remove(i)
                self.hold.append(i)
                self.mass += i.get_mass()
                self.space -= i.get_mass()


class CargoShip(Ship):
    def __init__(self, sprite, coords, hull, armor, equipment):
        super().__init__(sprite, coords, hull, armor, equipment)
        self.slot_equipment = [(1, 1),  # engine and fuel tank
                               (1, randint(0, 1), 0, 0, 0),  # guns
                               (randint(0, 1), 0),  # grab and shield
                               (1, 0),  # locator and scanner
                               0]  # afterburner
        self.hull *= 1.5

        # equipment setting up
        for i in self.equipment:
            if not self.slot_equipment[i.get_type()[0]][i.get_type()[1]]:
                self.equipment.remove(i)
                self.hold.append(i)
                self.mass += i.get_mass()
                self.space -= i.get_mass()


class NomadShip(Ship):
    def __init__(self, sprite, coords, hull, armor, equipment):
        super().__init__(sprite, coords, hull, armor, equipment)
        self.slot_equipment = [(1, 1),  # engine and fuel tank
                               (1, 1, randint(0, 1), 0, 0),  # guns
                               (1, randint(0, 1)),  # grab and shield
                               (1, randint(0, 1)),  # locator and scanner
                               randint(0, 1)]  # afterburner
        self.hull *= 0.9

        # equipment setting up
        for i in self.equipment:
            if not self.slot_equipment[i.get_type()[0]][i.get_type()[1]]:
                self.equipment.remove(i)
                self.hold.append(i)
                self.mass += i.get_mass()
                self.space -= i.get_mass()


class Kristalid(Ship):
    def __init__(self, sprite, coords, hull, armor, equipment):
        super().__init__(sprite, coords, hull, armor, equipment)
        self.slot_equipment = [(1, 1),  # engine and fuel tank
                               (1, 1, 1, 1, 1),  # guns
                               (1, 1),  # grab and shield
                               (1, 1),  # locator and scanner
                               1]  # afterburner
        self.hull *= difficult
        self.armor += round(difficult / 100)

        # equipment setting up
        for i in self.equipment:
            self.equipment.remove(i)
            self.hold.append(i)
            self.mass += i.get_mass()
            self.space -= i.get_mass()