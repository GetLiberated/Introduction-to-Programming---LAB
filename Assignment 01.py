lebar=int(input("Enter number of rows: ")) # This is where you input the number

#Triangle 1
for y in range(0,lebar): # The range of Y axis from 0 to total number of the rows you entered.
    for x in range(0,y+1): # The range of X axis from 0 to total number of y plus 1.
        print('*', end=" ") # Print asteriskt then space within the X range.
    print() # Print a new line after each asterisk and space printed.
print() # Print a new line to seperate this triangle with below triangle.

#Triangle 2
for y in range(0, lebar): # The range of Y axis from 0 to total number of the rows you entered.
    for x in range(0,lebar-y): # The range of X axis from 0 to total number of the rows you entered minus the Y range.
        print(end=" ")
    for x in range(0,y+1):
        print('*',end='')
    print()
print()

#Triangle 3
for y in range(0,lebar+1):
    for x in range(0,lebar-y):
        print('*', end=" ")
    print()
print()

#Triangle 4
for y in range(0, lebar):
    for x in range(0,lebar+y):
        print(end=" ")
    for x in range(0,lebar-y):
        print('*',end='')
    print()
print()

#Triangle 5
for y in range(0,lebar):
    for x in range(0,lebar-y):
        print(end=" ")
    for x in range(0,y):
        print('*', end=" ")
    print()
print()

#Triangle 6
for y in range(0, lebar):
    for x in range(0,lebar-y):
        print(end=" ")
    for x in range(0,y):
        print('*', end=" ")
    print()

for y in range(0, lebar):
    for x in range(0,y):
        print(end=" ")
    for x in range(0,lebar-y):
        print('*',end=' ')
    print()
