""" Strategy Pattern - Geometry Figures
You often work with the different geometrical figures and with their parameters -
the perimeter, area, and volume.
You are tired of doing it manually, so you’ve decided to automate this process,
and therefore you need to write a particular program.
In this program you should create the class Parameters which will choose one of the few figures
(the circle, right triangle, square, right pentagon, right hexagon, cube) using the choose_figure() method
and will count the perimeter, area, and volume with the help of the following methods:

perimeter() - returns the perimeter of the figure;
area() - returns the area of the figure;
volume() - returns the volume of the figure.

Also you have to create a class for each figure and use the Strategy design pattern to solve this mission.
Every figure, except the cube, has the volume = 0.
If the result has no decimal places, you should return it as int(), in other case - round it to the 2 decimal points.

Input: Statements and expressions of the classes.
Output: The perimeter, area, and volume (number).

Hot it is used: For the geometrical object analysis.

Precondition: All data is correct.
"""
from abc import ABC, abstractmethod
from math import pi, sqrt


class Figure(ABC):
    """
    Abstract geometry figure.
    The Strategy interface declares operations common to all supported versions
    of some algorithm.
    The Parameters (Context) uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def area(self, parameter):
        """ calculate figure's area """
        pass

    @abstractmethod
    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        pass

    @abstractmethod
    def volume(self, parameter):
        """ calculate figure's volume """
        pass


class Parameters:
    """The Context defines the interface of interest to clients."""

    def __init__(self,
                 parameter: int,
                 figure: Figure = None):
        self.parameter = parameter
        self._figure = figure

    def choose_figure(self, figure: Figure) -> None:
        """ Context allows replacing a Figure (Strategy) object at runtime. """
        self._figure = figure

    def area(self):
        """ calculate figure's area """
        return self._figure.area(self.parameter)

    def perimeter(self):
        """ calculate figure's perimeter """
        return self._figure.perimeter(self.parameter)

    def volume(self):
        """ calculate figure's volume """
        return self._figure.volume(self.parameter)


"""
Concrete Figures (Strategies) implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class Circle(Figure):
    """ Circle geometry figure """

    def area(self, parameter):
        """ calculate figure's area """
        return round(pi * parameter ** 2, ndigits=2)

    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        return round(2 * pi * parameter, ndigits=2)

    def volume(self, parameter):
        """ calculate figure's volume """
        return 0


class Triangle(Figure):
    """ Equilateral Triangle geometry figure """

    def area(self, parameter):
        """ calculate figure's area """
        return round(parameter ** 2 * sqrt(3) / 4, ndigits=2)

    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        return round(3 * parameter, ndigits=2)

    def volume(self, parameter):
        """ calculate figure's volume """
        return 0


class Square(Figure):
    """ Square geometry figure """

    def area(self, parameter):
        """ calculate figure's area """
        return round(parameter ** 2, ndigits=2)

    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        return round(4 * parameter, ndigits=2)

    def volume(self, parameter):
        """ calculate figure's volume """
        return 0


class Pentagon(Figure):
    """ Regular Pentagon geometry figure """

    def area(self, parameter):
        """ calculate figure's area """
        return round(0.25 * sqrt(5 * (5 + 2 * sqrt(5))) * parameter ** 2, ndigits=2)

    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        return round(5 * parameter, ndigits=2)

    def volume(self, parameter):
        """ calculate figure's volume """
        return 0


class Hexagon(Figure):
    """ Regular Hexagon geometry figure """

    def area(self, parameter):
        """ calculate figure's area """
        return round(parameter ** 2 * 1.5 * sqrt(3), ndigits=2)

    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        return round(6 * parameter, ndigits=2)

    def volume(self, parameter):
        """" calculate figure's volume """
        return 0


class Cube(Figure):
    """ Cube geometry figure """

    def area(self, parameter):
        """ calculate figure's area """
        return round(6 * parameter ** 2, ndigits=2)

    def perimeter(self, parameter):
        """ calculate figure's perimeter """
        return round(12 * parameter, ndigits=2)

    def volume(self, parameter):
        """" calculate figure's volume """
        return round(parameter ** 3, ndigits=2)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    figure = Parameters(10)

    figure.choose_figure(Circle())
    assert figure.area() == 314.16

    figure.choose_figure(Triangle())
    assert figure.perimeter() == 30

    figure.choose_figure(Square())
    assert figure.area() == 100

    figure.choose_figure(Pentagon())
    assert figure.perimeter() == 50

    figure.choose_figure(Hexagon())
    assert figure.perimeter() == 60

    figure.choose_figure(Cube())
    assert figure.volume() == 1000

    print("Coding complete? Let's try tests!")
