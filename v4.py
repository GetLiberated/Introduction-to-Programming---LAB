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

    def car(self):
        self.car_total[self.tollboth] += 1
        self.car_revenue_total[self.tollboth] += self.car_price

    def bus(self):
        self.bus_total[self.tollboth] += 1
        self.bus_revenue_total[self.tollboth] += self.bus_price

    def truck(self):
        self.truck_total[self.tollboth] += 1
        self.truck_revenue_total[self.tollboth] += self.truck_price

    def car_cashless(self):
        self.car_total[self.tollboth] += 1
        self.car_revenue_cashless_total[self.tollboth] += self.car_price

    def bus_cashless(self):
        self.bus_total[self.tollboth] += 1
        self.bus_revenue_cashless_total[self.tollboth] += self.bus_price

    def truck_cashless(self):
        self.truck_total[self.tollboth] += 1
        self.truck_revenue_cashless_total[self.tollboth] += self.truck_price

    def get_car_total(self):
        return self.car_total[self.tollboth]

    def get_bus_total(self):
        return self.bus_total[self.tollboth]

    def get_truck_total(self):
        return self.truck_total[self.tollboth]

    def get_car_revenue_total(self):
        return self.car_revenue_total[self.tollboth]

    def get_bus_revenue_total(self):
        return self.bus_revenue_total[self.tollboth]

    def get_truck_revenue_total(self):
        return self.truck_revenue_total[self.tollboth]

    def get_car_revenue_cashless_total(self):
        return self.car_revenue_cashless_total[self.tollboth]

    def get_bus_revenue_cashless_total(self):
        return self.bus_revenue_cashless_total[self.tollboth]

    def get_truck_revenue_cashless_total(self):
        return self.truck_revenue_cashless_total[self.tollboth]

    def car2(self):
        self.car_total2[self.tollboth] += 1
        self.car_revenue_total2[self.tollboth] += self.car_price2

    def bus2(self):
        self.bus_total2[self.tollboth] += 1
        self.bus_revenue_total2[self.tollboth] += self.bus_price2

    def truck2(self):
        self.truck_total2[self.tollboth] += 1
        self.truck_revenue_total2[self.tollboth] += self.truck_price2

    def car2_cashless(self):
        self.car_total2[self.tollboth] += 1
        self.car_revenue_cashless_total2[self.tollboth] += self.car_price2

    def bus2_cashless(self):
        self.bus_total2[self.tollboth] += 1
        self.bus_revenue_cashless_total2[self.tollboth] += self.bus_price2

    def truck2_cashless(self):
        self.truck_total2[self.tollboth] += 1
        self.truck_revenue_cashless_total2[self.tollboth] += self.truck_price2

    def get_car_total2(self):
        return self.car_total2[self.tollboth]

    def get_bus_total2(self):
        return self.bus_total2[self.tollboth]

    def get_truck_total2(self):
        return self.truck_total2[self.tollboth]

    def get_car_revenue_total2(self):
        return self.car_revenue_total2[self.tollboth]

    def get_bus_revenue_total2(self):
        return self.bus_revenue_total2[self.tollboth]

    def get_truck_revenue_total2(self):
        return self.truck_revenue_total2[self.tollboth]

    def get_car_revenue_cashless_total2(self):
        return self.car_revenue_cashless_total2[self.tollboth]

    def get_bus_revenue_cashless_total2(self):
        return self.bus_revenue_cashless_total2[self.tollboth]

    def get_truck_revenue_cashless_total2(self):
        return self.truck_revenue_cashless_total2[self.tollboth]

    def get_car_total_all(self):
        return self.car_total[1]+self.car_total[2]+self.car_total[3]+self.car_total[4]+self.car_total[5]

    def get_bus_total_all(self):
        return self.bus_total[1]+self.bus_total[2]+self.bus_total[3]+self.bus_total[4]+self.bus_total[5]

    def get_truck_total_all(self):
        return self.truck_total[1]+self.truck_total[2]+self.truck_total[3]+self.truck_total[4]+self.truck_total[5]

    def get_car_revenue_total_all(self):
        return self.car_revenue_total[1]+self.car_revenue_total[2]+self.car_revenue_total[3]+self.car_revenue_total[4]+self.car_revenue_total[5]

    def get_bus_revenue_total_all(self):
        return self.bus_revenue_total[1]+self.bus_revenue_total[2]+self.bus_revenue_total[3]+self.bus_revenue_total[4]+self.bus_revenue_total[5]

    def get_truck_revenue_total_all(self):
        return self.truck_revenue_total[1]+self.truck_revenue_total[2]+self.truck_revenue_total[3]+self.truck_revenue_total[4]+self.truck_revenue_total[5]

    def get_car_revenue_cashless_total_all(self):
        return self.car_revenue_cashless_total[1]+self.car_revenue_cashless_total[2]+self.car_revenue_cashless_total[3]+self.car_revenue_cashless_total[4]+self.car_revenue_cashless_total[5]

    def get_bus_revenue_cashless_total_all(self):
        return self.bus_revenue_cashless_total[1]+self.bus_revenue_cashless_total[2]+self.bus_revenue_cashless_total[3]+self.bus_revenue_cashless_total[4]+self.bus_revenue_cashless_total[5]

    def get_truck_revenue_cashless_total_all(self):
        return self.truck_revenue_cashless_total[1]+self.truck_revenue_cashless_total[2]+self.truck_revenue_cashless_total[3]+self.truck_revenue_cashless_total[4]+self.truck_revenue_cashless_total[5]

    def get_car_total2_all(self):
        return self.car_total2[1]+self.car_total2[2]+self.car_total2[3]+self.car_total2[4]+self.car_total2[5]

    def get_bus_total2_all(self):
        return self.bus_total2[1]+self.bus_total2[2]+self.bus_total2[3]+self.bus_total2[4]+self.bus_total2[5]

    def get_truck_total2_all(self):
        return self.truck_total2[1]+self.truck_total2[2]+self.truck_total2[3]+self.truck_total2[4]+self.truck_total2[5]

    def get_car_revenue_total2_all(self):
        return self.car_revenue_total2[1]+self.car_revenue_total2[2]+self.car_revenue_total2[3]+self.car_revenue_total2[4]+self.car_revenue_total2[5]

    def get_bus_revenue_total2_all(self):
        return self.bus_revenue_total2[1]+self.bus_revenue_total2[2]+self.bus_revenue_total2[3]+self.bus_revenue_total2[4]+self.bus_revenue_total2[5]

    def get_truck_revenue_total2_all(self):
        return self.truck_revenue_total2[1]+self.truck_revenue_total2[2]+self.truck_revenue_total2[3]+self.truck_revenue_total2[4]+self.truck_revenue_total2[5]

    def get_car_revenue_cashless_total2_all(self):
        return self.car_revenue_cashless_total2[1]+self.car_revenue_cashless_total2[2]+self.car_revenue_cashless_total2[3]+self.car_revenue_cashless_total2[4]+self.car_revenue_cashless_total2[5]

    def get_bus_revenue_cashless_total2_all(self):
        return self.bus_revenue_cashless_total2[1]+self.bus_revenue_cashless_total2[2]+self.bus_revenue_cashless_total2[3]+self.bus_revenue_cashless_total2[4]+self.bus_revenue_cashless_total2[5]

    def get_truck_revenue_cashless_total2_all(self):
        return self.truck_revenue_cashless_total2[1]+self.truck_revenue_cashless_total2[2]+self.truck_revenue_cashless_total2[3]+self.truck_revenue_cashless_total2[4]+self.truck_revenue_cashless_total2[5]



