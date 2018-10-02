# class Test:
#     def fun(self):
#         print('Hello')
#
# obj = Test()
# obj.fun()
#
# # You can't call out class, you must assign it into a variable.
# # You can't call out module inside the class
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print('Hello, my name is', self.name, "and im", self.age)
#
#
# p = Person('Shwetanshu', "18")
# p.say_hi()
#
# me = Person('Eris',18)
# me.say_hi()

#### Class Calculator ####

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

    class Calculator:
        def __init__(self,a,b):
            self.number = a
            self.number0 = b

        def plus(self):
            print('=',self.number + self.number0)
            stack.append(self.number + self.number0)

        def minus(self):
            print('=',self.number - self.number0)
            stack.append(self.number - self.number0)

        def kali(self):
            print('=',self.number * self.number0)
            stack.append(self.number * self.number0)

        def bagi(self):
            print('=',self.number0 / self.number)
            stack.append(self.number0 / self.number)

    calculator = Calculator(a,b)
    if op=='+':
        calculator.plus()
    if op=='-':
        calculator.minus()
    if op=='*':
        calculator.kali()
    if op=='/':
        calculator.bagi()
