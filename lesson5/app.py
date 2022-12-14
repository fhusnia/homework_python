# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }

# string = "firstname Elcin, username elchina, birthday 18-08-2000"

# Dict = dict((x.strip(), y.strip())
#              for x, y in (element.split(' ') 
#              for element in string.split(', ')))
# user_info.update(Dict)
# print(user_info)

# Istifadəçi sizə "5 salam" şəklində solda ədəd, ortada, boşluq, sağda isə bir input verəcək.
#  Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər yazıb, istifadəçiyə qaytarın.
#  Örnək yuxaridakı inputun outputu salam salam salam salam salam  

# x = input()
# newlist = list(x.split(" "))
# newlist2 = (newlist[1] + ' ') * int(newlist[0])
# print(newlist2)


# İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. Örnək:
# Input: This is an example! 
# Output: sihT si na !elpmaxe

# x = "This is an example!"
# alma = x[::-1].split(' ')
# alma.reverse()
# print(' '.join(alma))


# 1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
# 2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
# 3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
# 4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin

# users = [
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]


# username = input('username: ')
# finded_user = None
# for user in users:
#     if user['username'] == username:
#         finded_user = user

# if not finded_user:
#     print('Istifadeci tapilmadi!')
#     exit()

# sifre = input('sifre: ')


# if finded_user['password'] == sifre:

#         if finded_user['blocked'] == False:
#             print('siz daxil ola bilmezsiniz')
#         else:
#             print(finded_user['name'] + " "'girish etdiniz')
# else:
#      print('sifre sehvdir')

#  Bunları konsolda göstərin
#     1. İstifadəçinin boyunu artırın
#     2. Telefonun markasını dəyişərək Samsung edin
#     3. İstifadəçinin adını silin
#     4. İstifadəçinin ilk sifarişini silin
#     5. İstofadəçinin sifarişlərinin başına ball əlavə edin
#     6. Sonuna headphones əlavə edin

# user = {
#     'name': 'Elnur',
#     'height': 179,
#     'phone': {
#         'model': 'Iphone',
#     },
#     'orders': ['book', 'mouse', 'mousepad']
# }

# print(user['height'] + 1)
# change = user['phone']['model'] = 'Samsung'
# print(change)
# del user['name']
# del user['orders'][0]
# user['orders'][0] = 'ball' 
# print(user['orders'])
# user['orders'].append('headphones')
# print(user)


# Dictionary əsasən istifadəçi sizə məhsul adı girəcək. 
# Bu məhsulun mağazada olan qiymətini göstərən proqram hazırlayın. Girilən məhsul mağaza da olmadığı halda "None" qaytarın.
#  Mağazaya yeni məhsullar və qiymətlərini əlavə edin.
#  Mağazada nə qədər məhsul olduğunu göstərin
#  Məhsulların qiymətini 30% artırıb yeni qiymətləri mağazaya əlavə edin.


# shop = {
# 	"t-shirt" : 59.00,
# 	"jeans" : 75.00,
# 	"sweatshirt" : 60.00, 
# 	"shoe" : 124.99, 
# 	"jacket" : 154.90
# }
# search_productname = None
# productname = input()
# for key,value in shop.items():
#     if key == productname:
#         print(value)
#         search_productname = value
# if not search_productname:
#         print(search_productname)
#         exit()


# shop['goggles'] = 200.99
# print(shop)

# print(len(shop.keys()))

# for key,value in shop.items():
#     newvalue = value + (value * 30/100)
#     shop[key] = newvalue
# print(shop)


# listone = [2384, 12385, 13226, 653, 12362423] 
# list içərisindəki ədədlərin key olduğu və value-ların həmin ədədlərin rəqəm sayı 
# olduğu bir dictionary hazırlayın
# result={i : int(i) for i in listone}
# print(result)

# -100-dən müsbət 100-ə qədər ədədlər arasında 7-yə bölünən ədədlərin 3-ə vurulmasından ibarət bir list qurun.
#  Bunun üçün range və list comprehensions istifadə edin.

# result=[i * 3  for i in range(-100,100) if i % 7 == 0 ]
# print(result)

# info = ["Resul", "Serifov", 35]
# Yuxarıdakı arrayı dinamik olaraq ["Resul Serifov", 25] vəziyyətinə gətirin

# info.insert(0,info[0] + ' '+info[1])
# del1 = info.pop(1)
# del2 = info.pop(1)
# print(info)