# import time
# for i in range(10,-1,-1):
#     print(i)
#     time.sleep(1)
# print('bitdi')

# import os
# import shutil
# os.mkdir('newfolder')
# os.chdir('newfolder')
# os.mkdir('ders1.txt')
# os.mkdir('ders2.txt')
# os.rename('newfolder/ders2.txt','newfolder/python notlar')
# os.makedirs('./python/general/python')
# shutil.move('./newfolder/python notlar','./python')
# shutil.copyfile('./python','/Users/macbook/Desktop/python')
# shutil.rmtree('newfolder')

import json
users = '[{"device": "iphone", "price": 3000, "count": null}, {"device": "samsung", "price": 2500, "count": 3},{"device": "xiaomi", "price": 2100, "count": null},{"device": "nokia", "price": 1800, "count": 4}]'

data = json.loads(users)
result = 0
for i in data:
    if not i.get('count') == None:
        result += i.get('price')
print(result)
