class TollGate:
    car_total = [0,0,0,0,0,0]
    bus_total = [0,0,0,0,0,0]
    truck_total = [0,0,0,0,0,0]
    car_revenue_total = [0,0,0,0,0,0]
    bus_revenue_total = [0,0,0,0,0,0]
    truck_revenue_total = [0,0,0,0,0,0]
    car_revenue_cashless_total = [0,0,0,0,0,0]
    bus_revenue_cashless_total = [0,0,0,0,0,0]
    truck_revenue_cashless_total = [0,0,0,0,0,0]

    def __init__(self):
        super(TollGate,self).__init__()
        self.car_price = 6000
        self.bus_price = 8000
        self.truck_price = 10000


class TollGate2:
    car_total2 = [0,0,0,0,0,0]
    bus_total2 = [0,0,0,0,0,0]
    truck_total2 = [0,0,0,0,0,0]
    car_revenue_total2 = [0,0,0,0,0,0]
    bus_revenue_total2 = [0,0,0,0,0,0]
    truck_revenue_total2 = [0,0,0,0,0,0]
    car_revenue_cashless_total2 = [0,0,0,0,0,0]
    bus_revenue_cashless_total2 = [0,0,0,0,0,0]
    truck_revenue_cashless_total2 = [0,0,0,0,0,0]

    def __init__(self):
        super(TollGate2,self).__init__()
        self.car_price2 = 18000
        self.bus_price2 = 20000
        self.truck_price2 = 25000


