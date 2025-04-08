name_list=['Tom','Lily','Rose']
# print(name_list)
# print(name_list[0])
# print(name_list[1])
# print(name_list[2])

#len()適用於任何函數
# print(name_list.index('Tom'))#找不到會報錯
# print(name_list.count('Tom'))#出現的次數
# print(name_list.count('Tom1'))#沒有的話返回0
# print(len(name_list))#3，統計列表中有多少數據

#in 和not in 也是公共文句
# print('Lily' in name_list)#true,是否在列表中
# print('Lilys' in name_list)#true,是否不在列表中,可以用於判斷郵箱是否在其中
#
# print('Lily' not in name_list)#false,是否在列表中
# print('Lilys' not in name_list)#true,是否不在列表中

#查找是否列表中有該字符串，有則不能注冊
# name=input('請輸入您的賬號：')
#
# if name in name_list:
# # 提示用戶名已經存在
#     print(f'您輸入的名字{name},此用戶名已經存在！')
# else:
# # 提示可以注冊
#     print(f'您輸入的名字{name},此用戶可以注冊')

# name_list.append('John')#追加字符串到結尾
# print(name_list)#列表數據改變，是可變類型
# name_list.append(['Sam','Smith'])#追加整個數列到結尾
# print(name_list)

# name_list.extend('xiaoming')#拆開為每個字符，加入列表
# print(name_list)

# name_list.extend(['xiaoming','xiaohong'])#如果是序列，拆開加入到列表結尾
# print(name_list)

# name_list.insert(1,'xiaoming')#加到指定位置
# print(name_list)

# del name_list
# print(name_list)
# del(name_list)
# print(name_list)
#del也可刪除指定位置的字符串
# del name_list[0]
# print(name_list)

#pop()刪除指定位置的字符串，不指定刪除最後一個,返回刪除字符串
# del_name=name_list.pop()
# print(name_list)#不指定：['Tom', 'Lily']
# print(del_name)#Rose

# name_list.remove('Rose')#如果有相同，刪除第一個
# print(name_list)

# name_list.clear()
# print(name_list)

# name_list[0]='aaa'
# print(name_list)

# name_list.reverse()#倒敘排列
# print(name_list)

# name_list.sort()#默認升序排序
# print(name_list)

# name_list.sort(reverse=True)#降序排序
# print(name_list)

# name_list1=name_list.copy()#現場要保留原來數據，再進行修改，因而copy()常用
# print(name_list1)

list1=[]
i=0
while i<10:
    list1.append(i)
    i+=1
print(list1)

list2=[]
for du in range(10):
    list2.append(du)
print(list2)

#列表推導式
list3=[dedu for dedu in range(0,10,2) ]
print(list3)

list4=[]
for deduc in range(10):
    if deduc%2==0:
        list4.append(deduc)
print(list4)

list5=[deduc1 for deduc1 in range(10) if deduc1%2==0]
print(list5)

list6=[(d,k) for d in range(1,3) for k in range(3)]
print(list6)

dic1={ii:ii**2 for ii in range(1,5)}
print(dic1)

list7=['name','age','gender']
list8=['Tom',20,'man']
dic2={list7[iii]:list8[iii] for iii in range(len(list7))}
print(dic2)
#如果兩個列表長度相同，如果個數不同，應按個數少的來計算len,否則報錯

counts={'MBP':268,'HP':125,'DELL':201,'Lenovo':199,'acer':99}
count1={key: value for key,value in counts.items() if value>=200}
print(count1)

list9=[1,1,2]
set1={ds**2 for ds in list9}
print(set1)#集合去重










