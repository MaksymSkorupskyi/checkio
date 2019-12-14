"""The Vampires
So we have 3 types of units: the Warrior, Knight and Defender.
Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional vampirism parameter,
which helps him to heal himself.
When the Vampire hits the other unit, he restores his health by +50% of the dealt damage
(enemy defense makes the dealt damage value lower).
The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%
You should store vampirism attribute as an integer (50 for 50%).
It will be needed to make this solution evolutes to fit one of the next challenges of this saga.

Input: The warriors and armies.
Output: The result of the battle (True or False).
Precondition: 4 types of units
"""
