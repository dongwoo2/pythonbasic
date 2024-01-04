#immutable(변경 불가능한) - 튜플 자료형
def func(a):
    #a[0] = 'HELLO' # 요소 변경 불가!! 요소는 절대 변경못함 (튜플 요소 변경 시 Error!)
    a = (1,2,3)
    print('func:',a)

a = ('hello','hi')
#a = 'hi' 이렇게 객체를 아예 바꿀수는 있음
print(a)
func(a)
print(a)