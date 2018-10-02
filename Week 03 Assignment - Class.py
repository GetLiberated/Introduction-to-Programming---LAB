# Muhammad Erizky Suryaputra
# 2201797052

#### CLASS CALCULATOR ####
# For this method, You must input the number like this: 1+1 *ENTER*
# You can't input like this: 1 *ENTER* + *ENTER* 1
# After getting the result, you can input again like this: +1 *ENTER*

stack=[] # Create List.
x=True
while x is True: # Create infinite loop.

    num=input() # Input.
    stack.extend(num) # Slice string that you input into stack as individual strings. ex: '1+1' -> '1','+','1'

    if num=='q': # Enter q to stop.
        break

    a=int(stack.pop()) # Create variable 'a' : Take the string you input as integer (In this case number)
    op=stack.pop() # Create variable 'op' : Take another one as string (In this case operator)
    b=int(stack.pop()) # Create variable 'b' : And another as integer (In this case number)

    class Calculator: # Create Class.
        def __init__(self,one,two): # Initialize parameter
            self.number = one
            self.number0 = two

        def plus(self): # Module for plus
            print('=',self.number + self.number0)
            stack.append(self.number + self.number0)

        def minus(self): # Module for minus
            print('=',self.number - self.number0)
            stack.append(self.number - self.number0)

        def kali(self): # Module for times
            print('=',self.number * self.number0)
            stack.append(self.number * self.number0)

        def bagi(self): # Module for obelus
            print('=',self.number0 / self.number)
            stack.append(self.number0 / self.number)

    calculator = Calculator(a,b) # assign class as 'calculator' and also 'a' & 'b' as the parameter
    if op=='+': # if 'op' is '+', do dis module from inside the Calculator class.
        calculator.plus()
    if op=='-': # self explainatory, just like above
        calculator.minus()
    if op=='*': # are you even still asking what's this?
        calculator.kali()
    if op=='/': # bruh
        calculator.bagi()
