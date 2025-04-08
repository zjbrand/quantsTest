#字典型用鍵值來查找，不要用索引，相當於用表頭來做鍵值，鍵值：key 數據:value,合成為鍵值對
dict1={'name':'Tom','age':20,'gender':'男'}
# print(dict1)
# print(type(dict1))

# dict2={}#dict()也可創建
# print(dict2)
# print(type(dict2))

#新增鍵值
dict1['id']=110
print(dict1)

dict1['name']='Rose'#不存在鍵值就新增，如果存在就更改
print(dict1)

# del(dict1)
# print(dict1)

# del dict1['name']
# print(dict1)
# dict1.clear()
# print(dict1)

# dict1['name']='Lily'#修改
# print(dict1)
# print(dict1['name'])
# print(dict1['id'])

# print(dict1.get('name'))
# print(dict1.get('names','Nana'))#Nana
# print(dict1.get('names'))#如果不存在返回none
# print(dict1.get('id'))
#
# #keys()
# print(dict1.keys())#dict_keys(['name', 'age', 'gender', 'id'])查找字典中所有的key,可以用for遍歷
#
# #values()
#
# print(dict1.values())#dict_values(['Rose', 20, '男', 110])查找字典中的所有value
#
# #items()
# print(dict1.items())#查找出所有鍵值對

# for key in dict1.keys():#遍歷key
#     print(key)


# for v in dict1.values():
#     print(v)

# for it in dict1.items():
#     print(it)

for k,v in dict1.items():
    print(f'{k}={v}')
print('-'*40)

students=[{'name':'Tom','age':20},{'name':'Rose','age':19},{'name':'Jack','age':22}]
students.sort(key=lambda x:x['name'])
print(students)
students.sort(key=lambda x:x['name'],reverse=True)
print(students)

