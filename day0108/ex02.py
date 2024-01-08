class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        print('x getter 호출')
        return self.__x
    
    @property
    def y(self):
        print('y getter 호출')
        return self.__y
    
    @x.setter
    def x(self, x):
        print('x setter 호출')
        self.__x = x
        
    @y.setter
    def y(self, y):
        print('y setter 호출')
        self.__y = y


p1 = Point(10,20)
print(p1.x,p1.y) # 직접 접근하듯 사용. 실제로 x() 함수 호출
p1.x = 100 # 속성에 직접 접근하듯 사용. 실제로 x(100)함수 호출
p1.y = 200
print(p1.x,p1.y)
