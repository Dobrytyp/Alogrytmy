# from datetime import datetime
# now = datetime.now()
#
# from random import randint
# lst = []
# while len(lst) < 5000:
#     liczba = randint(1, 100000)
#     if liczba in lst:
#         continue
#     lst.append(liczba)
# print(lst)
#
# oldnow = datetime.now()
#
# def bubblesort(lst):
#     n = len(lst) - 1
#     for i in range(n):
#         for j in range(n-i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
#
#
# print(bubblesort(lst))
#
# now = datetime.now()
#
# print("bubble sort", now - oldnow)
#
#
# oldnow = datetime.now()
#
# def selectionsort(lst):
#     for i in range(len(lst)):
#         min_idx = i
#         for j in range(i+1, len(lst)):
#             if lst[j] < lst[min_idx]:
#                 min_idx = j
#
#         lst[i], lst[min_idx] = lst[min_idx], lst[i]
#     return lst
#
# print(selectionsort(lst))
#
# now = datetime.now()
#
# print("selection sort", now - oldnow)
#
#
# oldnow = datetime.now()
#
# def insertionsort(lst):
#     for idx in range(1, len(lst)):
#         value, pos = lst[idx], idx
#
#         while lst[pos-1] > value and pos > 0:
#             lst[pos] = lst[pos - 1]
#             pos -= 1
#         lst[pos] = value
#     return lst
#
# print(insertionsort(lst))
#
#
# now = datetime.now()
#
# print("insertion sort", now - oldnow)
#
#
# oldnow = datetime.now()
#
# def merge_sort(lst):
#     if len(lst) > 1:
#         mid = len(lst)//2
#         left, right = lst[:mid], lst[mid:]
#         left, right = merge_sort(left), merge_sort(right)
#
#         i, j, k = 0, 0, 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 lst[k] = left[i]
#                 i += 1
#             else:
#                 lst[k] = right[j]
#                 j += 1
#             k += 1
#
#         while i < len(left):
#             lst[k] = left[i]
#             i += 1
#             k += i
#
#         while j < len(right):
#             lst[k] = right[j]
#             j += 1
#             k += 1
#
#     return lst
#
# print(merge_sort(lst))
#
# now = datetime.now()
#
# print("quick sort", now - oldnow)
#
#
# oldnow = datetime.now()
#
# def sorted_(lst):
#     lst = sorted(lst)
#     return lst
#
# print(sorted_(lst))
#
# now = datetime.now()
#
# print("sorted", now - oldnow)


# Given a list of numbers. Determine the element in the list with the largest value. Print the value of the largest element and then the index number.
# If the highest element is not unique, print the index of the first instance.

# Napisz funkcję, która sprawdzi, czy podana liczba jest doskonała (tj. jest
# sumą swoich dzielników właściwych, np. 6 = 1 + 2 + 3).

# def doskonala(n):
#     dzielniki = []
#     for i in range(1, n):
#         if n % i == 0:
#             dzielniki.append(i)
#     if sum(dzielniki) == n:
#         return "jest doskonała"
#     else:
#         return "Nie jest"
#
#
# if __name__ == '__main__':
#     print(doskonala(4))
#     print(doskonala(6))


# def roman_numbers(n):
#     lst_rom = []
#     lst_rom2 = []
#     for i in n:
#         lst_rom.append(i)
#     print(lst_rom)
#     lst_rom2(lst_rom.insert(0, "o"))
#     lst_rom = lst_rom.insert(0, "o")
#     # for i in lst_rom:
#     #     if i == 'C' and i(+1)
#
#
#     return lst_rom, lst_rom2
#
# if __name__ == '__main__':
#     print(roman_numbers("CMM"))


# Bąbelki

#
#
# def bubblesort(lst):
#     n = len(lst) -1
#     for i in range(n):
#         for j in range(n-i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
#
# lista = [4, 54, 123, 1, 13, 8, 1]
# print(bubblesort(lista))
#
# def bubblesort2(lst):
#     n = len(lst) - 1
#     for i in range(n):
#         for j in range(n-i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst

#
#
# print(bubblesort2(lista))
#
#
# def bubblesort3(lst):
#     n = len(lst) -1
#     for i in range(n):
#         for j in range(n- i):
#             if lst[j] > lst[j+1]:
#                 lst[j], lst[+1] = lst[j+1], lst[j]
#     return lst
#
# print(bubblesort3(lista))



list1 =  [1, 2, 3, 4, 5]
def daily(lst):
    new_list = []
    suma = 1
    for i in lst:
        suma *= i
    for i in lst:
        new_list.append(int(suma/i))
    return new_list

print(daily(list1))
print(daily([3, 2, 1]))












