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
# print(selectionsort(lst))

# To samo ale inaczej ------------------------------------------

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


# Sortowanie przez wstawianie ============================================================

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

# Albo ----------------------------------------

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


# DZIEL I RZĄDŹ ===========================================================================

# Wyszukiwanie linearne -------------------------------------------------------------------

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
# # Albo -------------------------------------------------------
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

# Wyszukiwanie Binarne ======================================

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

# Albo ---------------------------------------

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


# Merge Sort ========================================================


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
# lst = [1, 5, 4, 95, 3, 87]
# print(merge_sort(lst))

# Quick Sort =====================================================================

# lst = [10, 8, 1, 7, 14, 2, 17, 13]
#
# def quicksort(lst):
#     if len(lst) < 2:
#         return lst
#     pivot = lst[0]
#     left, right,  equal = [], [], []
#     for i in lst[1:]:
#         if i < pivot:
#             left.append(i)
#         elif i == pivot:
#             equal.append(i)
#         else:
#             right.append(i)
#
#     return quicksort(left) + [pivot] + quicksort(right)
#
# print(quicksort(lst))



#-----------------------------------------------

# def quicksort_inaczej(lst):
#
#     less = []
#     equal = []
#     greater = []
#
#     if len(lst) > 1:
#         pivot = lst[0]
#         for i in lst:
#             if i > pivot:
#                 greater.append(i)
#             elif i < pivot:
#                 less.append(i)
#             else:
#                 equal.append(i)
#
#
#     else:
#         return lst
#
# lst = [10, 8, 1, 7, 14, 2, 17, 13]
# print(quicksort_inaczej(lst))

#------------------------------------------------------

# lst = [10, 8, 1, 7, 14, 2, 17, 13]
#
# def quicksort_4(lst):
#     if len(lst) == 1 or len(lst) == 0:
#         return lst
#     else:
#         pivot = lst[0]
#         i = 0
#         for j in range(len(lst) - 1):
#             if lst[j + 1] < pivot:
#                 lst[j + 1], lst[i + 1] = lst[i + 1], lst[j + 1]
#                 i += 1
#         lst[0], lst[i] = lst[i], lst[0]
#         first_part = quicksort_4(lst[:i])
#         second_part = quicksort_4(lst[i + 1:])
#         first_part.append(lst[i])
#         return first_part + second_part
#
# print(quicksort_4(lst))

#========================

# To nie działa

# def get_k_max(lst, k):
#     sorted_lst = quicksort(lst)
#     return sorted_lst[-k]
#
# if __name__ == "__main__":
#     parser = ArgumentParser()
#     parser.add_argument("--k", type=int, required=True)
#     args = parser.parse_args()
#
#     lista = [5, 3, 1, 7, 13 ,9 ,2]
#     print(get_k_max(lista, args.k))


# Napisz program, w którym użytkonik podaje n liczb całkowitych jako

# from argparse import ArgumentParser
#
# def cumulative_sum(lst):
#     sums = []
#     total = 0
#
#
#
# def sum_section(lst, start, stop):
#     return sum(lst[start:stop+1])
#
# if __name__ == "__main__":
#     parser = ArgumentParser()
#     parser.add_argument("--list", "-l", nargs="+", required=True)
#     args = parser.parse_args()
#
#     lst = list(map(int, args.list))
#     n = int(input("podaj liczbę przediałów\n"))
#     print(n)
#     for _ in range(n):
#         start, stop = input("podja przedział\n").split()
#         start, stop = int(start), int(stop)
#         print(sum_section(lst, start, stop))
#


from argparse import ArgumentParser


def sum_section(lst, start, stop):
    return sum(lst[start:stop+1])


def cumulative_sum(lst):
    sums = []
    total = 0
    for elem in lst:
        total += elem
        sums.append(total)
    return sums


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--list", "-l", nargs="+", required=True)
    args = parser.parse_args()

    lst = list(map(int, args.list))
    cum_sum = cumulative_sum(lst)
    n = int(input("Podaj liczbę przedziałów\n"))
    for _ in range(n):
        start, stop = input("Podaj przedział\n").split()
        start, stop = int(start), int(stop)
        if start == 0:
            print(cum_sum[stop])
        else:
            print(cum_sum[stop] - cum_sum[start-1])