class Vehicle(TollGate,TollGate2):
    def __init__(self,a):
        super(Vehicle,self).__init__()
        self.tollboth = a

    def add(self,vehicle_type):

        if vehicle_type == 'car':
            self.car_total[self.tollboth] += 1
            self.car_revenue_total[self.tollboth] += self.car_price

        if vehicle_type == 'bus':
            self.bus_total[self.tollboth] += 1
            self.bus_revenue_total[self.tollboth] += self.bus_price

        if vehicle_type == 'truck':
            self.truck_total[self.tollboth] += 1
            self.truck_revenue_total[self.tollboth] += self.truck_price

        if vehicle_type == 'car_cashless':
            self.car_total[self.tollboth] += 1
            self.car_revenue_cashless_total[self.tollboth] += self.car_price

        if vehicle_type == 'bus_cashless':
            self.bus_total[self.tollboth] += 1
            self.bus_revenue_cashless_total[self.tollboth] += self.bus_price

        if vehicle_type == 'truck_cashless':
            self.truck_total[self.tollboth] += 1
            self.truck_revenue_cashless_total[self.tollboth] += self.truck_price

        if vehicle_type == 'car2':
            self.car_total2[self.tollboth] += 1
            self.car_revenue_total2[self.tollboth] += self.car_price2

        if vehicle_type == 'bus2':
            self.bus_total2[self.tollboth] += 1
            self.bus_revenue_total2[self.tollboth] += self.bus_price2

        if vehicle_type == 'truck2':
            self.truck_total2[self.tollboth] += 1
            self.truck_revenue_total2[self.tollboth] += self.truck_price2

        if vehicle_type == 'car2_cashless':
            self.car_total2[self.tollboth] += 1
            self.car_revenue_cashless_total2[self.tollboth] += self.car_price2

        if vehicle_type == 'bus2_cashless':
            self.bus_total2[self.tollboth] += 1
            self.bus_revenue_cashless_total2[self.tollboth] += self.bus_price2

        if vehicle_type == 'truck2_cashless':
            self.truck_total2[self.tollboth] += 1
            self.truck_revenue_cashless_total2[self.tollboth] += self.truck_price2


    def get_total(self,vehicle_type):

        if vehicle_type == 'car':
            return self.car_total[self.tollboth]

        if vehicle_type == 'bus':
            return self.bus_total[self.tollboth]

        if vehicle_type == 'truck':
            return self.truck_total[self.tollboth]

        if vehicle_type == 'car2':
            return self.car_total2[self.tollboth]

        if vehicle_type == 'bus2':
            return self.bus_total2[self.tollboth]

        if vehicle_type == 'truck2':
            return self.truck_total2[self.tollboth]

        if vehicle_type == 'car_all':
            return self.car_total[1]+self.car_total[2]+self.car_total[3]+self.car_total[4]+self.car_total[5]

        if vehicle_type == 'bus_all':
            return self.bus_total[1]+self.bus_total[2]+self.bus_total[3]+self.bus_total[4]+self.bus_total[5]

        if vehicle_type == 'truck_all':
            return self.truck_total[1]+self.truck_total[2]+self.truck_total[3]+self.truck_total[4]+self.truck_total[5]

        if vehicle_type == 'car2_all':
            return self.car_total2[1]+self.car_total2[2]+self.car_total2[3]+self.car_total2[4]+self.car_total2[5]

        if vehicle_type == 'bus2_all':
            return self.bus_total2[1]+self.bus_total2[2]+self.bus_total2[3]+self.bus_total2[4]+self.bus_total2[5]

        if vehicle_type == 'truck2_all':
            return self.truck_total2[1]+self.truck_total2[2]+self.truck_total2[3]+self.truck_total2[4]+self.truck_total2[5]

    def get_revenue(self,vehicle_type):

        if vehicle_type == 'car':
            return self.car_revenue_total[self.tollboth]

        if vehicle_type == 'bus':
            return self.bus_revenue_total[self.tollboth]

        if vehicle_type == 'truck':
            return self.truck_revenue_total[self.tollboth]

        if vehicle_type == 'car_cashless':
            return self.car_revenue_cashless_total[self.tollboth]

        if vehicle_type == 'bus_cashless':
            return self.bus_revenue_cashless_total[self.tollboth]

        if vehicle_type == 'truck_cashless':
            return self.truck_revenue_cashless_total[self.tollboth]

        if vehicle_type == 'car2':
            return self.car_revenue_total2[self.tollboth]

        if vehicle_type == 'bus2':
            return self.bus_revenue_total2[self.tollboth]

        if vehicle_type == 'truck2':
            return self.truck_revenue_total2[self.tollboth]

        if vehicle_type == 'car2_cashless':
            return self.car_revenue_cashless_total2[self.tollboth]

        if vehicle_type == 'bus2_cashless':
            return self.bus_revenue_cashless_total2[self.tollboth]

        if vehicle_type == 'truck2_cashless':
            return self.truck_revenue_cashless_total2[self.tollboth]

        if vehicle_type == 'car_all':
            return self.car_revenue_total[1]+self.car_revenue_total[2]+self.car_revenue_total[3]+self.car_revenue_total[4]+self.car_revenue_total[5]

        if vehicle_type == 'bus_all':
            return self.bus_revenue_total[1]+self.bus_revenue_total[2]+self.bus_revenue_total[3]+self.bus_revenue_total[4]+self.bus_revenue_total[5]

        if vehicle_type == 'truck_all':
            return self.truck_revenue_total[1]+self.truck_revenue_total[2]+self.truck_revenue_total[3]+self.truck_revenue_total[4]+self.truck_revenue_total[5]

        if vehicle_type == 'car_cashless_all':
            return self.car_revenue_cashless_total[1]+self.car_revenue_cashless_total[2]+self.car_revenue_cashless_total[3]+self.car_revenue_cashless_total[4]+self.car_revenue_cashless_total[5]

        if vehicle_type == 'bus_cashless_all':
            return self.bus_revenue_cashless_total[1]+self.bus_revenue_cashless_total[2]+self.bus_revenue_cashless_total[3]+self.bus_revenue_cashless_total[4]+self.bus_revenue_cashless_total[5]

        if vehicle_type == 'truck_cashless_all':
            return self.truck_revenue_cashless_total[1]+self.truck_revenue_cashless_total[2]+self.truck_revenue_cashless_total[3]+self.truck_revenue_cashless_total[4]+self.truck_revenue_cashless_total[5]

        if vehicle_type == 'car2_all':
            return self.car_revenue_total2[1]+self.car_revenue_total2[2]+self.car_revenue_total2[3]+self.car_revenue_total2[4]+self.car_revenue_total2[5]

        if vehicle_type == 'bus2_all':
            return self.bus_revenue_total2[1]+self.bus_revenue_total2[2]+self.bus_revenue_total2[3]+self.bus_revenue_total2[4]+self.bus_revenue_total2[5]

        if vehicle_type == 'truck2_all':
            return self.truck_revenue_total2[1]+self.truck_revenue_total2[2]+self.truck_revenue_total2[3]+self.truck_revenue_total2[4]+self.truck_revenue_total2[5]

        if vehicle_type == 'car2_cashless_all':
            return self.car_revenue_cashless_total2[1]+self.car_revenue_cashless_total2[2]+self.car_revenue_cashless_total2[3]+self.car_revenue_cashless_total2[4]+self.car_revenue_cashless_total2[5]

        if vehicle_type == 'bus2_cashless_all':
            return self.bus_revenue_cashless_total2[1]+self.bus_revenue_cashless_total2[2]+self.bus_revenue_cashless_total2[3]+self.bus_revenue_cashless_total2[4]+self.bus_revenue_cashless_total2[5]

        if vehicle_type == 'truck2_cashless_all':
            return self.truck_revenue_cashless_total2[1]+self.truck_revenue_cashless_total2[2]+self.truck_revenue_cashless_total2[3]+self.truck_revenue_cashless_total2[4]+self.truck_revenue_cashless_total2[5]


