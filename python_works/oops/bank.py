# BANKNAME ,person name ,account<name ,balance

# deposit,withdraw,enquiry



class Bank:

    bank_name:str

    person_name:str

    account_number:int

    balance:float

    def set_bank(self,person_name,account_number,balance):

        self.bank_name = 'SBI'

        self.person_name = person_name

        self.account_number = account_number

        self.balance = balance

    def deposit(self,amount):

        # self.amount=amount

        self.balance+=amount

        print('money is deposited')

    def withdraw(self,amount):

        # self.amount=amount

        if amount<self.balance:

            self.balance+=amount

            print('money is debited')

        else:

            print('not enough balance')

    def bal_enquiry(self):

        print('balance is',self.balance)


brigin = Bank()

brigin.set_bank('brigin1',23,20000)

brigin.bal_enquiry()
