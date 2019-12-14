"""Army Battles
In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen.
Great job! But let's move to something that feels a little more epic - the armies!
In this mission your task is to add new classes and functions to the existing ones.

The new class should be the Army and have the method add_units() -
for adding the chosen amount of units to the army.
The first unit added will be the first to go to fight, the second will be the second, ...

Also you need to create a Battle() class with a fight() function, which will determine the strongest army.
The battles occur according to the following principles:
at first, there is a duel between the first warrior of the first army and the first warrior of the second army.
As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel,
and the surviving warrior continues to fight with his current health.
This continues until all the soldiers of one of the armies die.
In this case, the battle() function should return True, if the first army won,
or False, if the second one was stronger.
Note that army 1 have the advantage to start every fight!

Input: The warriors and armies.
Output: The result of the battle (True or False).

Precondition:
2 types of units
For all battles, each army is obviously not empty at the beginning.
"""

from typing import List, Type


class Warrior:
    """ Basic warrior unit """
    health = 50
    attack = 5

    @property
    def is_alive(self) -> bool:
        """ Warrior is alive if his health is bigger than 0 """
        return self.health > 0


class Knight(Warrior):
    """ Warrior with increased attack """
    attack = 7


class Army:
    """ Army of warriors """

    def __init__(self):
        self.units: List[Warrior] = []

    def add_units(self,
                  unit: Type[Warrior],
                  quantity: int):
        """ Add the chosen amount of units to the army """
        for i in range(quantity):
            self.units.append(unit())

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
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            # unit_1 has won!
            return True
        unit_1.health -= unit_2.attack

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) is True
    assert fight(dave, carl) is False
    assert chuck.is_alive is True
    assert bruce.is_alive is False
    assert carl.is_alive is True
    assert dave.is_alive is False
    assert fight(carl, mark) is False
    assert carl.is_alive is False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Warrior, 20)
    army_2.add_units(Warrior, 21)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) is True
    assert battle.fight(army_3, army_4) is False
    assert battle.fight(army_1, army_2) is True
    print("Coding complete? Let's try tests!")
