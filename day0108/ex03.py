class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y

    
    def setX(self,x):
        self.__x = x
    
  
    def setY(self,y):
        self.__y = y
    

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

p1 = Point(10,20)
print(p1.getX(),p1.getY())
p1.setX = 100 
p1.setY = 200
print(p1.getX(),p1.getY())
