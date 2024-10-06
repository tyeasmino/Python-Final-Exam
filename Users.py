from abc import ABC

class Bank:
    users = []
    admins = []
    bankrupt = 0
    transaction_history = []
    available_balance = 200000
    loan_amount = 0

    @staticmethod
    def add_transaction(acccount_no, transaction_type='', transaction_amount='', transferdTo='', transferdAmount='', receivedFrom='', receivedAmount=''):
        Bank.transaction_history.append((acccount_no, transaction_type, transaction_amount, transferdTo, transferdAmount, receivedFrom, receivedAmount))

class Users(ABC):
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        if account_type == 1: self.account_type = 'savings'
        else: self.account_type = 'current'
        amount = 0
        account_no = len(Bank.users)+1 
        limit = 2

        user = (account_no, self.account_type, name, email, address, amount, limit)
        Bank.users.append(user) 

    def deposit(self, account_no, deposit_amount):
        for i, u in enumerate(Bank.users):
            if u[0] == account_no:
                data = list(u)
                data[5] += deposit_amount
                Bank.users[i] = tuple(data) 
                Bank.available_balance += deposit_amount
                Bank.add_transaction(account_no, transaction_type='Deposit ', transaction_amount=deposit_amount)
                print(f"Your new balance is {data[5]}")
                return   
        print(f"Account does not exist") 
        
    def withdraw(self, account_no, withdraw_amount):
        if Bank.bankrupt:
            print("Bank is bankrupt") 
            return

        for i, u in enumerate(Bank.users):
            if u[0] == account_no:
                data = list(u)
                if withdraw_amount > data[5]:
                    print("Withdrawal amount excessded")
                    return
                else: 
                    data[5] -= withdraw_amount 
                    Bank.available_balance -= withdraw_amount
                    Bank.users[i] = tuple(data)
                    Bank.add_transaction(account_no, transaction_type='Withdraw', transaction_amount=withdraw_amount) 
                    print(f"{withdraw_amount} taka withdraw done")
                    return 
            else: 
                print(f"Account does not exist") 

    def available_balance(self, account_no): 
        for u in Bank.users:
            if u[0] == account_no:
                print(f"Your available balance: {u[5]} for account no: {u[0]}")
                return    
        print('Account no is not exist')
        
    def transaction_history(self, account_no):
        print("Account NO \tTransaction Type \tTransaction Amount \tTransferd To \tTransfer Amount \tReceived From \tReceived Amount")
        noaccount = 1
        for t in Bank.transaction_history:
            if t[0] == account_no:
                noaccount = 0
                print(f"{t[0]}\t\t{t[1]}\t\t{t[2]}\t\t\t\t{t[3]}\t\t\t{t[4]}\t\t\t{t[5]}\t\t{t[6]}")
        
        if noaccount: 
            print(f'There is no transaction history of account {account_no}')

    def loan(self, account_no, loan_amount):
        if Bank.bankrupt:
            print("Bank is bankrupt") 
            return

        elif loan_amount <= Bank.available_balance:
            for i, u in enumerate(Bank.users):
                if u[0] == account_no:
                    data = list(u)
                    if data[6] is not 0:  
                        data[5] += loan_amount 
                        print(f"You have loaned {loan_amount} successfully. Now your new balance is {data[5]}.")
                        data[6] -= 1
                        if data[6] == 1: print(f"Note that, Your loan limit is now 1.")
                        Bank.users[i] = tuple(data) 
                        Bank.available_balance -= loan_amount
                        Bank.loan_amount += loan_amount
                        Bank.add_transaction(account_no, transaction_type='loan    ', transaction_amount=loan_amount) 
                        return   
                    else: 
                        print(f"Your loan limit is exist") 
                        return
            print(f"Account does not exist") 
        else: print(f"Not enough amount to give loan")

    def transfer(self, my_account_no, receiver_account_no, transfer_amount):
        if Bank.bankrupt:
            print("Bank is bankrupt") 
            return
            
        for i, m in enumerate(Bank.users):
            if m[0] == my_account_no:
                mydata = list(m) 
                if mydata[5] >= transfer_amount: 
                    for j, u in enumerate(Bank.users):
                        if u[0] == receiver_account_no:
                            receiverdata = list(u) 
                            mydata[5] -= transfer_amount
                            receiverdata[5] += transfer_amount
                            Bank.users[i] = tuple(mydata) 
                            Bank.users[j] = tuple(receiverdata) 
                            Bank.add_transaction(acccount_no=my_account_no, transferdTo=receiver_account_no, transferdAmount=transfer_amount)
                            Bank.add_transaction(acccount_no=receiver_account_no, receivedFrom=my_account_no, receivedAmount=transfer_amount)
                            print(f"Transaction done successfully")
                            return   
                    print(f"Receiver account does not exist") 
                    return
                print(f"Your have not sufficent amount to transfer") 
                return        
        print('Your account does not exist')
        

class Admin(ABC):
    def __init__(self, username, password):
        self.username = username
        self.password = password

        admin = (username, password)
        Bank.admins.append(admin)