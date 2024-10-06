from Users import Bank, Users, Admin

run = True
while run:
    print("Select your role:")
    print("1. User")
    print("2. Admin") 
    print("3. Exit") 


    role = int(input("Enter 1 or 2 as your role: "))
    if role == 1:
        print("---------------------")
        print("1. Create an account") 
        print("2. Deposit amount") 
        print("3. Withdraw amount") 
        print("4. Available balance")
        print("5. Transaction history") 
        print("6. Request for LOAN")
        print("7. Transfer amount to others") 

        role1op = int(input("Enter your option: "))
        if role1op == 1:
            name = input("Name: ")
            email = input("Email: ")
            address = input("Address: ")
            account_type = int(input("1 for savings and 2 for current: "))
            account = Users(name, email, address, account_type)  
            print(f"Welcome {name}, Your {account.account_type} account number is {len(Bank.users)}")

        elif role1op == 2:
            account_no = int(input("Enter account number: "))
            deposit_amount = int(input("Enter amount: ")) 
            account.deposit(account_no, deposit_amount)
        
        elif role1op == 3:
            account_no = int(input("Enter account number: "))
            withdraw_amount = int(input("Enter amount: ")) 
            account.withdraw(account_no, withdraw_amount) 

        elif role1op == 4:
            account_no = int(input("Enter account number: "))
            account.available_balance(account_no) 

        elif role1op == 5:
            account_no = int(input("Enter account number: "))
            account.transaction_history(account_no) 
            
        elif role1op == 6:
            account_no = int(input("Enter account number: "))
            loan_amount = int(input("Enter LOAN Amount: "))
            account.loan(account_no, loan_amount) 
            
        elif role1op == 7:
            my_account_no = int(input("Enter your account number: "))
            receiver_account_no = int(input("Enter receiver account number: "))
            transfer_amount = int(input("Enter transfer amount: "))
            account.transfer(my_account_no, receiver_account_no, transfer_amount)
        
        
    elif role == 2:
        print("1. Create an account")
        print("2. Delete any account")
        print("3. All users accounts list")
        print("4. Total available balance")
        print("5. Total Transaction history") 
        print("6. Total LOAN amount")
        print("7. Change LOAN feature / Declare BANKRUPT") 

        role2op = int(input("Enter your option: "))
        if role2op == 1:
            username = input("Username: ")
            password = input("Password: ")
            admin = Admin(username, password)
            print(f"{username}, Your admin account created successfully!!!")

        elif role2op == 2:
            account_no = int(input("User account no to delete: "))

            deleteDone = False
            for i, u in enumerate(Bank.users):
                if u[0] == account_no:
                    deleteDone = True
                    Bank.users.pop(i) 
                    break
            
            if deleteDone: print(f"{account_no} no account has been deleted successfully")
            else: print('There is no account for delete')
            
        elif role2op == 3:
            print(f"Account No \tAccount Type \tAccount Holder \tEmail \t\t\tAddress \tAmount\tLoan Limit") 
            for u in Bank.users:
                print(f'{u[0]}\t\t{u[1]}\t\t{u[2]}\t\t{u[3]}\t\t{u[4]} -- {u[5]}\t{u[6]}')   

        elif role2op == 4:
            print(f"Available balance of bank: {Bank.available_balance}")

        elif role2op == 5:
            print("Account NO \tTransaction Type \tTransaction Amount \tTransferd To \tTransfer Amount \tReceived From \tReceived Amount")
            for t in Bank.transaction_history:
                print(f"{t[0]}\t\t{t[1]}\t\t{t[2]}\t\t\t\t{t[3]}\t\t\t{t[4]}\t\t\t{t[5]}\t\t{t[6]}")
            
        elif role2op == 6:
            print(f"Total LOAN amount: {Bank.loan_amount}")

        elif role2op == 7: 
            choice = input("on - To declare BANKRUPT or \noff - To give the loan feature \nType here: ")
            
            if choice == 'on': 
                Bank.bankrupt = 1
                print("BANKRUPT mode is ON")            
            elif choice == 'off': 
                Bank.bankrupt = 0
                print("BANKRUPT mode is OFF")  
            else: print("you entered wrong option. type only (on) or (off)")            

    else:
        exit() 
