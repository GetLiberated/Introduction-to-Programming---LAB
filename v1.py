class TollGate:
    def __init__(self):
        self.car_price = 6000
        self.bus_price = 8000
        self.truck_price = 10000

class Vehicle(TollGate):
    def car(self):
        print('\nFee:',self.car_price)
    def bus(self):
        print('\nFee:',self.bus_price)
    def truck(self):
        print('\nFee:',self.truck_price)


v = Vehicle()

print('================================================================================\n                               Toll Payment Systems\n                                PT Jasa Marga, Tbk.\n================================================================================')
while True:
    ask=input('\nCategory of vehicle:\n1. Car (RP 6000)\n2. Bus (RP 8000)\n3. Truck (RP 10000)\n> ')

    if ask == '1':
        v.car()

    if ask == '2':
        v.bus()

    if ask == '3':
        v.truck()
