#0,1,1,2,3,5,8,13,21,34

def fb(num):
    x=0
    y=1
    for i in range(num):
        print(x)
        print(y)
        x=x+y
        y=y+x
        yield x
        yield y

f=fb(10)
print(next(f))
print(next(f))
#for i in f:
#    print(i)
