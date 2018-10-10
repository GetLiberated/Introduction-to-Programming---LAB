class TollGate:
    def __init__(self):
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


class Vehicle(TollGate):
    def car(self):
        self.car_total[0] += 1
        self.car_revenue_total[0] += self.car_price

    def bus(self):
        self.bus_total[0] += 1
        self.bus_revenue_total[0] += self.bus_price

    def truck(self):
        self.truck_total[0] += 1
        self.truck_revenue_total[0] += self.truck_price


v = Vehicle()

print('================================================================================\n                               Toll Payment Systems\n                                PT Jasa Marga, Tbk.\n================================================================================')
while True:
    usr=input('\nMenu:\n1. Charge the vehicles.\n2. Count the total number of vehicles.\n3. Count the total revenue of the day.\n> ')

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