print('================================================================================\n                               Toll Payment Systems\n                                PT Jasa Marga, Tbk.\n================================================================================')
while True:
    ask = input('\nSelect location of Toll Gate:\n1. Meruya\n2. Pondok Aren\nEnter 3 for the total number of vehicles passing and total revenue of the day on all toll booth on each/both gates.\n> ')
    if ask == '1':

        while True:
            ask2 = int(input('\nWhich Toll Booth? (1, 2, 3, 4, 5)\nEnter 0 to change Toll Gate\n> '))
            v = Vehicle(ask2)

            if ask2 == 0:
                break

            while True:
                print('\nLocation of Toll Gate: Meruya\nToll Booth:',ask2,'\nMenu:\n1. Charge the vehicles.\n2. Count the total number of vehicles.\n3. Count the total revenue of the day.\n4. Change Toll Booth')
                usr=input('> ')

                if usr == '1':
                    ask=input('\nCategory of vehicle:\n1. Car (RP 6000)\n2. Bus (RP 8000)\n3. Truck (RP 10000)\n> ')

                    if ask == '1':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.add('car')
                            print('\nSuccess!\n')

                        elif ask3 == '2':
                            v.add('car_cashless')
                            print('\nSuccess!\n')

                    if ask == '2':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.add('bus')
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.add('bus_cashless')
                            print('\nSuccess!\n')

                    if ask == '3':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.add('truck')
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.add('truck_cashless')
                            print('\nSuccess!\n')

                if usr == '2':
                    print('\nToll Booth:',ask2,'\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_total('car'),'\t  ',v.get_total('bus'),'\t ',v.get_total('truck'),'\n-------------------')
                    print('Total number of vehicles:',v.get_total('car')+v.get_total('bus')+v.get_total('truck'),'\n')

                if usr == '3':
                    print('\nToll Booth:',ask2,'\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car'),'\t ',v.get_revenue('bus'),'\t',v.get_revenue('truck'),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_revenue('car')+v.get_revenue('bus')+v.get_revenue('truck'),'\n')
                    print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car_cashless'),'\t ',v.get_revenue('bus_cashless'),'\t',v.get_revenue('truck_cashless'),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_revenue('car_cashless')+v.get_revenue('bus_cashless')+v.get_revenue('truck_cashless'),'\n')
                    print('Grand total revenue: Rp.',v.get_revenue('car')+v.get_revenue('bus')+v.get_revenue('truck')+v.get_revenue('car_cashless')+v.get_revenue('bus_cashless')+v.get_revenue('truck_cashless'),'\n')

                if usr == '4':
                    break

    elif ask == '2':

        while True:
            ask2 = int(input('\nWhich Toll Booth? (1, 2, 3, 4, 5)\nEnter 0 to change Toll Gate\n> '))
            v = Vehicle(ask2)

            if ask2 == 0:
                break

            while True:
                print('\nLocation of Toll Gate: Pondok Aren\nToll Booth:',ask2,'\nMenu:\n1. Charge the vehicles.\n2. Count the total number of vehicles.\n3. Count the total revenue of the day.\n4. Change Toll Booth')
                usr=input('> ')

                if usr == '1':
                    ask=input('\nCategory of vehicle:\n1. Car (RP 18000)\n2. Bus (RP 20000)\n3. Truck (RP 25000)\n> ')

                    if ask == '1':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.add('car2')
                            print('\nSuccess!\n')

                        elif ask3 == '2':
                            v.add('car2_cashless')
                            print('\nSuccess!\n')

                    if ask == '2':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.add('bus2')
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.add('bus2_cashless')
                            print('\nSuccess!\n')

                    if ask == '3':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.add('truck2')
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.add('truck2_cashless')
                            print('\nSuccess!\n')

                if usr == '2':
                    print('\nToll Booth:',ask2,'\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_total('car2'),'\t  ',v.get_total('bus2'),'\t ',v.get_total('truck2'),'\n-------------------')
                    print('Total number of vehicles:',v.get_total('car2')+v.get_total('bus2')+v.get_total('truck2'),'\n')

                if usr == '3':
                    print('\nToll Booth:',ask2,'\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car2'),'\t ',v.get_revenue('bus2'),'\t',v.get_revenue('truck2'),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_revenue('car2')+v.get_revenue('bus2')+v.get_revenue('truck2'),'\n')
                    print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car2_cashless'),'\t ',v.get_revenue('bus2_cashless'),'\t',v.get_revenue('truck2_cashless'),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_revenue('car2_cashless')+v.get_revenue('bus2_cashless')+v.get_revenue('truck2_cashless'),'\n')
                    print('Grand total revenue: Rp.',v.get_revenue('car2')+v.get_revenue('bus2')+v.get_revenue('truck2')+v.get_revenue('car2_cashless')+v.get_revenue('bus2_cashless')+v.get_revenue('truck2_cashless'),'\n')

                if usr == '4':
                    break


    elif ask == '3':

        while True:
            ask_again = input('\nWhich Toll Gate? (1. Meruya, 2. Pondok Aren, 3. Both)\nEnter 0 to go back.\n> ')

            if ask_again == '0':
                break

            if ask_again == '1':

                print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_total('car_all'),'\t  ',v.get_total('bus_all'),'\t ',v.get_total('truck_all'),'\n-------------------')
                print('Total number of vehicles:',v.get_total('car_all')+v.get_total('bus_all')+v.get_total('truck_all'),'\n')

                print('Revenues\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car_all'),'\t ',v.get_revenue('bus_all'),'\t',v.get_revenue('truck_all'),'\n--------------------------')
                print('Total revenue: Rp.',v.get_revenue('car_all')+v.get_revenue('bus_all')+v.get_revenue('truck_all'),'\n')
                print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car_cashless_all'),'\t ',v.get_revenue('bus_cashless_all'),'\t',v.get_revenue('truck_cashless_all'),'\n--------------------------')
                print('Total revenue: Rp.',v.get_revenue('car_cashless_all')+v.get_revenue('bus_cashless_all')+v.get_revenue('truck_cashless_all'),'\n')
                print('Grand total revenue: Rp.',v.get_revenue('car_all')+v.get_revenue('bus_all')+v.get_revenue('truck_all')+v.get_revenue('car_cashless_all')+v.get_revenue('bus_cashless_all')+v.get_revenue('truck_cashless_all'),'\n')

            elif ask_again == '2':

                print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_total('car2_all'),'\t  ',v.get_total('bus2_all'),'\t ',v.get_total('truck2_all'),'\n-------------------')
                print('Total number of vehicles:',v.get_total('car2_all')+v.get_total('bus2_all')+v.get_total('truck2_all'),'\n')

                print('Revenues\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car2_all'),'\t ',v.get_revenue('bus2_all'),'\t',v.get_revenue('truck2_all'),'\n--------------------------')
                print('Total revenue: Rp.',v.get_revenue('car2_all')+v.get_revenue('bus2_all')+v.get_revenue('truck2_all'),'\n')
                print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car2_cashless_all'),'\t ',v.get_revenue('bus2_cashless_all'),'\t',v.get_revenue('truck2_cashless_all'),'\n--------------------------')
                print('Total revenue: Rp.',v.get_revenue('car2_cashless_all')+v.get_revenue('bus2_cashless_all')+v.get_revenue('truck2_cashless_all'),'\n')
                print('Grand total revenue: Rp.',v.get_revenue('car2_all')+v.get_revenue('bus2_all')+v.get_revenue('truck2_all')+v.get_revenue('car2_cashless_all')+v.get_revenue('bus2_cashless_all')+v.get_revenue('truck2_cashless_all'),'\n')

            elif ask_again == '3':

                print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_total('car_all')+v.get_total('car2_all'),'\t  ',v.get_total('bus_all')+v.get_total('bus2_all'),'\t ',v.get_total('truck_all')+v.get_total('truck2_all'),'\n-------------------')
                print('Total number of vehicles:',v.get_total('car_all')+v.get_total('bus_all')+v.get_total('truck_all')+v.get_total('car2_all')+v.get_total('bus2_all')+v.get_total('truck2_all'),'\n')

                print('Revenues\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car_all')+v.get_revenue('car2_all'),'\t ',v.get_revenue('bus_all')+v.get_revenue('bus2_all'),'\t',v.get_revenue('truck_all')+v.get_revenue('truck2_all'),'\n--------------------------')
                print('Total revenue: Rp.',v.get_revenue('car_all')+v.get_revenue('bus_all')+v.get_revenue('truck_all')+v.get_revenue('car2_all')+v.get_revenue('bus2_all')+v.get_revenue('truck2_all'),'\n')
                print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_revenue('car_cashless_all')+v.get_revenue('car2_cashless_all'),'\t ',v.get_revenue('bus_cashless_all')+v.get_revenue('bus2_cashless_all'),'\t',v.get_revenue('truck_cashless_all')+v.get_revenue('truck2_cashless_all'),'\n--------------------------')
                print('Total revenue: Rp.',v.get_revenue('car_cashless_all')+v.get_revenue('bus_cashless_all')+v.get_revenue('truck_cashless_all')+v.get_revenue('car2_cashless_all')+v.get_revenue('bus2_cashless_all')+v.get_revenue('truck2_cashless_all'),'\n')
                print('Grand total revenue: Rp.',v.get_revenue('car_all')+v.get_revenue('bus_all')+v.get_revenue('truck_all')+v.get_revenue('car_cashless_all')+v.get_revenue('bus_cashless_all')+v.get_revenue('truck_cashless_all')+v.get_revenue('car2_all')+v.get_revenue('bus2_all')+v.get_revenue('truck2_all')+v.get_revenue('car2_cashless_all')+v.get_revenue('bus2_cashless_all')+v.get_revenue('truck2_cashless_all'),'\n')

