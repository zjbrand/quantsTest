#1.今年我的年齡是嵗
#2.我的名字是
#3.我的體重是公斤
#4.我的學號是001
#5.我的名字是，明年是嵗 今年嵗
#6.

age=18
name='Tom'
weight=75.5
stu_id=1
stu_id2=1000

print('今年我的年齡是%d嵗'%age)
print('我的名字是%s'%name)
print('我的體重是%.2f公斤'%weight)#百分號后代表保存的位數
print('我的學號是%d'%stu_id)
print('我的學號是%03d'%stu_id)
print('我的學號是%03d'%stu_id2)
print("我的名字是%s，今年嵗%d"%(name,age))
print("我的名字是%s，明年嵗%d，體重%0.2f，學號是%06d"%(name,age+1,weight,stu_id))
print("我的名字是%s，今年%s嵗，體重%s公斤，學號是%06d"%(name,age,weight,stu_id))

print(f'我的名字是{name}，今年{age}嵗')


