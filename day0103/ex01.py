# mutable (변경 가능한) 

def func(a):
    a[0] = 'HELLO'

a = ['hello', 'hi']
print(a)
func(a)
print(a)