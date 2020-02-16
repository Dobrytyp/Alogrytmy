# class Kolejka:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, x):
#         self.queue.append(x)
#
#
#     def dequeue(self):
#         if not self.empty():
#             self.queue.pop(0)
#             return self.queue
#         else:
#             return None
#
#     def empty(self):
#         return len(self.queue) == 0
#
#     def __str__(self):
#         return str(self.queue)

#--------- Nowe zadanie ------------ NIE DZIALA

# class Stos:
#     def __init__(self):
#         self.queue1 = Kolejka()
#         self.queue2 = Kolejka()
#
#     def push(self, item):
#         self.queue2.enqueue(item)
#         while not self.queue1.empty():
#             self.queue2.enqueue((self.queue1.dequeue()))
#
#         self.queue1, self.queue2 = self.queue2, self.queue1
#
#
#     def pop(self):
#         if not self.empty():
#             return self.queue1.dequeue()
#         else:
#             print("nie można pobrać elementu z pustego stosu")
#             return None
#
#     def empty(self):
#         return self.queue1.empty()
#
#     def __str__(self):
#         pass
#
# if __name__ == "__main__":
#     stack = Stos()
#     stack.push(3)
#     stack.push(5)
#     stack.push(9)
#     stack.push(11)
#
#     print(stack.pop())


# Zadanie Zaimplementuj kalkulator do rozwiązywania wyrażeń zapisanych w odwrotnej notacji polskiej.
# np. dla wyrażenia„3 5 2 * +” powinien zwrócić wynik 13„15 7 1 1 + − ÷ 3 × 2 1 1 + + −”
# powinien zwrócić 5„6 2 3 + - 3 8 2 / + * 2 5 3 + + +” powinien zwrócić 17

#                                            ZRÓB TO !  ZROBILEM!


# class Stos:                 # Tu masz obiektówkę stosu, zapisz sobie pewnie ci się przyda
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.empty():
#             return self.stack.pop()
#         else:
#             print("stos jest pusty")
#
#     def empty(self):
#         return len(self.stack) == 0
#
#     def __str__(self):
#         return str(self.stack)
#
# stos1 = Stos()
#
# def expression(symbol, a ,b):           # Tu masz lamdę z działań arytmetycznych
#     symbols = {
#         "+": lambda a, b: a + b,
#         "-": lambda a, b: a - b,
#         "*": lambda a, b: a * b,
#         "/": lambda a, b: a / b,
#     }
#     func = symbols[symbol]
#     return func(a, b)
#
# def onp(wzor):                  # a tu sam zrobiłenm
#     wzor = wzor.split(" ")
#     for i in wzor:
#         if i =="+":
#             a = int(stos1.pop())
#             b = int(stos1.pop())
#             c = expression("+", b, a)
#             stos1.push(c)
#         elif i =="-":
#             a = int(stos1.pop())
#             b = int(stos1.pop())
#             c = expression("-", b, a)
#             stos1.push(c)
#         elif i =="*":
#             a = int(stos1.pop())
#             b = int(stos1.pop())
#             c = expression("*", b, a)
#             stos1.push(c)
#         elif i =="/":
#             a = int(stos1.pop())
#             b = int(stos1.pop())
#             c = expression("/", b, a)
#             stos1.push(c)
#         else:
#             stos1.push(i)
#
#
#
#     return stos1
#
# print(onp("3 5 2 * +"))

# Albo

# class Stos:
#     def __init__(self):
#         self.stack = []
#
#     def push(self, item):
#         self.stack.append(item)
#
#     def pop(self):
#         if not self.empty():
#             return self.stack.pop()
#         else:
#             print("stos jest pusty")
#
#     def empty(self):
#         return len(self.stack) == 0
#
#     def __str__(self):
#         return str(self.stack)
# stos1 = Stos()
#
# def expression(symbol, a ,b):
#     symbols = {
#         "+": lambda a, b: a + b,
#         "-": lambda a, b: a - b,
#         "*": lambda a, b: a * b,
#         "/": lambda a, b: a / b,
#     }
#     func = symbols[symbol]
#     return func(a, b)
#
# def calculate(exp_str):
#     stack = Stos()
#     symbols = {"+", "-", "*", "/"}
#     elements = exp_str.split()
#     for i in elements:
#         if i in symbols:
#             a = stack.pop()
#             b = stack.pop()
#             resault = expression(i, b, a)
#             stack.push(resault)
#         else:
#             stack.push(int(i))
#
#     return stack.pop()
#
# print(calculate("3 5 2 * +"))

#---------------------------------


