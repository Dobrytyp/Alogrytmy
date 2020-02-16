# #Pierwsze

# pierwsze = []

# def prime_in_range(n):
#     if n > 1:
#         for i in range(2, n-1):
#             if n % i == 0:
#                 break
#         else:
#             pierwsze.append(n)
#         prime_in_range(n-1)
#     else:
#         print(pierwsze)
        
# print(prime_in_range(100))

#---------------------------------------------------------------------

# fibonacci = []

# def fibbonacci_string(n):
#     if n == 1:
#         return 0 
#     elif n == 2:
#         return 1
#     else:
#         return fibbonacci_string(n-1) + fibbonacci_string(n-2)
    
# print(fibbonacci_string(9))

#-----------------------------------------------------------------

# silnia

# def silnia(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 2
#     else:
#         wynik = 1
#         for i in range(1, n+1):
#             wynik *= i
#         return wynik

# print(silnia(6))

#--------------------------------------------------------------------

# # silnia rekurencyjnie

# def silnia_rek(n):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return 1
#     else:
#         return n * silnia_rek(n-1)

# print(silnia_rek(5))
