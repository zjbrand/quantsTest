#遞歸是函數自己調用自己，必須要有出口，防止出現死循環

# def return_num():
#     return 100
#
# result=return_num()
# print(result)

#3以内數字纍加和
def sum_numbers(num):
    if num==1:
        return 1
    #如果取消出口，那麽報錯如下： [Previous line repeated 996 more times]
    #RecursionError: maximum recursion depth exceeded---遞歸深度一般計算機在990~1000之間，所以不像死循環一樣無數次循環
    return num+sum_numbers(num-1)

result=sum_numbers(3)
print(result)

#lambda表達式，也叫匿名表達式，作用是簡化代碼，對計算機節省内存，對程序員節省精力
#lambda可以進入多個參數，但返回值只有一個.lambda 參數列表（可以不要）：返回值
def fn1():
    return 200
print(fn1) #<function fn1 at 0x000001C9A4BB85E0>
print(fn1())#200

fn2=lambda:100#lambda是匿名函數，因而賦值對象雖然不帶（ ）但也是函數
print(fn2)#<function <lambda> at 0x000001BC70488900>
print(fn2())#拿到了返回值100

def add(a,b):
    return a+b

result=add(1,3)
print(result)

fn3=lambda a,b:a+b
print(fn3(1,2))

#lambda可以沒參數，一個參數，可變參數
ft1=lambda a:a
print(ft1("Hello world!"))

#默認參數，缺省參數
ft2=lambda a,b,c=100:a+b+c
print(ft2(10,20))#130
print(ft2(10,20,200))#230,默認參數可以被取代

#可變參數：*args,返回元組型
ft3=lambda *args:args
print(ft3(10,20,30))#(10, 20, 30)
print(ft3(10,20))#(10, 20)
print(ft3(10))#(10,)

#可變參數：**kwargs，接受不定長參數，返回的是字典
ft4=lambda **kwargs:kwargs#這裏用什麽名字都可以，只是要加兩個**，返回的是字典型
print(ft4(name='python',age=20,gender='男'))

#帶判斷的lambda
fc=lambda a,b:a if a>b else b
print(fc(1000,500))



