class Point:
    def __init__(self) : # 디폴트 생성자
        self.x = 0
        self.y = 0
        pass

    def prt(self):
        print(f'[{self.x},{self.y}]')

p = Point() # 객체 생성( __init__() 호출)
p.x = 10
p.y = 10
p.prt
