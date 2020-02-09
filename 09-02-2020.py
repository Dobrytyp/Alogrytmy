# Sortowanie bombpelkowe

# lista = [5,8,1,4,9,4]
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
# lista = [4, 54, 123, 1, 13, 8, 1]
# print(bubblesort(lista))


# Sortowanie przez wybór ==================================

# lst = [ 3, 2, 4 ,3 ,1 ,2, 0]
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
# print(selectionsort(lst)) =================================

# To samo ale inaczej

# def Insert_sort(A):
#     for i in range(1,len(A)):
#         klucz = A[i]
#         j = i - 1
#         while j>=0 and A[j]>klucz:
#             A[j + 1] = A[j]
#             j = j - 1
#         A[j + 1] = klucz
#     return A
#
# print(Insert_sort(lst))


# Sortowanie przez wstawianie

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
# lst = [ 3, 2, 4 ,3 ,1 ,2, 0]
#
# print(insertionsort(lst))

# Albo

# lst = [ 3, 2, 4 ,3 ,1 ,2, 0]
#
# def insertionsort2(lst):
#     for i in range(1, len(lst)):
#         klucz = lst[i]
#         j = i - 1
#         while j >= 0 and lst[j] > klucz:
#             lst[j + 1] = lst[j]
#             j = j - 1
#         lst[j + 1] = klucz
#     return lst
#
# print(insertionsort2(lst))


# DZIEL I RZĄDŹ

# Wyszukiwanie linearne

# n = 7
# lst = [2, 3, 5, 7, 11, 13, 22]
#
# def linear_search(lst, to_find):
#     for idx, elem in enumerate(lst):
#         if elem == to_find:
#             return idx
#     return -1
#
# print(linear_search(lst, n))
#
# # Albo
#
# def wysz_liniowe(lst, n):
#     idx = 0
#     for i in lst:
#         if i == n:
#             return idx
#         else:
#             idx +=1
#
# print(wysz_liniowe(lst, n))
#
# n = 7
# lst = [2, 3, 5, 7, 11, 13, 22]

# Wyszukiwanie Binarne

# def binary_search(lst, start, end, to_find):
#     if start > end:
#         return -1
#     mid = (start + end) //2
#     if lst[mid] == to_find:
#         return mid
#     elif lst[mid] > to_find:
#         return binary_search(lst, start, mid-1, to_find)
#     return binary_search(lst, mid+1, end, to_find)
#
# print(binary_search(lst, 0, len(lst), n))

# Albo

# n = 7
# lst = [2, 3, 5, 7, 11, 13, 22]
#
# def binary_search2(lst, to_find):
#     mid = len(lst) //2
#     if lst[mid] == to_find:
#         return mid
#     elif lst[mid] > to_find:
#         return binary_search2(lst[mid], to_find)
#     return binary_search2(lst[mid+1:], to_find) + mid + 1
#
# print(binary_search2(lst, n))


