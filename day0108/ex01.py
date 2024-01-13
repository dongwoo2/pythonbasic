class Person:
    def __init(self, name = None, age = 0):
        self.__name = name
        self.__age = age

    def printInfo(self):
        print(self.__name, self.__age)


    def main():
        p1 = Person('홍길동',20)
        print(p1.__dict__)
        print(dir(p1))
        p1.__dict__['age']
        p1.__dict__['__age'] = 40
        print(p1.__age)

        p1.printInfo
        print(p1.age)
        print(dir(p1))
