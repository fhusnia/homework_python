# userData = [
#     {
#         'debt': 12543,
#         'payed': 341.346742,
#         'payed_percent': 0.027214122777644904,
#         'card_number': '5326-6644-1234-6432',
#         'first_name': 'Akif',
#         'last_name': 'Serifov',
#         'father_name': 'Elekber',
#     }
# ]
# Hormetli A. E. Serifov, sizin 5326-6644********** nomreli
# kredit kartiniza 341.35AZN odenis edildi.
# Umumi 12,543AZN teskil eden borcunuzdan 2.72% borc silinmisdir!

# text = 'Hormetli {user[first_name]:.<2.1} {user[father_name]:.<2.1} {user[last_name]:,<8.7} sizin {user[card_number]:*<18.8} nomreli kredit kartiniza {user[payed]:.2f}AZN odenish edildi.Umumi {user[debt]:,}AZN teskil eden borcunuzdan {user[payed_percent]:.2%} borc silinmisdir!'.format(user=userData[0])
# print(text)

# n1 = 15 və n2 = 13. Başqa bir variable yaratmadan aşağıdakı sual işarələrini doludurun.
# n1 = 15 
# n2 = 13
# print('%s + %s = %s' % (n1,n2,n1+n2))

#3
# number = range(0,30)
# for a in number:
#     print('{0:0}  {0:b}  {0:o}  {0:x}'.format(a))

def reverse(*arg):
    for a in arg:
        return a[::-1]
print(reverse(12,13))