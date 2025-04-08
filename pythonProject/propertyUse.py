class Person(object):
    def __init__(self):
        self.age=0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,new_age):
        self.__age=new_age

p=Person()
#age=p.age
print(p.age)
p.age=47
print(p.age)