#set()集合有去重的作用
s1={10,20,30,40,50}#集合沒有順序，也就沒有索引
# print(s1)
#
# s2={10,20,30,40,60,30,40}
# print(s2)#有去重的功能
#
# s3=set('abcdefg')
# print(s3)#{'f', 'd', 'e', 'g', 'b', 'c', 'a'}
#
# s4=set()
# print(s4)
# print(type(s4))#<class 'set'>
#
# s5={}
# print(type(s5))#<class 'dict'>

# s1.add(100)#增加單一數據,集合是可變類型，可能加到任何位置
# print(s1)
# s1.add(100)
# print(s1)#有去重功能
#
# s1.add([10,20,30])
# print(s1)#報錯，只能增加一個數據

# s1.update([10,20,30,50,70])#只能追加序列，追加單個數據報錯
# print(s1)#{50, 20, 70, 40, 10, 30},10,20,30沒有添加，去重功能

# s1.remove(10)#刪除指定數據，如果沒有則報錯
# s1.remove(10)#報錯
# print(s1)

# s1.discard(20)
# s1.discard(20)#刪除，沒有也不報錯
# print(s1)

# del_num=s1.pop()#隨機刪除一個數據，並返回這個數據
# print(del_num)
# print(s1)

print(10 in s1)#True
print(10 not in s1)#False















