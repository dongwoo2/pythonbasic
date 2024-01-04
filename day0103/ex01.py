# mutable (변경 가능한) 
# 리스트는 글로벌 값이 바뀜
def func(a):
    a[0] = 'HELLO'

a = ['hello', 'hi']
print(a)
func(a)
print(a)