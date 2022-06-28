class Building:
    def __init__(self, size=2500, cost=600000):
        self.size = size
        self.cost = cost
    def __str__(self):
        return "The build is {} square ft and costs ${}.".format(self.size, self.cost)

class Bank(Building):
    def __init__(self, size =10000, cost = 2000000 ):
        self.size = size
        self.cost = cost
        self.client_list = {}

    def add_client_deposit(self, client_name, deposit_amount):
        try:   
            self.client_list[client_name] += deposit_amount
        except:
            self.client_list[client_name] = deposit_amount

    def cash_on_hand(self ):
        total_cash = sum(self.client_list.values())
        return total_cash

    def __str__(self):
        print(Building.__str__(self))
        cash = self.cash_on_hand()
        return "The building is a bank with ${} cash on hand.".format(cash)
















test_bank = Bank(25000, 2500000)
print(test_bank)

test_bank.add_client_deposit("Jack Sparrow", 50000)

test_bank.add_client_deposit("Johns Tip", 250)

print(test_bank.cash_on_hand())

test_bank.add_client_deposit("Johns Tip", 10)

print(test_bank.cash_on_hand())