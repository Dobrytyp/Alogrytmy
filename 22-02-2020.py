# WZORCE PROJEKTOWE I DOBRE PRAKTYKI

# PEP 8 to zestaw reguł który definiuje w jaki sposób pisać kod

# class Student:
#     NUMBER_OF_BEERS = 40            # Atrybut Klasy
#
#     def __init__(self, first_name, second_name):    # Atrybut instancji
#         self.first_name = first_name
#         self.second_name = second_name
#
#     def foo(self):      # Metoda instancji
#         pass
#
#     @classmethod        # Metoda Klasy
#     def bar(cls):
#         pass
#
#     @staticmethod       # Metoda Statyczna używana przez klasę, ale traktowana jako stała
#     def spam():
#         return 42
#
#
#
# jack = Student("jack", "simpson")
# print(jack.first_name)

# -------------------------------------------------------------------------------

# Atrybut prywatny (metoda prywatna), Atrybut publiczny (metoda publiczna)


# class Student:
#     NUMBER_OF_BEERS = 40  # Atrybut Klasy
#
#     def __init__(self, first_name, second_name):    # Atrybut instancji
#         self._first_name = first_name               # Żeby oznaczyć atrybut jako prywatny dajemy na początku "_"
#         self._second_name = second_name
#
#     def _foo(self):                                 # Meotdę rpywatną też oznaczamy "_" na poczatku
#         pass
#
#
# jack = Student("jack", "simpson")
# print(jack._first_name)


#--------------------------------------------------------------

x = None
if not x:
    pass

if x == None:
    pass
if x is None:       # To jest prawidłowy zapis !
    pass

#--------------------------------------------------------------

# Cwiczenie 1

