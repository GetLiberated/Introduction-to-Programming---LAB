lebar=int(input("Enter number of rows: "))
for y in range(0,lebar):
    for x in range(0,y+1):
        print('*', end=" ")
    print()
print()

for y in range(0, lebar):
    for x in range(0,lebar-y):
        print(end=" ")
    for x in range(0,y+1):
        print('*',end='')
    print()
print()

for y in range(0,lebar+1):
    for x in range(0,lebar-y):
        print('*', end=" ")
    print()
print()

for y in range(0, lebar):
    for x in range(0,lebar+y):
        print(end=" ")
    for x in range(0,lebar-y):
        print('*',end='')
    print()
print()

for y in range(0,lebar):
    for x in range(0,lebar-y):
        print(end=" ")
    for x in range(0,y):
        print('*', end=" ")
    print()
print()

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
