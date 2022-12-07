#1-----
# #1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın (1+2+3+...+99+100)
# values = range(101)
# num = 0
# for  i in values:
#     num += i
# print(num);



#2
# #100000-dən aşağı doğru gedərək 9999-a bölünən ilk ədədi konsolda göstərin.
# for i in range(100000, 0, -1):
#     if i % 9999 == 0:
#         print(i)
#         break
#

#3
#'I study Python every day’ bu stringin saitlər çıxarılmış vəziyyətini konsolda göstərin.

# text = 'I study Python every day'
# textreverse = text[::-1]
# vowels = 'aeiuo'
# result = ''
# for char in textreverse:
#     if char not in vowels:
#         result += char
# print(result)

# 4
# (Orta) İstifadəçinin girdiyi cümlədə neçə heca olduğunu deyən program hazırlayın. Hecaların sayını tapmaq üçün saitlərdən istifadə edin.

# text = input()
# vowels = 'aeiuo'
# result = ""
# for num in text:
#     if num  in vowels:
#         result += num

        
# print(len(result))


#Girilən ədədin sadə bölənlərini göstərən kod hazırlayın. Örnək 12 ⇒ 2, 2, 3
# values = input()
# for i in range(2,int(values)):
#     if int(values) % i == 0:
#         print(int(values) // i )
        # while int(values) // i >= 0:
        #     print(int(values))

num = 133
inter = range(num)
result = 0
for i in inter:
    result += i
print(result)     
