"""The Defenders
In the previous mission - Army battles, you've learned how to make a battle between 2 armies.
But we have only 2 types of units - the Warriors and Knights.
Let's add another one - the Defender.
It should be the subclass of the Warrior class and have an additional defense parameter,
which helps him to survive longer. When another unit hits the defender,
he loses a certain amount of his health according to the next formula:
enemy attack - self defense (if enemy attack > self defense).
Otherwise, the defender doesn't lose his health.

The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

Input: The warriors and armies.
Output: The result of the battle (True or False)."""

from typing import List, Type


class Warrior:
    """ Basic warrior unit """
    health = 50
    attack = 5

    @property
    def is_alive(self) -> bool:
        """ Warrior is alive if his health is bigger than 0 """
        return self.health > 0

    def get_damage(self, damage):
        """ Get damage from enemy's attack """
        self.health -= damage


class Knight(Warrior):
    """ Warrior with increased attack """
    attack = 7


class Defender(Warrior):
    """
    Warrior with defense which helps him to survive longer.
    When another unit hits the defender,
    he loses a certain amount of his health according to the next formula:
    enemy attack - self defense (if enemy attack > self defense).
    Otherwise, the defender doesn't lose his health.
    """
    health = 60
    attack = 3
    defense = 2

    def get_damage(self, damage):
        """ Get damage from enemy's attack considering defense """
        if damage > self.defense:
            self.health -= damage - self.defense


class Army:
    """ Army of warriors """

    def __init__(self):
        self.units: List[Warrior] = []

    def add_units(self,
                  unit: Type[Warrior],
                  quantity: int):
        """ Add the chosen amount of units to the army """
        self.units.extend(unit() for _ in range(quantity))

    def remove_one_unit(self):
        """ Remove dead unit from the Army """
        if self.units:
            self.units.pop(0)


class Battle:
    """ Battle between two armies """

    @staticmethod
    def fight(first_army: Army,
              second_army: Army) -> bool:
        """
        Determine the strongest army.
        Return True, if the first army won, or False, if the second one was stronger.
        """
        while first_army.units:
            if fight(first_army.units[0], second_army.units[0]):
                second_army.remove_one_unit()
            else:
                first_army.remove_one_unit()
            if not second_army.units:
                return True
        return False


def fight(unit_1: Warrior,
          unit_2: Warrior) -> bool:
    """
    Initiate the duel between 2 warriors and define the strongest of them.
    Every turn, the first warrior will hit the second and this second will lose his health
    in the same value as the attack of the first warrior.
    After that, if he is still alive, the second warrior will do the same to the first one.
    The fight ends with the death of one of them.
    If the first warrior is still alive (and thus the other one is not anymore),
    the function should return True, False otherwise.
    """
    while unit_1.is_alive:
        unit_2.get_damage(unit_1.attack)
        if not unit_2.is_alive:
            # unit_1 has won!
            return True
        unit_1.get_damage(unit_2.attack)

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False
    assert fight(bob, mike) is False
    assert fight(lancelot, rog) is True

    # battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is False
    assert battle.fight(army_3, army_4) is True
    print("Coding complete? Let's try tests!")
