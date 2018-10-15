import sys

class Hotel:
    def __init__(self):
        # initialize room
        self.room = []

        # set room category prices
        self.room_price1 = 500000
        self.room_price2 = 1000000

        # initialize revenue
        self.revenue = 0

    # check occupied rooms
    def check_room(self):

        # show total of occupied room
        print('\nCurrent room:\n',len(self.room),'Room occupied\n')
        print('Occupied room numbers:')

        # show every occupied rooms
        for bed in self.room:
            print(bed)
        print('\n')

    # check revenue
    def check_revenue(self):
        print('\nRevenue: Rp.',self.revenue,'\n')

    # menu
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

# customer class inheritance with hotel class
class Customer(Hotel):

    # check in
    def check_in(self):

        # choose room category
        print('\nChoose room category:\n1. Cheap\n2. Expensive')
        usr2 = input('> ')

        # cheap
        if usr2 == '1':

            # enter room number, you are the operator, you know all the room numbers, you have to, you don't need a list of room numbers
            room = int(input('\nEnter room number: '))

            # if you enter the room number that's already occupied
            if room in self.room:
                print('\nSorry, room number',room,'is already occupied.\n')

            # if not then add it
            else:
                self.room.append(room)
                self.revenue += self.room_price1
                print('\nYou payed Rp. 500.000\nEnjoy your stay!\n')

        # expensive
        elif usr2 == '2':

            # enter room number, you are the operator, you know all the room numbers, you have to, you don't need a list of room numbers
            room = int(input('\nEnter room number: '))

            # if you enter the room number that's already occupied
            if room in self.room:
                print('\nSorry, room number',room,'is already occupied.\n')

            # if not then add it
            else:
                self.room.append(room)
                self.revenue += self.room_price2
                print('\nYou payed Rp. 1.000.000\nEnjoy your stay!\n')

    # check out
    def check_out(self):

        # show every occupied rooms
        print('\nChoose room number:')
        for bed in self.room:
            print(bed)

        # choose room to check out
        room = int(input('> '))

        # if room is occupied
        if room in self.room:
            self.room.remove(room)
            print('\nThank you for staying in Ritz-Carlton Hotel!\n')

        # if not
        else:
            print('\nSorry, can\'t check out room number',room,', it is empty right now.\n')

c = Customer()
c.menu()
