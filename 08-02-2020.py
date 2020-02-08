# ALGORYTMY i STRUKTURY DANYCH

# Złożonośc obliczeń



# lista = [89, 30, 52, 58, 73, 22, 77, 85, 21, 70, 22, 43, 53, 39, 26, 56, 24, 42, 49]
#
# lista2 = [34, 15, 19, 7, 79, 74, 66, 25, 48, 83, 87, 82, 32, 77, 70, 50, 74, 63, 1]

# lista3 = []
# for i in lista:
#     if i in lista2:
#         lista3.append(i)
#
# print(lista3)

# def common_elements(lista, lista2):
#     common_elem = []
#     for elem in lista:
#         if elem in lista2:
#             common_elem.append(elem)
#     return common_elem
#
# print(common_elements([1,3,5,6,9,11], [2,3,5,23,44]))

# Zwiększamy wydajność

# def common_elements(lista, lista2):
#     common_elem = []
#     lista2 = set(lista2)        # zrobiliśmy seta żeby nie iterować
#     for elem in lista:
#         if elem in lista2:
#             common_elem.append(elem)
#     return common_elem
#
# print(common_elements([1,3,5,6,9,11], [2,3,5,23,44]))

# Napisz program znajdujący tak podział listy, by wartość bezwzględna sum elementów po loewej stronie i elementów
# po prawej była jak najmniejsza. Zwróc tę wartość. Okreś złożóność programu

# def get_min_diff(lst):
#     differences = []
#     for i in range(1, len(lst)):
#         differences.append(abs(sum(lst[:i]) - sum(lst[i:])))
#     return min(differences)
#
# lst = [3, 1, 2, 4, 3]
# print(get_min_diff(lst))
#
# def get_min_diff2(lst):
#     return min([abs(sum(lst[:i]) - sum(lst[i:])) for i in range(1, len(lst))])
#
# lst = [3, 1, 2, 4, 3]
# print(get_min_diff2(lst))
#
# def get_min_diff3(lst):
#     differences = []
#     left, right = 0, sum(lst)
#     for elem in lst:
#         left += elem
#         right -= elem
#         differences.append(abs(left - right))
#
#     return min(differences)
#
# print(get_min_diff3(lst))

# Napisz program sumujący elementy ciągu powstałego w wyniku użycia funkcji range. Okreś jeso zlożoność


# lista = list(range(0, 20, 3)) # To jest stałyt element
#
# def get_sum(lista):
#     suma = 0
#     for i in lista:
#         suma += i
#     return suma
#
# print(get_sum(lista))
#
# # Albo
#
# def get_sum2(lista):
#     return sum(lista)
#
# print(get_sum2(lista))
#
# # Albo Najlepiej
#
# def get_sum3(lista):
#     return (lista[0] + lista[-1]) / 2 * len(lista)
#
# print(get_sum3(lista))

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