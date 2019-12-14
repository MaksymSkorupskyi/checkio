"""Warriors Duel.
You need to create the class Warrior, the instances of which will have 2 parameters -
health (equal to 50 points) and
attack (equal to 5 points), and
1 property - is_alive, which can be True (if warrior's health is > 0) or False (in the other case).
In addition you have to create the second unit type - Knight,
which should be the subclass of the Warrior but have the increased attack - 7.
Also you have to create a function fight(),
which will initiate the duel between 2 warriors and define the strongest of them.
The duel occurs according to the following principle:
Every turn, the first warrior will hit the second and this second will lose his health
in the same value as the attack of the first warrior.
After that, if he is still alive, the second warrior will do the same to the first one.
The fight ends with the death of one of them.
If the first warrior is still alive (and thus the other one is not anymore),
the function should return True, False otherwise.

Input: The warriors.
Output: The result of the duel (True or False).
Precondition:
2 types of units
All given fights have an end (for all missions).
"""


class Warrior:
    """ Basic warrior unit """
    health = 50
    attack = 5

    @property
    def is_alive(self):
        """ Warrior is alive if his health is bigger than 0  """
        return self.health > 0


class Knight(Warrior):
    """ Warrior with increased attack """
    attack = 7


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
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.health -= unit_1.attack
        if not unit_2.is_alive:
            # unit_1 has won!
            return True
        unit_1.health -= unit_2.attack

    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

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

    print("Coding complete? Let's try tests!")
