from math import pi
from abc import ABCMeta, abstractmethod, ABC
#
#
# class Shape(metaclass=ABCMeta):  # liczu pole, zrób koło trójkąt
#
#     @abstractmethod
#     def area(self):
#         raise NotImplementedError
#
#
# class Circle(Shape):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return pi * self.radius ** 2
#
#
# if __name__ == '__main__':
#     circle = Circle(1)
#     assert circle.area() == pi
#
# circle2 = Circle(4)
#
# print(circle2.area())


#==========================================================
# Strategia wzorca "BUDOWNICZY"

# from abc import ABCMeta, abstractmethod
#
#
# class Car:
#
#     def __init__(self, wheels=4, seats=4, color="Black"): # najlepiej dąc jakieś wartości domyślne
#         self.wheels = wheels
#         self.seats = seats
#         self.color = color
#
#     def __str__(self):
#         return f"This is a {self.color} car with " \
#             f"{self.wheels} wheels and {self.seats} seats."
#
#
# class Builder(metaclass=ABCMeta):                         # to dajemy klasę abstrakcyjną, jeżeli wszystkie metody są
#                                                                # abstrakcyjne nazywamy ja interfjesem
#     @abstractmethod
#     def set_wheels(self, value):
#         pass
#
#     @abstractmethod
#     def set_seats(self, value):
#         pass
#
#     @abstractmethod
#     def set_color(self, value):
#         pass
#
#     @abstractmethod
#     def get_result(self):
#         pass
#
#
# class CarBuilder(Builder):                            # Tu dajemny klasę "Buildera"
#
#     def __init__(self):
#         self.car = Car()
#
#     def set_wheels(self, value):
#         self.car.wheels = value
#         return self
#
#     def set_seats(self, value):
#         self.car.seats = value
#         return self
#
#     def set_color(self, value):
#         self.car.color = value
#         return self
#
#     def get_result(self):
#         return self.car
#
#
# class CarBuilderDirector:
#
#     @staticmethod
#     def construct():
#         builder = CarBuilder()
#         model = builder.set_wheels(8).set_seats(4).set_color("Red")
#         return model.get_result()
#
#
# def main():
#     car = CarBuilderDirector.construct()
#     print(car)
#
#
# if __name__ == '__main__':
#     main()

# ============================================================

# Budynek ma :
# ilość doors
# ilość scian
# ilosc pięter
# okien
# roof

# from abc import ABCMeta, abstractmethod
#
#
# class Budynek:
#     def __init__(self, doors=3, walls=4, okna=8, floors=50, roof="Krzywy"):
#         self.doors = doors
#         self.walls = walls
#         self.okna = okna
#         self.floors = floors
#         self.roof = roof
#
#     def __str__(self):
#         return f"Ten budynek ma {self.doors} doors, {self.walls} ściany i {self.okna} okien. " \
#                f"Budynek ma{self.floors} pięter, Budynek posiada roof typu: {self.roof}"
#
#
# class Builder(metaclass=ABCMeta):
#
#     @abstractmethod
#     def set_doors(self, value):
#         pass
#
#     @abstractmethod
#     def set_walls(self, value):
#         pass
#
#     @abstractmethod
#     def set_okna(self, value):
#         pass
#
#     @abstractmethod
#     def set_floors(self, value):
#         pass
#
#     @abstractmethod
#     def set_roof(self, value):
#         pass
#
#     @abstractmethod
#     def set_result(self):
#         pass
#
#
# class BudynekBuilder(Builder):
#
#     def __init__(self):
#         self.budynek = Budynek()
#
#     def set_doors(self, value):
#         self.budynek.doors = value
#         return self
#
#     def set_walls(self, value):
#         self.budynek.walls = value
#         return self
#
#     def set_okna(self, value):
#         self.budynek.okna = value
#         return self
#
#     def set_floors(self, value):
#         self.budynek.floors = value
#         return self
#
#     def set_roof(self, value):
#         self.budynek.roof = value
#         return self
#
#     def set_result(self):
#         return self.budynek
#
#
# class BudynekBuilderDirector:
#     @staticmethod
#     def construct():
#         builder = BudynekBuilder()
#         model = builder.set_doors(4).set_okna(3).set_walls(4).set_floors(8).set_roof("Prosty")
#         return model.set_result()
#
#
# def main():
#     car = BudynekBuilderDirector.construct()
#     print(car)
#
#
# if __name__ == '__main__':
#     main()


#==============================================================================
# Metoda - Strategia

