# from math import pi

# def hesabla(r,h):
#     result = 1/3*pi*(r**2)*h
#     return result
# print(hesabla(12,12))

# def hesabla(r):
#     result = 4/3*pi*(r*r*r)
#     return result
# print(hesabla(2))

# import math
# def permutasiya(n,r):
#     if n < r:
#         return 'n boyuk olmalidir'
#     else:
#         a = math.factorial(n)
#         diff = math.factorial(n - r)
#         result = a/diff
#         return result
# print(permutasiya(2,3))

# from random import choice

# input1 = input('Adlari girin:').split(',')
# for i in range(len(input1)):
#     print(choice(input1))
#     input('')

# “Saat 17:00, 04.06.2022 tarixində dərsə gəlin” cümləsindən
#  istifadə edərək tarixi datetime formatına çevirin. 
# from datetime import datetime,timedelta

# hours = 50580000/90
# diff = datetime.now() + timedelta(hours=hours)
# print(diff)

# from datetime import datetime
# text = 'Saat 17:00, 04.06.2022 tarixində dərsə gəlin'
# text2 = 'Saat %I:%M, %d.%m.%Y tarixində dərsə gəlin'
# result = datetime.strptime(text,text2)
# print(result)

