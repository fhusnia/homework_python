#1**********
# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci']

#a----->

#print((ferma.index('keci')) + 1);


#b----->

# ferma.sort()
# print(ferma)

#c----->

# ferma.remove('at')
# ferma.append('toyuq')
# print(ferma)

#d----->

# ferma.insert(0,'keci')
# print(ferma)

#e----->
 
# del ferma[len(ferma)//2 : ]
# print(ferma)

#f---->

# ferma.extend(['at', 'qoyun', 'inek', 'inek', 'qoyun'])
# print(ferma)

#g---->

# print(ferma * 3)

#h---->

# ferma.reverse()
# print(ferma)

#i----->

# print((ferma.count('inek') / len(ferma)) * 100 )

#j----->

# copyfarm = ferma.copy()
# print(copyfarm)

#k------->

# ferma.clear()
# print(ferma)

#2*************

# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
 
# menfi = 0
# musbet = 0
# for i in numbers:
#     if i < 0:
#         menfi += i
#     elif i > 0:
#         musbet += i

# result.clear()
# result.insert(0,musbet)
# result.insert(1,menfi)
# print(result)

#3*************

# x = input()
# a = []
# for i in x:  
#     a.append(int(i))
# a.reverse()
# print(a)

#4*************

# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]

# numbers.sort()
# max = numbers.pop()
# min = numbers.pop(0)
# print(min,max)


# max_number = max(numbers)
# min_number = min(numbers)
# print(max_number)
# print(min_number)


#5**********
# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]

#a---->

# print(len(r))

#b----->

# result = 0
# count = 0
# for i in r:
#     result += i
#     count += 1
# print(result/count)

#c---->

# result = 0
# for i in r :
#     if(i < 51):
#         result += 1

# print((result * 100) / len(r) )

#d---->

# r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# result = 0
# for i in r :
#     if i > 80:
#      result += 1

# print( (result * 100) / len(r))


