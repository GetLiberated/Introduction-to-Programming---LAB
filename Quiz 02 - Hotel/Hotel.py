import sys

class Hotel:
    def __init__(self):
        self.room = []
        self.room_price1 = 500000
        self.room_price2 = 1000000
        self.revenue = 0

    def check_room(self):
        print('\nCurrent room:\n',len(self.room),'Room occupied\n')
        print('Occupied room numbers:')
        for bed in self.room:
            print(bed)
        print('\n')

    def check_revenue(self):
        print('\nRevenue: Rp.',self.revenue,'\n')

    def menu(self):
        while True:
            usr = input('Welcome to Ritz-Carlton Hotel!\nWhat do you want to do?:\n1. Check In\n2. Check Out\n3. Check Room\n4. Check Revenue\n5. Exit\n> ')

            if usr == '1':
                c.check_in()

            elif usr == '2':
                c.check_out()

            elif usr == '3':
                c.check_room()

            elif usr == '4':
                c.check_revenue()

            elif usr == '5':
                sys.exit()


class Customer(Hotel):

    def check_in(self):
        print('\nChoose room category:\n1. Cheap\n2. Expensive')
        usr2 = input('> ')
        if usr2 == '1':
            room = int(input('\nEnter room number: '))
            if room in self.room:
                print('\nSorry, room number',room,'is already occupied.\n')
            else:
                self.room.append(room)
                self.revenue += self.room_price1
                print('\nYou payed Rp. 500.000\nEnjoy your stay!\n')

        elif usr2 == '2':
            room = int(input('\nEnter room number: '))
            if room in self.room:
                print('\nSorry, room number',room,'is already occupied.\n')
            else:
                self.room.append(room)
                self.revenue += self.room_price2
                print('\nYou payed Rp. 1.000.000\nEnjoy your stay!\n')

    def check_out(self):
        print('\nChoose room number:')
        for bed in self.room:
            print(bed)
        room = int(input('> '))
        if room in self.room:
            self.room.remove(room)
            print('\nThank you for staying in Ritz-Carlton Hotel!\n')
        else:
            print('\nSorry, can\'t check out room number',room+', it is occupied right now.\n')

c = Customer()
c.menu()