print('================================================================================\n                               Toll Payment Systems\n                                PT Jasa Marga, Tbk.\n================================================================================')
while True:
    ask = input('\nSelect location of Toll Gate:\n1. Meruya\n2. Pondok Aren\nPress 3 for the total number of vehicles passing and total revenue of the day on all toll booth at each/both gates.\n> ')
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
                            v.car()
                            print('\nSuccess!\n')

                        elif ask3 == '2':
                            v.car_cashless()
                            print('\nSuccess!\n')

                    if ask == '2':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.bus()
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.bus_cashless()
                            print('\nSuccess!\n')

                    if ask == '3':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.truck()
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.truck_cashless()
                            print('\nSuccess!\n')

                if usr == '2':
                    print('\nToll Booth:',ask2,'\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total(),'\t  ',v.get_bus_total(),'\t ',v.get_truck_total(),'\n-------------------')
                    print('Total number of vehicles:',v.get_car_total()+v.get_bus_total()+v.get_truck_total(),'\n')

                if usr == '3':
                    print('\nToll Booth:',ask2,'\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total(),'\t ',v.get_bus_revenue_total(),'\t',v.get_truck_revenue_total(),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_car_revenue_total()+v.get_bus_revenue_total()+v.get_truck_revenue_total(),'\n')
                    print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_cashless_total(),'\t ',v.get_bus_revenue_cashless_total(),'\t',v.get_truck_revenue_cashless_total(),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_car_revenue_cashless_total()+v.get_bus_revenue_cashless_total()+v.get_truck_revenue_cashless_total(),'\n')
                    print('Grand total revenue: Rp.',v.get_car_revenue_total()+v.get_bus_revenue_total()+v.get_truck_revenue_total()+v.get_car_revenue_cashless_total()+v.get_bus_revenue_cashless_total()+v.get_truck_revenue_cashless_total(),'\n')


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
                            v.car2()
                            print('\nSuccess!\n')

                        elif ask3 == '2':
                            v.car2_cashless()
                            print('\nSuccess!\n')

                    if ask == '2':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.bus2()
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.bus2_cashless()
                            print('\nSuccess!\n')

                    if ask == '3':
                        ask3 = input('\nPay with:\n1. Cash\n2. Cashless\n> ')

                        if ask3 == '1':
                            v.truck2()
                            print('\nSuccess!\n')

                        if ask3 == '2':
                            v.truck2_cashless()
                            print('\nSuccess!\n')

                if usr == '2':
                    print('\nToll Booth:',ask2,'\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total2(),'\t  ',v.get_bus_total2(),'\t ',v.get_truck_total2(),'\n-------------------')
                    print('Total number of vehicles:',v.get_car_total2()+v.get_bus_total2()+v.get_truck_total2(),'\n')

                if usr == '3':
                    print('\nToll Booth:',ask2,'\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total2(),'\t ',v.get_bus_revenue_total2(),'\t',v.get_truck_revenue_total2(),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_car_revenue_total2()+v.get_bus_revenue_total2()+v.get_truck_revenue_total2(),'\n')
                    print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_cashless_total2(),'\t ',v.get_bus_revenue_cashless_total2(),'\t',v.get_truck_revenue_cashless_total2(),'\n--------------------------')
                    print('Total revenue: Rp.',v.get_car_revenue_cashless_total2()+v.get_bus_revenue_cashless_total2()+v.get_truck_revenue_cashless_total2(),'\n')
                    print('Grand total revenue: Rp.',v.get_car_revenue_total2()+v.get_bus_revenue_total2()+v.get_truck_revenue_total2()+v.get_car_revenue_cashless_total2()+v.get_bus_revenue_cashless_total2()+v.get_truck_revenue_cashless_total2(),'\n')

                if usr == '4':
                    break

    elif ask == '3':

        ask_again = input('\nSelect Toll gate:\n1. Meruya, 2. Pondok Aren, 3. Both\n> ')

        if ask_again == '1':

            print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total_all(),'\t  ',v.get_bus_total_all(),'\t ',v.get_truck_total_all(),'\n-------------------')
            print('Total number of vehicles:',v.get_car_total_all()+v.get_bus_total_all()+v.get_truck_total_all(),'\n\n')

            print('Revenues\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total_all(),'\t ',v.get_bus_revenue_total_all(),'\t',v.get_truck_revenue_total_all(),'\n--------------------------')
            print('Total revenue: Rp.',v.get_car_revenue_total_all()+v.get_bus_revenue_total_all()+v.get_truck_revenue_total_all(),'\n')
            print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_cashless_total_all(),'\t ',v.get_bus_revenue_cashless_total_all(),'\t',v.get_truck_revenue_cashless_total_all(),'\n--------------------------')
            print('Total revenue: Rp.',v.get_car_revenue_cashless_total_all()+v.get_bus_revenue_cashless_total_all()+v.get_truck_revenue_cashless_total_all(),'\n')
            print('Grand total revenue: Rp.',v.get_car_revenue_total_all()+v.get_bus_revenue_total_all()+v.get_truck_revenue_total_all()+v.get_car_revenue_cashless_total_all()+v.get_bus_revenue_cashless_total_all()+v.get_truck_revenue_cashless_total_all(),'\n')


        elif ask_again == '2':

            print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total2_all(),'\t  ',v.get_bus_total2_all(),'\t ',v.get_truck_total2_all(),'\n-------------------')
            print('Total number of vehicles:',v.get_car_total2_all()+v.get_bus_total2_all()+v.get_truck_total2_all(),'\n\n')

            print('Revenues\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total2_all(),'\t ',v.get_bus_revenue_total2_all(),'\t',v.get_truck_revenue_total2_all(),'\n--------------------------')
            print('Total revenue: Rp.',v.get_car_revenue_total2_all()+v.get_bus_revenue_total2_all()+v.get_truck_revenue_total2_all(),'\n')
            print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_cashless_total2_all(),'\t ',v.get_bus_revenue_cashless_total2_all(),'\t',v.get_truck_revenue_cashless_total2_all(),'\n--------------------------')
            print('Total revenue: Rp.',v.get_car_revenue_cashless_total2_all()+v.get_bus_revenue_cashless_total2_all()+v.get_truck_revenue_cashless_total2_all(),'\n')
            print('Grand total revenue: Rp.',v.get_car_revenue_total2_all()+v.get_bus_revenue_total2_all()+v.get_truck_revenue_total2_all()+v.get_car_revenue_cashless_total2_all()+v.get_bus_revenue_cashless_total2_all()+v.get_truck_revenue_cashless_total2_all(),'\n')


        elif ask_again == '3':

            print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total_all()+v.get_car_total2_all(),'\t  ',v.get_bus_total_all()+v.get_bus_total2_all(),'\t ',v.get_truck_total_all()+v.get_truck_total2_all(),'\n-------------------')
            print('Total number of vehicles:',v.get_car_total_all()+v.get_bus_total_all()+v.get_truck_total_all()+v.get_car_total2_all()+v.get_bus_total2_all()+v.get_truck_total2_all(),'\n\n')

            print('Revenues\n\nCash\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total_all()+v.get_car_revenue_total2_all(),'\t ',v.get_bus_revenue_total_all()+v.get_bus_revenue_total2_all(),'\t',v.get_truck_revenue_total_all()+v.get_truck_revenue_total2_all(),'\n--------------------------')
            print('Total revenue: Rp.',v.get_car_revenue_total_all()+v.get_bus_revenue_total_all()+v.get_truck_revenue_total_all()+v.get_car_revenue_total2_all()+v.get_bus_revenue_total2_all()+v.get_truck_revenue_total2_all(),'\n')
            print('\nCashless\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_cashless_total_all()+v.get_car_revenue_cashless_total2_all(),'\t ',v.get_bus_revenue_cashless_total_all()+v.get_bus_revenue_cashless_total2_all(),'\t',v.get_truck_revenue_cashless_total_all()+v.get_truck_revenue_cashless_total2_all(),'\n--------------------------')
            print('Total revenue: Rp.',v.get_car_revenue_cashless_total_all()+v.get_bus_revenue_cashless_total_all()+v.get_truck_revenue_cashless_total_all()+v.get_car_revenue_cashless_total2_all()+v.get_bus_revenue_cashless_total2_all()+v.get_truck_revenue_cashless_total2_all(),'\n')
            print('Grand total revenue: Rp.',v.get_car_revenue_total_all()+v.get_bus_revenue_total_all()+v.get_truck_revenue_total_all()+v.get_car_revenue_total2_all()+v.get_bus_revenue_total2_all()+v.get_truck_revenue_total2_all()+v.get_car_revenue_cashless_total_all()+v.get_bus_revenue_cashless_total_all()+v.get_truck_revenue_cashless_total_all()+v.get_car_revenue_cashless_total2_all()+v.get_bus_revenue_cashless_total2_all()+v.get_truck_revenue_cashless_total2_all(),'\n')

