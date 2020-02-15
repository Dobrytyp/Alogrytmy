# Znajdź w liście najmniejszy i największy element optymalizująć liczbę porównań


# Najprostszy sposób
# lst = [10, 43, 88, 5, 63, 99]

# def naj_naj(lst):
#     mini = lst[0]
#     maxi = lst[0]
#     for i in lst:
#         if i < mini:
#             mini = i
#         elif i > maxi:
#             maxi = i
#     return mini, maxi
#
# print(naj_naj(lst))

# -----------------------------------
# Najszybszy sposób
# def naj_naj2(lst):
#     lst = sorted(lst)
#     return lst[0], lst[-1]
#
# print(naj_naj2(lst))

# ------------------------------------

# lst = [10, 43, 88, 5, 63, 99]
#
# def naj_naj3(lst):
#     mini = lst[0]
#     maxi = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] < mini:
#             mini = lst[i]
#         elif lst[i] > maxi:
#             maxi = lst[i]
#     return mini, maxi
#
# print(naj_naj3(lst))

# ---------------------------------
# Optymalizujemy

# lst = [10, 43, 88, 5, 63, 99]

# def naj_naj4(lst):
#     mini = lst[0]
#     maxi = lst[0]
#     is_n_even = False
#     n = len(lst)
#     if n % 2 == 0:
#         n -= 1
#         is_n_even = True
#
#     for i in range(1, n, 2):
#         if lst[i] > lst[i+1]:
#             current_min = lst[i+1]
#             current_max = lst[i]
#         elif lst[i] < lst[i+1]:
#             current_min = lst[i]
#             current_max = lst[i+1]
#
#         if current_max > maxi:
#             maxi = current_max
#         if current_min < mini:
#             mini = current_min
#
#     if is_n_even:
#         if lst[n] > maxi:
#             maxi = lst[n]
#         elif lst[n] < mini:
#             mini = lst[n]
#
#     return mini, maxi
#
# print(naj_naj4(lst))

# =======================================

# Zoptyamlizuj sortowanie bombelkowe
# Sam to zrbiłem, jak lista jest od razu ułożona to nie trzeba sortowąc kolejny raz

# def bubblesort(lst):
#     n = len(lst) - 1
#     flaga = True
#     for i in range(n):
#         for j in range(n-i):
#             if lst[j] > lst[j+1]:
#                 flaga = False
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#         if flaga:
#             return lst
#     return lst
#
# lista = [1, 2, 3, 4, 5, 6, 7, 8]
# print(bubblesort(lista))

# =========================================
# Znajdź najmniejszy brakujący element na posortowanej liście

# def brak(lst):
#     for i in range(len(lst)):
#         if lst[i] != i:
#             return i
#     return len(lst)
#
# print(brak([0,1,2,6,9,11,15]))
# print(brak([1,2,3,4,5,6,9,11,15]))
# print(brak(([0,1,2,3,4,5,6])))

# -------------------------------------------
# Optymalizujemy przez sortowanie binarne

# def brak_binarnie(lst, start, end):
#     if start > end:
#         return end + 1
#
#     if start != lst[start]:
#         return start
#
#     mid = (start + end) // 2
#
#     if mid == lst[mid]:
#         return brak_binarnie(lst, mid+1, end)
#     return brak_binarnie(lst, start, mid)
#
# def smallest_missing2(lst):
#     return brak_binarnie(lst, 0, len(lst)-1)
#
# lst = [0, 1,2,3,4,5,6,7,11,15]
# print(smallest_missing2(lst))


# Znajdź indeks pierwszego wyśtąpienia elementu w posorotowanej liście

# lst = [2,5,5,5,6,6,8,9,9,9]
#
# def find_min_idx(lst, n):
#     counter = -1
#     for i in lst:
#         if i != n:
#             counter += 1
#         elif i == n:
#             counter += 1
#             return counter
#     else:
#         return -1
#
# print(find_min_idx(lst, 6))

# --------------------------------

# lst = [2,5,5,5,6,6,8,9,9,9]
#
# def find_min_idx_binary(lst, to_find):
#     start, stop = 0, len(lst)-1
#     resault = -1
#     while start <= stop:
#         mid = (start + stop) //2
#         if lst[mid] == to_find:
#             resault = mid
#             stop = mid - 1
#         elif to_find < lst[mid]:
#             stop = mid - 1
#         else:
#             start = mid + 1
#     return resault
# #
# #
# # print(find_mix_idx_binary(lst, 5))
#
# # -------------------------------------------------
#
# # lst = [2,5,5,5,6,6,8,9,9,9]
#
# def find_max_idx_binary(lst, to_find):
#     start, stop = 0, len(lst)-1
#     resault = -1
#     while start <= stop:
#         mid = (start + stop) //2
#         if lst[mid] == to_find:
#             resault = mid
#             start = mid + 1
#         elif to_find < lst[mid]:
#             stop = mid - 1
#         else:
#             start = mid + 1
#     return resault
# #
# # print(find_max_idx_binary(lst, 5))
#
# # --------------------------------------------------
#
# lst = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
#
#
# def how_many(lst, number):
#     max_idx = find_max_idx_binary(lst, number)
#     min_idx = find_min_idx_binary(lst, number)
#     if min_idx == -1:
#         return 0
#     return max_idx - min_idx +1
#
# print(how_many(lst, 5))

# STOS
# Struktura typu LIFO (last in, first out)

class Stos:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.empty():
            return self.stack.pop()
        else:
            print("stos jest pusty")

    def empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)
#
# stack = Stos()
# stack.push(5)
# stack.push(6)
# stack.push(9)
# stack.push(2)
#
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
# # print(stack.pop())
#
# print(stack)

# KOLEJKI
# Struktura typu FIFO (first in, first out)

# class Kolejka:
#     def __init__(self):
#         self.queue = []
#
#     def enqueue(self, x):
#         self.queue.append(x)
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
#
# kol = Kolejka()
# kol.enqueue(5)
# kol.enqueue(9)
# kol.enqueue(2)
# kol.enqueue(4)
#
# print(kol)
#
# print(kol.dequeue())


# Zrób kolejkęz dwóch sotsów


class Kolejka:
    def __init__(self):
        self.stack1 = Stos()
        self.stack2 = Stos()

    def enqueue(self, elem):
        while not self.stack1.empty():
            self.stack2.push(self.stack1.pop())
        self.stack1.push(elem)

    def dequeue(self):
        if not self.empty():
            return self.stack1.pop()
        else:
            return None

    def empty(self):
        return self.stack1.empty()

    def __str__(self):
        return str(self.stack1)

kol = Kolejka()
kol.enqueue(5)
kol.enqueue(9)
kol.enqueue(2)
kol.enqueue(4)



print(kol.dequeue())
print(kol.dequeue())
print(kol.dequeue())
print(kol.dequeue())