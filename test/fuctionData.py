# def sel_func():
#     print('顯示餘額')
#     print('存款')
#     print('取款')
#
# print('恭喜您登錄成功')
# sel_func()
#
# print('您的餘額是100000')
# sel_func()
#
# print('取了1000元')
# sel_func()

# def add_num(a,b):
#     num=a+b
#     print(num)
#
# add_num(10,30)

#reture作用一是返回值，二是中斷函數執行

def add_num1(a,b):
    """
    求和函數
    :param a: 參數1
    :param b: 參數2
    :return:
    """
    return a+b

result=add_num1(5,6)
print(result)

#help函數的作用：查看函數的説明文檔，如：help(len)
help(add_num1)

def print_line():
    print('-'*20)

def print_lines(num):
    i=0
    while i<num:
        print_line()
        i+=1

print_lines(2)

def average_num(a,b,c):#形參
    return (a+b+c)/3

ave=average_num(10,20,30)#實參
print(ave)

#global可改局部變量為全局變量
def return_num():
    return 1,2

result=return_num()
print(result)#一個函數，多個返回值，返回為元組類型，可以return後面跟列表，字典

# def user_info(name,age,gender):
#     print(f'您的名字是{name}，年齡是{age}，性別是{gender}')
#
# user_info('Jimmy',20,'男')#位置參數個數和次序必須一直
#
# user_info(gender='女',name='Rose',age=16)#采用了關鍵字參數，次序可以變化

# def user_info(name,age,gender='男'):#默認值為男，要放在最後
#     print(f'您的名字是{name}，年齡是{age}，性別是{gender}')
# user_info('Jimmy',20,'女')#修改默認參數，您的名字是Jimmy，年齡是20，性別是女
# user_info('Jimmy',20)#缺省情況下，使用默認參數

# def user_info(*args):#返回都是元組，包裹位置傳遞
#     print(args)
# user_info('Tom')
# user_info('Tom',18)
# user_info('Tom',18,'man')#參數個數不指定
#
# #包裹關鍵字傳遞，收集所有關鍵字參數，返回一個字典型
# def user_info1(**kwargs):
#     print(kwargs)
# user_info1()
# user_info1(name='Tom')
# user_info1(name='Tom',age=20)

# def return_num():
#     return 100,200
# #result=return_num()
# num1,num2=return_num()
# print(num1)
# print(num2)#實現了元組的拆包


# dict1={'name':'Tom','age':18}
# a,b=dict1
# print(a)
# print(b)
#
# print(dict1[a])
# print(dict1[b])#用key值來獲取value值


aa,bb=1,2
aa,bb=bb,aa
print(aa)
print(bb)#實現了變量的交換
print('-'*20)

a=1
b=a
print(b)
print(id(a))
print(id(b))#返回在内存中的地址

#可變類型，在原數據上修改内容：列表、字典、集合
#不可變類型不能在原數據上修改内容：整型、浮點型、字符串、元組







