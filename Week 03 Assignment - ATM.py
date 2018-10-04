# Muhammad Erizky Suryaputra
# 2201797052

#### CLASS ATM ####
# a Bank with class. B-)

# Class for bank
class Bank:
    # Ask customer name here
    def register(self):
        a = input('First Name: ')
        b = input('Last Name: ')
        global customer # Declare variable 'customer' as global
        customer = Customer(a,b) # Object for Customer class with 'a' and 'b' as parameter
        customer.data() # Execute 'data' module inside Costumer class

# Class for customer
class Customer:
    # Initialize parameter 'a' and 'b'
    def __init__(self,a,b):
        self.firstName = a
        self.lastName = b

    # Store new customer name here, and also give them 0 money
    def data(self):
        namebase.append(self.firstName+' '+self.lastName)
        moneybase.append(0)
        print('\nAccount successfully registered!\n')

    # If you get bored and want to get fired, delete some registered customer here!
    def delete(self):
        for x in range (len(namebase)):
            print('\nNo.',x,'\nCustomer:',namebase[x],'\nAccount: $',moneybase[x],'\n')
        ask = int(input('Select account to delete: '))
        del namebase[ask]
        del moneybase[ask]

# Class for account
class Account:
    # Show list of registered customer
    def getBalance(self):
        for x in range (len(namebase)):
            print('\nNo.',x,'\nCustomer:',namebase[x],'\nAccount: $',moneybase[x],'\n')

    # Deposit dem money here
    def deposit(self):
        for x in range (len(namebase)):
            print('\nNo.',x,'\nCustomer:',namebase[x],'\nAccount: $',moneybase[x],'\n')
        ask=int(input('Who? '))
        amount = int(input('How much? '))
        moneybase[ask] += amount

    # Withdraw customer money here
    def withdraw(self):
        ask=int(input('Who? '))
        amount = int(input('How much? '))
        moneybase[ask] -= amount

    # Be nice and give some to charity will ya?
    def transfer(self):
        for x in range (len(namebase)):
            print('\nNo.',x,'\nCustomer:',namebase[x],'\nAccount: $',moneybase[x],'\n')
        ask=int(input('Transfer from: '))
        ask2=int(input('Transfer to: '))
        ask3=int(input('Amount of money to transfer:  '))
        moneybase[ask] -= ask3
        moneybase[ask2] += ask3

namebase = [] # Store customer name here
moneybase = [] # Store customer money here
bankName = 'Cool' # Insert the bank name here
bank = Bank() # Object for Bank Class
account = Account() # Object for Account Class

#Create a loop
while True:
    # Create a menu for input
    usr=input('Welcome to '+bankName+'bank!\nMenu:\n1. Register\n2. View Account\n3. Deposit\n4. Withdraw\n5. Transfer\n6. Delete Account\n7. Quit\n> ')
    if usr=='1':
        bank.register()
    if usr=='2':
        account.getBalance()
    if usr=='3':
        account.deposit()
    if usr=='4':
        account.withdraw()
    if usr=='5':
        account.transfer()
    if usr=='6':
        customer.delete()
    if usr=='7':
        print('Please come back again!\n')
        break
