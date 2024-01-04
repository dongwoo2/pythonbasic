#immutable(변경 불가능한) - 기본자료형
def func(a):
    print('func2 :', id(a)) #지금 a는 글로벌 a를 바라보고 있음
    a = 'HELLO' # 하지만 여기서 a는 'HELLO' 객체를 바라봄
    print('func3 :', id(a)) # 그렇기에 바라보는 객체의 id값이 달라짐
    print('func :', a) 

a = 'hello'
print('global1:', id(a))
print(a)
func(a)
print(a)
print('global:4', id(a))