# import math
# import os
# import random
# import re
# import sys
# class Stos:
#     def __init__(self):
#         self.stack = []
#     def push(self, item):
#         self.stack.append(item)
#     def pop(self):
#         if not self.empty():
#             return self.stack.pop()
#         else:
#             print("Stos jest pusty")
#             return None
#     def empty(self):
#         return len(self.stack) == 0
# opening_brackets = ["[", "(", "{"]
# closing_brackets = ["]", ")", "}"]
# # Complete the isBalanced function below.
# def isBalanced(s):
#     stack = Stos()
#     for char in s:
#         if char in opening_brackets:
#             stack.push(char)
#         else:
#             start = stack.pop()
#             if start != opening_brackets[closing_brackets.index(char)]:
#                 return "NO"
#     return "YES" if stack.empty() else "NO"
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     t = int(input())
#     for t_itr in range(t):
#         s = input()
#         result = isBalanced(s)
#         fptr.write(result + '\n')
#     fptr.close()

#===========================================================
# ALOGRYTMY ZACHłANNE


# Istnieje N lin ponumerowanych od 0 do N - 1, których długości podano w tablicy A, leżącej na podłodze w linii.
# Dla każdego I (0 ≤ I <N) długość liny I na linii wynosi A [I].
#
# Mówimy, że dwie liny I i I + 1 sąsiadują ze sobą. Dwie sąsiednie liny można związać razem węzłem,
# a długość związanej liny jest sumą długości obu lin. Powstałą nową linę można następnie ponownie związać.
#
# Dla danej liczby całkowitej K celem jest związanie lin w taki sposób, aby liczba lin,
# których długość była większa lub równa K, była maksymalna.
#
# Na przykład rozważmy K = 4 i tablicę A taką, że:
#
#     A [0] = 1
#     A [1] = 2
#     A [2] = 3
#     A [3] = 4
#     A [4] = 1
#     A [5] = 1
#     A [6] = 3
# Liny pokazano na poniższym rysunku.
#
#
#
# Możemy związać:
#
# lina 1 z liną 2 do wytworzenia liny o długości A [1] + A [2] = 5;
# lina 4 z liną 5 z liną 6 do wytworzenia liny o długości A [4] + A [5] + A [6] = 5.
# Następnie będą trzy liny, których długości są większe lub równe K = 4. Nie można wyprodukować czterech takich lin.


# a = [1, 2, 3, 4, 1, 1, 3]
#
# def solution(K, A): # Wymagana Długość k,
#     ropes = 0
#     current_sum = 0
#     for elem in A:
#         current_sum += elem
#         if current_sum >= K:
#             ropes += 1
#             current_sum = 0
#
#     return ropes
# print(solution(4, a))

#-----------------------------------------

# stan = {
#     10:1,
#     20:2,
#     50:1,
#     100:0,
#     200:0
# }
#
# def bankomat(lst, a):
#     suma = lst[0]*10 + lst[1]*20 + lst[2]*50 + lst[3]*100+ lst[4]*200
#     if a > suma:
#         return "Nie można wypłacić żadanej kwoty"
#     else:
#
#
# print(bankomat(lst, 80))

#--------------------------------------------------

# W liście znajdź wszystkie pary liczb, które sumują się do zadanej liczby.
# Np. dla listy [2, 4, 3, 5, 7, 8, 9] i szukanej sumy równej 7 chcemy otrzymać dwie
# pary: [(2, 5), (4, 3)].

# list1 = [2, 4, 5, 5, 7, 9]


# def get_pairs(lst, given_num):
#     pairs = []
#
#     for i in range(len(lst)):
#         for j in range(i+1, len(lst)):
#             if lst[i] + lst[j] == given_num:
#                 pairs.append((lst[i], lst[j]))
#     return pairs
#
# print(get_pairs([2, 4, 5, 5 ,7, 9], 7))


# Optymalizacja

# def get_pairs2(lst, given_num):
#     pairs = []
#     numbers_set = set()
#     for elem in lst:
#         b = given_num - elem
#         if b in numbers_set:
#             pairs.append((elem, b))
#         else:
#             numbers_set.add(elem)
#     return pairs
#
# print(get_pairs2([2, 4, 5, 5 ,7, 9], 7))


# def daily_coding_16_02(lst, k):
#     counter = 0
#     for i in lst:
#         for j in lst:
#             if i + j == k:
#                 return i, j, True
#
#
# print(daily_coding_16_02([10, 15, 3, 7], 17))

# def sumy_liczb(lst, given_num):
#     pary = []
#     numbers_set = set()
#     for elem in lst:
#         b = given_num - elem
#         if b in numbers_set:
#             pary.append((elem, b))
#             return True
#         else:
#             numbers_set.add(elem)
#     return pary
#
# print(sumy_liczb([10, 15, 3, 7], 17))


var1 = "Abdefghijklmnoprstuwzyz"
count = 0
for i in var1:
    count +=1

print(count)