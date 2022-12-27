# farm = ('inek', 'keci', 'at', 'at', 'at', 'keci', 'at', 'qoyun', 'at', 'keci', 'at', 'toyuq', 'inek', 'keci', 'at', 'toyuq', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'qoyun', 'keci', 'keci', 'qoyun', 'at', 'qoyun', 'inek', 'at', 'keci', 'qoyun', 'inek', 'keci', 'qoyun', 'inek', 'toyuq', 'at', 'toyuq', 'keci', 'inek', 'toyuq', 'at', 'toyuq', 'at', 'keci', 'qoyun', 'keci', 'keci', 'inek')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}
# animal = input('Ferma admin paneline xos geldiniz. Axtardiginiz heyvani daxil edin: ')

# text ="""
# Axtarilan Heyvan: {}
# {}
# Fermadaki {} sayi: {}
# Diger heyvanlara olan faizi: {}%
# {} umumi qiymeti:{}AZN
# """.format(
#     animal, 
#     '-' * 20,
#     animal,
#     farm.count(animal),
#     str((farm.count(animal) / len(farm))*100),
#     animal,
#     str(qiymetler[animal] * farm.count(animal))
# )
# print(text)


# l = [10, -21, 46, 73, -35, -31, 71, 36, -92, -53, -34, -18, -78, 54, -49, 2, 62, 25, 14, 8, 63, 84, -83, 40, 90, 57, -15, -7, 35, 78] 


# nov = { eded: ('menfi' if eded < 0 else 'musbet') for eded in l   }


# print(nov)

cumle = "sehifelerden en yaxsi sehife bu sehifedir"
l = ["sehife", "sehve"]



print(cumle.replace(*l))