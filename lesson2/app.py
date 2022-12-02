
# 1 kart = “5382-1739-9201-9017” bank kartı məlumatını daşıyan variablein ilk 8 nömrəsini ulduzlanmış şəkildə print edin.
# kart = “5382-1739-9201-9017”
# print(kart[10:].rjust(19,'*'))

# #2 15 ədədinin 4-ə bölünməsindən çıxan qalığın kubunu tapın
# print(pow(15 % 4,3))

# #3 256.91872 ədədinin nöqtədən sonrakı və əvvəlki 2-ci ədədə qədər yuvarlaqlaşdırın. (2 fərqli cavab almalısınız)
# print(round(256.91872,2))
# print(round(256.91872,-2))

# #4 34 ədədinin əvvəlinə string metodlarının köməyilə 3 sıfır əlavə edin
# print(str(34).rjust(5,'0'))

# #5 Verilen floatın tam hissəsinin neçə ədəddən ibarət olduğunu göstərən program hazırlayın. Bunun üçün input və print funksiyalarından istifadə edin.
# x=input()
# print(len(str(int(float(x)))))

# #6 Verilen websaytın əvvəlindəki https:// və sonundakı .com hissələrini silən və istifadəçiyə göstərən program hazırlayın. 
#  z=input()
#  print(z.removeprefix('https://').removesuffix('.com'))

# #7 İstifadəçinin girdiyi ədədin həm 7 həm 3 həm də 8-ə eyni anda bölünüb bölünmədiyini istifadəçiyə bildirən kod yazın.

# x = int(input())
# if x % 3 == 0 and x % 7 == 0 and x % 8 == 0 : 
#     print('bolunur')
# else : 
#     print('bolunmur')



# 1. İstifadəçinin şifrəsinin düzgün olub olmadığını yoxlayan kod yazın. Şifrə aşağıdakı qaydalara uymaldır. Əgər uymazsa istifadəçiyə səhvini print edərək bildirin:
#     1. Ən az 8 ən çox 40 characterdən ibarət olmalıdır
#     2. Ancaq ingilis sriflərindən ibarət olmalıdır
#     3. Ancaq hərf və rəqəmlərdən ibarət olmalıdır
#     4. Mütləq şəkildə ən az bir böyük və bir kiçik hərf olmalıdır
#     5. Mütləq şəkildə ən az 1 hərf və ən az 1 rəqəm olmalıdır

# x = input('Sifreni daxil edin')

if len(x) <= 8 :
    print('sifre sayisi yeterli deyil')
elif len(x) >= 40 :
     print('sifre sayisi coxdur')
elif x.isascii() == False :  
    print('ingilis sriftlərindən ibarət olmalidir')
elif x.isalnum() == False : 
    print('reqemlerden ibaret olmalidir')
elif x.isupper() or x.isnumeric():
    print('1 kicik herf olmalidirliv')




    

metn = input('metni daxil edin:')
metn2 = input('neyi deyismek istirsen:')
metn3 = input('neye deyishmek isteyirsen:')
print(metn.replace(metn2,metn3))