"""3 Chefs
You are the owner of a cafe where 3 chefs work: a JapaneseCook, RussianCook and ItalianCook.
Each of them can prepare the national food and beverage:
- JapaneseCook: Sushi and Tea;
- RussianCook: Dumplings and Compote;
- ItalianCook: Pizza and Juice.
Your task is to create 3 different subclasses (one for each chef)
which are the children of an AbstractCook and have these methods:
- add_food(food_amount, food_price), which add to the client's order the value of the food which he had chosen;
- add_drink(drink_amount, drink_price), which add to the client's order the value of the drink which he had chosen;
- total(), which returns a string like: 'Foods: 150, Drinks: 50, Total: 200',
and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used.
Every client can choose only one chef.
In this mission the Abstract Factory design pattern could help.

Example:

client_1 = JapaneseCook()
client_1.add_food(2, 20)
client_1.add_drink(5, 4)
client_1.total() == "Sushi: 40, Tea: 20, Total: 60"

client_2 = RussianCook()
client_2.add_food(1, 40)
client_2.add_drink(5, 20)
client_2.total() == "Dumplings: 40, Compote: 100, Total: 140"

client_3 = ItalianCook()
client_3.add_food(2, 20)
client_3.add_drink(2, 10)
client_3.total() == "Pizza: 40, Juice: 20, Total: 60"

All data here will be correct and you don't need to implement the value checking.

Input: Statements and expressions of the 3 chefs’ classes.
Output: The behaviour as described.

How it is used: Work with classes and object-oriented programming is considered to be on a much higher skill level
which you should reach in order to put Python to full use.

Precondition: All data is correct.
"""
from abc import ABC, abstractmethod


class AbstractCook(ABC):
    """ Abstract Cook Base Classes """

    def __init__(self,
                 food_amount: int = 0,
                 food_price: int = 0,
                 drink_amount: int = 0,
                 drink_price: int = 0):
        self.food = food_amount * food_price
        self.drink = drink_amount * drink_price

    def add_food(self,
                 food_amount: int,
                 food_price: int):
        """ add to the client's order the value of the food which he had chosen """
        self.food += food_amount * food_price

    def add_drink(self,
                  drink_amount: int,
                  drink_price: int):
        """ add to the client's order the value of the drink which he had chosen """
        self.drink += drink_amount * drink_price

    @abstractmethod
    def total(self):
        """
        Returns a string like: 'Foods: 150, Drinks: 50, Total: 200',
        and for the each chef instead of the Foods and Drinks will be the national food and drink that he’s used.
        """
        return f'Foods: {self.food}, Drinks: {self.drink}, Total: {self.food + self.drink}'


class JapaneseCook(AbstractCook):
    """ prepare the national food and beverage: Sushi and Tea """

    def total(self):
        return f'Sushi: {self.food}, Tea: {self.drink}, Total: {self.food + self.drink}'


class RussianCook(AbstractCook):
    """ prepare the national food and beverage: Dumplings and Compote """

    def total(self):
        return f'Dumplings: {self.food}, Compote: {self.drink}, Total: {self.food + self.drink}'


class ItalianCook(AbstractCook):
    """ prepare the national food and beverage: Pizza and Juice """

    def total(self):
        return f'Pizza: {self.food}, Juice: {self.drink}, Total: {self.food + self.drink}'


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    client_1 = JapaneseCook()
    client_1.add_food(2, 30)
    client_1.add_food(3, 15)
    client_1.add_drink(2, 10)

    client_2 = RussianCook()
    client_2.add_food(1, 40)
    client_2.add_food(2, 25)
    client_2.add_drink(5, 20)

    client_3 = ItalianCook()
    client_3.add_food(2, 20)
    client_3.add_food(2, 30)
    client_3.add_drink(2, 10)

    print('client_1.total():', client_1.total())
    print('client_2.total():', client_2.total())
    print('client_3.total():', client_3.total())

    assert client_1.total() == "Sushi: 105, Tea: 20, Total: 125"
    assert client_2.total() == "Dumplings: 90, Compote: 100, Total: 190"
    assert client_3.total() == "Pizza: 100, Juice: 20, Total: 120"
    print("Coding complete? Let's try tests!")
