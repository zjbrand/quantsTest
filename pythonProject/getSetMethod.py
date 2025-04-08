class Person(object):

    def __init__(self):
        self.age=0

    def get_age(self):
        return self.__age

    def set_age(self,new_age):
        if new_age>150:
            print("年龄错误")
        else:
            self.__age=new_age

    age=property(get_age,set_age)

p=Person()
print(p.age)
p.age=120
print(p.age)

