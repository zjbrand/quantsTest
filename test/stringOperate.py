# str2 = 'firstTest'
# for i in str2:
#     if i=='e':
#         continue #退出當前循環
#     print(i)
"""
str3='abcdefgh'
print(str3[2:5:2])#切片：【首索引：結束索引）：步長（默認為1）
print(str3[::-1])#可以不選第一個默認為0，第二個為最後一個，步長為1;如果步長為負倒序，負數第一第二表示從面數向前推
#如果選取方向和步長的方向衝突，則無法選取數據，如：str3[-4:-1:-1],改爲str3[-1:-4:-1]則可以

mystr= "hello world and itcast and abcdef and Python"
print(mystr.find('and'))#12
print(mystr.find('and',15,30))#23
print(mystr.find('ands',15,30))#-1,ands不存在

print(mystr.index('and'))#12,返回起始位置
print(mystr.index('and',15,30))#23
#print(mystr.index('ands',15,30))#報錯

print(mystr.count('and',15,30))#1
print(mystr.count('and'))#3返回出現的次數
print(mystr.count('ands'))#0

print(mystr.rfind('and'))#34  從右邊開始找，找到第一個返回從左數的位置,rindex()
"""

mystr1= "hello world and it cast and abcdef and Python"
#new_str=mystr1.replace('and','he')#mystr1原有字符串不修改，必須要變量接收replace的返回值，字符串不可變類型
#new_str=mystr1.replace('and','he',10)#超過的次數，不報錯只會替換全部
#print(new_str)

#list1=mystr1.split('and')#用and來分割字符串，丟失分割字符
#list1=mystr1.split('and',2)#替代次數
#print(list1)

# mylist=['aa','bb','cc','dd']
# #aa...bb...cc...
# new_str='...'.join(mylist)#先放鏈接符號
# print(new_str)

# new_str=mystr1.capitalize()#字符串首字母變爲大寫
# print(new_str)

# new_str=mystr1.title()#字符串每個單詞首字母大寫
# print(new_str)
#
# new_Ustr=mystr1.upper()#所有字母變大寫
# print(new_Ustr)
#
# new_lstr=mystr1.lower()#所有字母轉小寫
# print(new_lstr)

# mystr2= "  hello world and it cast and abcdef and Python  "
# print(mystr2)#打印有空白字符
# new_str2=mystr2.lstrip()
# print(new_str2)
# new_str3=mystr2.rstrip()
# print(new_str3)
# new_str4=mystr2.strip()#刪除兩側空白字符
# print(new_str4)

#ljust()左對齊,rjust(),center()第二個可用字符填充，如：ljust(str,'.')
#startswith('',start,end),endswith()字符串中是否以某個字串開始、結束

# print(mystr1.startswith('hello'))
# print(mystr1.startswith('hel'))
# print(mystr1.startswith('hels'))

# print(mystr1.endswith('Python'))
# print(mystr1.endswith('python'))

#isalpha()是否都是字母
print(mystr1.isalpha())#false,因爲其中有空格
print(mystr1.isdigit())
mystrD='12344567'
print(mystrD.isdigit())

#isalnum() 數字或字母或組合
print(mystrD.isalnum())#True
print(mystr1.isalnum())#false 有空格

# isspace()都是空白才返回true
print(mystr1.isspace())#false
mystrEm="   "
print(mystrEm.isspace())#true







