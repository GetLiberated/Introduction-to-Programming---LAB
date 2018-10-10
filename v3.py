class TollGate:
    def __init__(self):
        super(TollGate,self).__init__()
        self.car_price = 6000
        self.bus_price = 8000
        self.truck_price = 10000
        self.car_total = [0]
        self.bus_total = [0]
        self.truck_total = [0]
        self.car_revenue_total = [0]
        self.bus_revenue_total = [0]
        self.truck_revenue_total = [0]

    def get_car_total(self):
        return self.car_total[0]

    def get_bus_total(self):
        return self.bus_total[0]

    def get_truck_total(self):
        return self.truck_total[0]

    def get_car_revenue_total(self):
        return self.car_revenue_total[0]

    def get_bus_revenue_total(self):
        return self.bus_revenue_total[0]

    def get_truck_revenue_total(self):
        return self.truck_revenue_total[0]


class TollGate2:
    def __init__(self):
        super(TollGate2,self).__init__()
        self.car_price2 = 18000
        self.bus_price2 = 20000
        self.truck_price2 = 25000
        self.car_total2 = [0]
        self.bus_total2 = [0]
        self.truck_total2 = [0]
        self.car_revenue_total2 = [0]
        self.bus_revenue_total2 = [0]
        self.truck_revenue_total2 = [0]

    def get_car_total2(self):
        return self.car_total2[0]

    def get_bus_total2(self):
        return self.bus_total2[0]

    def get_truck_total2(self):
        return self.truck_total2[0]

    def get_car_revenue_total2(self):
        return self.car_revenue_total2[0]

    def get_bus_revenue_total2(self):
        return self.bus_revenue_total2[0]

    def get_truck_revenue_total2(self):
        return self.truck_revenue_total2[0]


class Vehicle(TollGate,TollGate2):
    def __init__(self):
        super(Vehicle,self).__init__()
    def car(self):
        self.car_total[0] += 1
        self.car_revenue_total[0] += self.car_price

    def bus(self):
        self.bus_total[0] += 1
        self.bus_revenue_total[0] += self.bus_price

    def truck(self):
        self.truck_total[0] += 1
        self.truck_revenue_total[0] += self.truck_price

    def car2(self):
        self.car_total2[0] += 1
        self.car_revenue_total2[0] += self.car_price2

    def bus2(self):
        self.bus_total2[0] += 1
        self.bus_revenue_total2[0] += self.bus_price2

    def truck2(self):
        self.truck_total2[0] += 1
        self.truck_revenue_total2[0] += self.truck_price2


v = Vehicle()

print('================================================================================\n                               Toll Payment Systems\n                                PT Jasa Marga, Tbk.\n================================================================================')
while True:
    ask = input('\nSelect location of Toll gate:\n1. Meruya\n2. Pondok Aren\nPress 3 for the whole number of vehicles passing the toll gates and total revenue of the day on both gates.\n> ')
    if ask == '1':

        while True:
            usr=input('\nLocation of Toll gate: Meruya\nMenu:\n1. Charge the vehicles.\n2. Count the total number of vehicles.\n3. Count the total revenue of the day.\n4. Change Toll Gate\n> ')

            if usr == '1':
                ask=input('\nCategory of vehicle:\n1. Car (RP 6000)\n2. Bus (RP 8000)\n3. Truck (RP 10000)\n> ')

                if ask == '1':
                    v.car()
                    print('\nSuccess!\n')

                if ask == '2':
                    v.bus()
                    print('\nSuccess!\n')

                if ask == '3':
                    v.truck()
                    print('\nSuccess!\n')

            if usr == '2':
                print('\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total(),'\t  ',v.get_bus_total(),'\t ',v.get_truck_total(),'\n-------------------\n')
                print('Total number of vehicles:',v.get_car_total()+v.get_bus_total()+v.get_truck_total(),'\n')

            if usr == '3':
                print('\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total(),'\t ',v.get_bus_revenue_total(),'\t',v.get_truck_revenue_total(),'\n--------------------------\n')
                print('Total revenue: Rp.',v.get_car_revenue_total()+v.get_bus_revenue_total()+v.get_truck_revenue_total(),'\n')

            if usr == '4':
                break

    elif ask == '2':

        while True:
            usr=input('\nLocation of Toll gate: Pondok Aren\nMenu:\n1. Charge the vehicles.\n2. Count the total number of vehicles.\n3. Count the total revenue of the day.\n4. Change Toll Gate\n> ')

            if usr == '1':
                ask=input('\nCategory of vehicle:\n1. Car (RP 18000)\n2. Bus (RP 20000)\n3. Truck (RP 25000)\n> ')

                if ask == '1':
                    v.car2()
                    print('\nSuccess!\n')

                if ask == '2':
                    v.bus2()
                    print('\nSuccess!\n')

                if ask == '3':
                    v.truck2()
                    print('\nSuccess!\n')

            if usr == '2':
                print('\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total2(),'\t  ',v.get_bus_total2(),'\t ',v.get_truck_total2(),'\n-------------------')
                print('Total number of vehicles:',v.get_car_total2()+v.get_bus_total2()+v.get_truck_total2(),'\n')

            if usr == '3':
                print('\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total2(),'\t ',v.get_bus_revenue_total2(),'\t',v.get_truck_revenue_total2(),'\n--------------------------')
                print('Total revenue: Rp.',v.get_car_revenue_total2()+v.get_bus_revenue_total2()+v.get_truck_revenue_total2(),'\n')

            if usr == '4':
                break

    elif ask == '3':

        print('\nVehicles\n-------------------\nCar   Bus   Truck\n-------------------\n',v.get_car_total()+v.get_car_total2(),'\t  ',v.get_bus_total()+v.get_bus_total2(),'\t ',v.get_truck_total()+v.get_truck_total2(),'\n-------------------')
        print('Total number of vehicles:',v.get_car_total()+v.get_bus_total()+v.get_truck_total()+v.get_car_total2()+v.get_bus_total2()+v.get_truck_total2(),'\n\n')
        print('Revenues\n--------------------------\nCar       Bus        Truck\n--------------------------\n',v.get_car_revenue_total()+v.get_car_revenue_total2(),'\t ',v.get_bus_revenue_total()+v.get_bus_revenue_total2(),'\t',v.get_truck_revenue_total()+v.get_truck_revenue_total2(),'\n--------------------------')
        print('Total revenue: Rp.',v.get_car_revenue_total()+v.get_bus_revenue_total()+v.get_truck_revenue_total()+v.get_car_revenue_total2()+v.get_bus_revenue_total2()+v.get_truck_revenue_total2(),'\n')

