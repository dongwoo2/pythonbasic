class Person:
    def __init__(self, name = '', age = 0):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f'person[name = {self.name}, age = {self.age}]'
    
#Person 객체 사용하기
    
p1 = Person()
p1.name = '김동우'
p1.age = 25

p2 = Person('jason', 27)
print(type(p1))
print(p1)
print(p2)
print()


class PersonManager:
    def __init__(self, size = 5):
        self.size = size
        self.pl = {}
        self.no = 0

    def insert(self,ps): 
        if len(self.pl) == self.size:
            return
        if isinstance(ps, Person): #ps가 Person객체로 만들어졌는지 확인 맞으면 true 틀리면 false
            self.pl.__setitem__(self.no, ps)
            self.no += 1

    def select(self, no):
        return self.pl.get(no)
    

    def sorted(self):
        return sorted(self.pl.items(), key = lambda x:x[1].name, reverse=True)


pm = PersonManager(10)

pm.insert(Person('이순신',20))
pm.insert(Person('홍길동',30))
pm.insert(Person('임꺽정',15))
pm.insert(Person('세종대왕',24))
pm.insert(Person('장보고',27))
pm.insert(Person('김구',10))

print(pm.select(0))
for no in range(0,10):
    if no != None:
        print(pm.select(no))

print(pm.pl.keys())

for ps in pm.sorted():
    print(ps[1])
