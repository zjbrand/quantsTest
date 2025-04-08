#tuple數據是不能修改的,比如身份証號
# t1=(10,20,30)#如果只有一個數據：t1=(10,)
# print(t1)
# print(type(t1))
#
# t2=(10,)
# print(type(t2))
#
# t3=(10)
# print(type(t3))#int
#
# t4=('aaa')
# print(type(t4))#str
#
# t5=('aaa',)
# print(type(t5))#tuple

#元組只支持查找數據
tuple1=('aa','bb','cc','bb')
# print(tuple1[0])#aa
# print(tuple1.index('bb'))#1
# #print(tuple1.index('bbb'))#報錯
# print(tuple1.count('bb'))#2
# print(tuple1.count('bbb'))#0
# print(len(tuple1))#4

#tuple1[0]='aaa'#報錯
tuple2=('aa','bb',['cc','bb'])
print(tuple2[2])
print(tuple2[2][0])
tuple2[2][0]='Tom'#元組中的列表是可以修改的
print(tuple2)




