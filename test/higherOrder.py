#高階函數：把一個函數當作參數傳入另外一個函數

# #求絕對值
# num=abs(-10)
# print(num)#10
#
# #四捨五入,但是0.5是捨去的，0.51不捨，而是進位
# num1=round(1.2)
# print(num1)#1
# print(round(2.9))#3

#任意兩個數字求絕對值后求和
# def abs_add(a,b):
#     return abs(a)+abs(b)
#
# result=abs_add(-2,-4)
# print(result)

#高階函數，根據傳入參數來確定使用什麽樣的函數
def sum_num(a,b,f):
    return f(a)+f(b)

result=sum_num(-1,2,abs)#使用abs絕對值
print(result)

result1=sum_num(1.1,4.51,round)
print(result1)


#内置高階函數：map(),reduce()
#map(func,lst)參數1的func作用與參數2的lst
#計算list序列中的各個數字的2次方
list1=[1,2,3,4,5,6]

def func(x):
    return x**2

result=map(func,list1)
print(result)#顯示的是地址
print(list(result))#將該地址變爲列表

#reduce(func,lst)  func必須有兩個參數，func的計算結果繼續和序列下一個計算

import functools
list2=[1,2,3,4]

def func(a,b):
    return a*b #如果是a+b那麽，返回10

result=functools.reduce(func,list2)
print(result)#24

#filter(func.lst)函數用於過濾序列
list3=[1,2,3,4,5,6,7,8,9,10]
def func(x):
    return x%2==0

result=filter(func,list3)
print(result)
print(list(result))