# from abc import ABCMeta, abstractmethod
#
#
# class AbstractShippingProvider(metaclass=ABCMeta):
#
#     @abstractmethod
#     def calculate_cost(self):
#         raise NotImplementedError
#
#
# class FedEx(AbstractShippingProvider):
#
#     def __init__(self, rate):
#         self._rate = rate
#
#     def calculate_cost(self):
#         return self._rate
#
#
# class PostPoland(AbstractShippingProvider):
#
#     def calculate_cost(self):
#         return 42
#
#
# class Calculator:
#
#     def __init__(self, shipping_provider):
#         self.shipping_provider = shipping_provider
#
#     def calculate(self, mass, height, width):
#         if self.shipping_provider is None:
#             raise Exception('No shipping provider set')
#         else:
#             return self.shipping_provider.calculate_cost()
#
#     def set_shipping_provider(self, new_shipping_provider):
#         self.shipping_provider = new_shipping_provider
#
#
# def main():
#     post_poland = PostPoland()
#     shipping_calculator = Calculator(post_poland)
#
#     cost = shipping_calculator.calculate(15, 10, 20)
#     print(f'Shipping cost with Post Poland is {cost}')
#
#     fedex = FedEx(rate=100)
#     shipping_calculator.set_shipping_provider(fedex)
#
#     cost = shipping_calculator.calculate(15, 10, 20)
#     print(f'Shipping cost with FedEx is {cost}')
#
#
# if __name__ == '__main__':
#     main()

#======================================================================
# WZORZEC PROJEKTOWY FACTORY

#
# from abc import ABCMeta, abstractmethod
#
#
# class Beer(metaclass=ABCMeta):
#     pass
#
#
# class Tuborg(Beer):
#     pass
#
#
# class Staropramen(Beer):
#     pass
#
#
# class Snack(metaclass=ABCMeta):
#
#     @abstractmethod
#     def interact(self, beer: Beer) -> None:
#         pass
#
#
# class Peanuts(Snack):
#
#     def interact(self, beer: Beer) -> None:
#         print(f'Drinking some {beer.__class__.__name__} with peanuts')
#
#
# class Chips(Snack):
#
#     def interact(self, beer: Beer) -> None:
#         print(f'Drinking some {beer.__class__.__name__} with chips')
#
#
# class AbstractShop(metaclass=ABCMeta):
#
#     @abstractmethod
#     def buy_beer(self) -> Beer:
#         pass
#
#     @abstractmethod
#     def buy_snack(self) -> Snack:
#         pass
#
#
# class ExpensiveShop(AbstractShop):
#
#     def buy_beer(self) -> Beer:
#         return Tuborg()
#
#     def buy_snack(self) -> Snack:
#         return Peanuts()
#
#
# class CheapShop(AbstractShop):
#
#     def buy_beer(self) -> Beer:
#         return Staropramen()
#
#     def buy_snack(self) -> Snack:
#         return Chips()
#
#
# def main():
#     expensive_shop = ExpensiveShop()
#     beer = expensive_shop.buy_beer()
#     snack = expensive_shop.buy_snack()
#     snack.interact(beer)
#
#     cheap_shop = CheapShop()
#     snack = cheap_shop.buy_snack()
#     beer = cheap_shop.buy_beer()
#     snack.interact(beer)
#
#
# if __name__ == '__main__':
#     main()

#========================================================

# Factory Method

# from abc import ABC, abstractmethod
#
#
# class MazeGame(ABC):
#
#     def __init__(self):
#         self.rooms = []
#         self._prepare_rooms()
#
#     def _prepare_rooms(self):
#         room1 = self.make_room()
#         room2 = self.make_room()
#
#         room1.connect(room2)
#         self.rooms.append(room1)
#         self.rooms.append(room2)
#
#     def play(self):
#         print('Playing using "{}"'.format(self.rooms[0]))
#
#     @abstractmethod
#     def make_room(self):
#         raise NotImplementedError("You should implement this!")
#
#
#     def make_room(self):
#         return MagicRoom()
#
#
# class OrdinaryMazeGame(MazeGame):
#
#     def make_room(self):
#         return OrdinaryRoom()
#
#
# class Room(ABC):
#     def __init__(self):
#         self.connected_rooms = []
#
#     def connect(self, room):
#         self.connected_rooms.append(room)
#
#
# class MagicRoom(Room):
#     def __str__(self):
#         return "Magic room"
#
#
# class OrdinaryRoom(Room):
#     def __str__(self):
#         return "Ordinary room"
#
#
# ordinaryGame = OrdinaryMazeGame()
# ordinaryGame.play()
#
# magicGame = MagicMazeGame()
# magicGame.play()

#=================================================================
# Singleton na ogół się nie stosuję, ale trzeba znac
# Klasa która w całej Aplikacji ma tylko jedną instancję.
# n.p. logery

# def singleton(cls):
#     instances = {}
#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls()
#         return instances[cls]
#     return getinstance
#
# @singleton
# class MyClass:
#     pass

#===================================================================

