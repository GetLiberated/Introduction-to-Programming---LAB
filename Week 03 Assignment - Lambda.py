# x=lambda a:a*10
# print(x(5))
#
# ex=[1,2,3,4,5]
# x=lambda a:a[-1]
# print(x(ex))
#
# ex={'a':1,'b':2}
# x=lambda a:a['a']
# print(x(ex))
#
# def a(b):
#     return lambda a:a*b
# b=a(2)
# print(b(3))
#
# def a(d):
#     return lambda a,b,c:a+b+c+d
# b=a(2)
# print(b(3,4,5))

#### LAMBDA CALCULATOR ####

stack=[]
x=True
while x is True:

    num=input()
    stack.extend(num)

    if num=='q':
        break

    a=int(stack.pop())
    op=stack.pop()
    b=int(stack.pop())

    plus = lambda a,b: a+b
    minus = lambda a,b: a-b
    kali = lambda a,b: a*b
    bagi = lambda a,b: b/a

    if op=='+':
        print('=',plus(a,b))
        stack.append(plus(a,b))
    if op=='-':
        print('=',minus(a,b))
        stack.append(minus(a,b))
    if op=='*':
        print('=',kali(a,b))
        stack.append(kali(a,b))
    if op=='/':
        print('=',bagi(a,b))
        stack.append(bagi(a,b))
