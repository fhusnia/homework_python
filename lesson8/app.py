# Girilen stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# upunion('birlesmis', 'milletler', 'teskilati') => 'BMT'

# def upunion(*args):
#     result = ''
#     for i in args:
#         result += i[0].upper()
#     return result
# print(upunion('birlesmis', 'milletler', 'teskilati'))

# Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') => 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'

# def chstr(text,**kwargs):
#     for key,value in kwargs.items():
#         text = text.replace(key,value)
#     return text

# print(chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') )

# Birinci argument ilk qiyməti, ikinci argument isə yeni qiyməti göstərir. Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
# find_percent(200, 60) # output: qiymet 70% azalmisdir 
# find_percent(100, 150) # output: qiymet 50% artmisdir

# def find_percent(a,b):
#     if b < a:
#         result=round((-(b-a)/a)*100)
#         print(str(result) +  '%' + ' azalmisdir' )
#     elif b > a:
#         result=str(((b-a)/a)*100)
#         find2 = result.find('.')
#         print(result[:find2] + '%'+ ' artmisdir')
# find_percent(200, 60)

# Girilən listin ən böyük ədədindən ən kiçiyini çıxarıb, nəticə verən bir funksiya hazırlayın.
# big_dif_sml([6, 3, 8, 9, 2]) => 7 # en  boyuk 9, en kicik 2

# def big_dif_sml(*args):
#     for arg in args:
#         arg.sort()
#         print(arg[len(arg) - 1] - arg[0])
# big_dif_sml([6, 3, 8, 9, 2])

# def getReversedSum(*args):  
#     sum = 0
#     for arg in args:
#         sum += int(str(arg)[::-1])
#     return sum  
# print(getReversedSum(123, 567, 562))

# def ReversedNum(number):
#     son = []
#     for n in number:
#         result = str(n)[::-1]
#         son.append(result)
#     return son

# def getReversedSum(*args):
#     total = ReversedNum(args)
#     sum = 0
#     for  num in total:
#       sum += int(num)
#     return sum
# print(getReversedSum(123, 567, 562))

# üç rəqəmli ədədləri sözə çevirən bir funksiya hazırlayın. Örnək output:
# eded_cevir(658) => altı yüz əlli səkkiz

# yuzluk = {'1':'yuz','2':'iki yuz','3':'üç yuz','4':'dord yuz','5':'bes yuz','6':'alti yuz','7':'yeddi yuz','8':'sekkiz yuz','9':'doqquz yuz'}
# onluq = {'1':'on','2':'iyirmi','3':'otuz','4':'qirx','5':'elli','6':'altmish','7':'yetmish','8':'seksen','9':'doxsan'}
# teklik = {'1':'bir','2':'iki','3':'üç','4':'dord','5':'bes','6':'alti','7':'yeddi','8':'sekkiz','9':'doqquz'}

# def eded_cevir(number):
#     result=[]
#     for num in str(number):
#         result.append(num)
#     if  result[0] in yuzluk:
#         if result[1] in onluq:
#             if result[2] in teklik:
#                     return yuzluk[result[0]]  + ' ' + onluq[result[1]] + ' ' + teklik[result[2]]
# print(eded_cevir(958))

# Aşağıdakı düsturladan 10-unu seçib, lambda ile funksiyaya cevirin

# physic={
#     'F':lambda m,a: m * a,
#     'a':lambda v,t: v / t,
#     's':lambda a,t: (a * pow(t ,2)) // 2,
#     'Ep':lambda m,g,h: m * g * h,
#     'W':lambda F,s: F + s,
#     'Ek':lambda m,v: (m * pow(v,2)) // 2,
#     'Ew':lambda w,q: w + q,
#     'U':lambda w,q: w / q,
#     'l':lambda q,t: q / t,
#     'T':lambda l,f: l / f
# }
# print(physic.get('s')(2,4))

# Lambda ilə factorial hesablayan recursive function hazırlayın.

# factorial = lambda x: 1 if x == 1 else x * factorial(x-1)
# print(factorial(3))
