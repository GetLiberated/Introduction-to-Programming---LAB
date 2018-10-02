# Muhammad Erizky Suryaputra
# 2201797052

#### LAMBDA CALCULATOR ####
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

    a=int(stack.pop()) # Create variable 'a' : Take the string from the stack that you input as integer (In this case number)
    op=stack.pop() # Create variable 'op' : Take another one as string (In this case operator)
    b=int(stack.pop()) # Create variable 'b' : And another as integer (In this case number)

    plus = lambda a,b: a+b # Plus lambda
    minus = lambda a,b: a-b # Minus lambda
    kali = lambda a,b: a*b # Times lambda
    bagi = lambda a,b: b/a # Obelus lambda

    if op=='+': # If 'op' is '+' then print '=' and Plus lambda with parameter of 'a' and 'b'
        print('=',plus(a,b))
        stack.append(plus(a,b))
    if op=='-': # If 'op' is '-' then print '=' and Minus lambda with parameter of 'a' and 'b'
        print('=',minus(a,b))
        stack.append(minus(a,b))
    if op=='*': # If 'op' is '*' then print '=' and Times lambda with parameter of 'a' and 'b'
        print('=',kali(a,b))
        stack.append(kali(a,b))
    if op=='/': # If 'op' is '/' then print '=' and Obelus lambda with parameter of 'a' and 'b'
        print('=',bagi(a,b))
        stack.append(bagi(a,b))
