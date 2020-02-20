# DCP1 = "\nGiven a list of numbers and a number k, return whether any two numbers from the list add up to k.\n" \
#        "For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17."
#
# def sumy_liczb(lst, given_num):
#     pary = []
#     numbers_set = set()
#     for elem in lst:
#         b = given_num - elem
#         if b in numbers_set:
#             pary.append((elem, b))
#             return True, elem, b
#         else:
#             numbers_set.add(elem)
#     return pary
#
# print(DCP1)
# print(sumy_liczb([10, 15, 3, 7], 17))
#
# #----------------------------------------------
#
# DCP2 = "\nGiven an array of integers, return a new array such that each element at index i of the new array\n" \
#        "is the product of all the numbers in the original array except the one at i.\n" \
#        "For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. \n" \
#        "If our input was [3, 2, 1], the expected output would be [2, 3, 6]."
#
# list1 =  [1, 2, 3, 4, 5]
# def daily(lst):
#     new_list = []
#     suma = 1
#     for i in lst:
#         suma *= i
#     for i in lst:
#         new_list.append(int(suma/i))
#     return new_list
#
# print(DCP2)
# print(daily(list1))
# print(daily([3, 2, 1]))

#------------------------------------------------------

# DCP2 = "Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well."

def coding(lst):
    new_list = []
    for i in lst:
        if i > 0:
            new_list.append(i)
    
    for i in range(1, max(new_list) + 2):
        if i not in new_list:
            return i
    

print(DCP4)
print(coding([3, 4, -1, 1]))
print(coding([1, 2, 0]))
