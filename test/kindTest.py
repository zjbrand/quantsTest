str1='aa'
str2='bb'

list1=[1,2]
list2=[10,20]

t1=(1,2)
t2=(10,20)

dict1={'name':'python'}
dict2={'age':30}

# #+:合并
# print(str1+str2)#aabb
# print(list1+list2)#[1, 2, 10, 20]
# print(t1+t2)#(1, 2, 10, 20)
#print(dict1+dict2)#報錯，字典不支持

#*:複製
# print(str1*5)
# print('-'*10)
# print(list1*5)
# print(t1*5)

str3='abcdefg'
list3=[10,20,30,40,50]
t3=(10,20,30,40,50)
s3={10,20,30,40,50}
dict3={'name':'Tom','age':18}

# print(len(str3))#7
# print(len(list3))#5
# print(len(t3))#5
# print(len(dict3))#2

# del str3
# print(str3)#報錯

# del list3
# print(list3)#報錯

# print(list3)
# del list3[1]
# print(list3)

# print(max(str3))#g
# print(max(t3))#50
# print(max(list3))#50
# print(min(list3))#10

#print(range(1,10,1))#range(1, 10)

# for i in range(1,10,1):
#     print(i)
#
# for i in range(1,10,1):
#     print(i)
# for i in range(1,10,2):
#     print(i)
#
# for i in range(10):#可以省略開始和步長，不能省略結束
#     print(i)


#enumerate返回值是元組，生成索引和原來數據
list4=['a','b','c','d','e']
# for i in enumerate(list4):
#     print(i)

# for i in enumerate(list4,start=1):#索引從1開始
#     print(i)

#tuple():轉換為元組
print(tuple(list3))#(10, 20, 30, 40, 50)
print(tuple(s3))

#list():轉換為集合
print(list(t3))#[10, 20, 30, 40, 50]
print(list(s3))

#set():轉化為集合
print(set(t3))#重複的數據會消失
print(set(list3))














