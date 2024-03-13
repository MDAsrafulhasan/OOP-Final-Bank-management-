# admin username = Admin
# admin password = 123

class BankAccount:
    # account_list = []
    def __init__(self,name,email,address,type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.type = type
        self.balance = 0
        self.transaction = []
        # self.account_No = len(BankAccount.account_list)+101
        self.account_No = len(Admin.user_list)+101
        self.loan = 0
        self.loan_feature = 'ON'
        # BankAccount.account_list.append(self)
        # Admin.user_list.append(self)

    def Withdraw(self,amount):
        if self.loan_feature == 'ON':
            if amount <= self.balance and amount>0:
                self.balance -= amount
                self.transaction.append(f'Withdraw : {amount}')
                print(f"\nWithdraw {amount} Successfully.New balance {self.balance}\n")
            else:
                print("\nWithdrawal amount exceeded\n")
        else:
            print("\nBank is bankrupt. Request admin to turn ON the loan feature\n")

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            self.transaction.append(f'Deposit : {amount}')
            print(f"Deposit {amount} Successfully. New balance {self.balance}\n")
        else:
            print("Invalid amount")

    def Check_available_balance(self):
        print(f"\nYour current balance is {self.balance}\n")
    
    def Transaction_history(self):
        if len(self.transaction) != 0:
            print("\nYour transaction history:")
            for val in self.transaction:
                print(val)
            print('\n')

        else:
            print("\nNo transaction available\n")

    def Take_loan(self):
        if self.loan != 2:
            self.balance+=1000
            self.transaction.append(f'Loan added: {1000}')
            self.loan+=1
            Admin.total_loan+=1000
            print(f"\nAmount added to your account. New balance is {self.balance}\n")

        else:
            print(f"\nYou don't have enough limit.Your current balnace is {self.balance}.Thank you\n")

    def Login_check(self,name,email):
        for user in Admin.user_list:
            if user.name == name and user.email == email:
                return user
        print("T\nhis account is not in out list. Thank you\n")

    
    def Transfer_amount(self,account_no,amount):
        # print('ji')
        if self.loan_feature == 'ON':
            for user in Admin.user_list:
            # for user in BankAccount.account_list:
                # print('for loop e dhuksi')
                if user.account_No == account_no:
                    # print('dhuksi')
                    user.balance+=amount
                    self.balance-=amount
                    self.transaction.append(f'Transfer amount: {amount}')
                    print(f"\nTransfer amount successfully.Your new blaance is {self.balance}\n")
                    # print(f"{user.name} ke taka dia disi")
                    return
            print("\nAccount does not exist.\n")
        else:
            print("\nBank is bankrupt. Request admin to turn ON the loan feature\n")

class Admin:
    user_list = []
    total_loan = 0
    def __init__(self) -> None:
        pass
        # self.user_list = []
        # self.total_loan = 0

    def Creat_account(self,name,email,address,type):
        user = BankAccount(name,email,address,type)
        Admin.user_list.append(user)
        return user


    def Delete_account (self,account_no):
        for user in Admin.user_list:
            if user.account_No == account_no:
                Admin.user_list.remove(user)
                print("User account deleted successfully.\n")
                return
        print("User account not found\n")

    def ALL_User_accounts_list(self):
        if len(Admin.user_list)!=0:
            for user in Admin.user_list:
                print(f'Name:{user.name}, Email:{user.email}, Address:{user.address}, Account_Type:{user.type}, Balance:{user.balance}, Account_No:{user.account_No}, Take total loan:{user.loan}, Laon_feature:{user.loan_feature}\n')
        else:
            print("Accoount list empty\n")

    
    def Total_available_balance(self):
        total = 0
        for user in Admin.user_list:
            total +=user.balance
        # total = sum(user.balance for user in Admin.user_list)
        print(f'Total balance is {total}\n')

    def Total_Loan_amount(self):
        print(f'Total loan amount is {Admin.total_loan}\n')

    def Turn_ON_or_OFF_loan(self,account_no):
        # cnt = 1
        for user in Admin.user_list:
            # print(cnt)
            # cnt+=1
            if user.account_No == account_no:
                if user.loan_feature == 'ON':
                    print(f"{user.name} loan feature is {user.loan_feature}")
                    op = input("Do you want to OFF the loan feature (yes/no) : ")
                    if op == 'yes':
                        # print("yes er por")
                        user.loan_feature = 'OFF'
                        print(f'{user.name} loan feature is now {user.loan_feature}\n')
                        return
                    else:
                        return

                elif user.loan_feature == 'OFF':
                    print(f"{user.name} loan feature is {user.loan_feature}")
                    op = input("Do you want to ON the loan feature (yes/no) : ")
                    if op == 'yes':
                        user.loan_feature = 'ON'
                        print(f'{user.name} loan feature is now {user.loan_feature}\n')
                        return
                    else:
                        return
        else:
            print(f"Invalid user account number {account_no}")

# admin = Admin()

# admin.Creat_account('sou','sou@','nar','sv')
# admin.Creat_account('cou','cou@','nar','cu')
# admin.ALL_User_accounts_list()
# admin.Turn_ON_or_OFF_loan(141)


# # # Creating user accounts
# user1 = admin.Creat_account("John Doe", "john@example.com", "123 Main St", "Savings")
# user2 = admin.Creat_account("Jane Smith", "jane@example.com", "456 Oak St", "Current")
# user2.deposit(1000)
# print(user2.balance)
# for user in admin.user_list:
#     print(user.name,user.email,user.address,user.type,user.balance,user.account_No,user.loan,user.loan_feature)

# for user in BankAccount.account_list:
#     print(user.name,user.email,user.address,user.type,user.balance,user.account_No,user.loan,user.loan_feature)

# self.email = email
# self.address = address
# self.type = type
# self.balance = 0
# self.transaction = []
# self.account_No = len(BankAccount.account_list)+101
# # self.account_No = len(Admin.user_list)+101
# self.loan = 0
# self.loan_feature = 'ON'

# user1 = Saving_account('soumick','soumick940@gmail.com','narsingdi','saving')
# user2 = Saving_account('sajib','sajib940@gmail.com','narsingdi','saving')
# # user.Check_available_balance()
# user1.deposit(1000)
# user2.deposit(1000)

# # user1.Withdraw(500)
# # user1.Withdraw(100)
# # user1.Withdraw(190)
# user1.Transfer_amount("sajib",100)
# user1.Transaction_history()
            
# admin = Admin()
# user1 = admin.Creat_account("John Doe", "john@example.com", "123 Main St", "Savings")
# user2 = admin.Creat_account("Jane Smith", "jane@example.com", "456 Oak St", "Current")

def main():
    user = None
    while True:
        print("\n-----------WELCOME TO OOP PERAMOY BANK----------\n")
        print("1.Admin")
        print("2.User")
        print("3.Exit")
        op = int(input("Choose one option: "))

        if op==1:
            name = input("Admin user name: ")
            password = int(input("Password: "))
            if name == 'Admin' and password == 123:
                user = Admin()
                print("\n--------WELCOME ADMIN--------\n")
                while True:
                    print("What you want? ")
                    print("1. Create an account")
                    print("2. Delete any user account")
                    print("3. See all user accounts list")
                    print("4. Check the total available balance")
                    print("5. Check the total loan amount")
                    print("6. Loan feature of the bank")
                    print("7. Log out")
                    option = int(input("Choose your option: "))
                    print("\n")
                    if option == 1:                                               # ekhn just option gula set kora lagbe
                        name = input("Your name: ")
                        email = input("Your email: ")
                        address = input("Your address: ")
                        Type = input("Account Type ( savings(sv) / current (cu) ): ")
                        user.Creat_account(name,email,address,Type)
                        print("Creat account successfully.\n")

                    elif option == 2:
                        account_no = int(input("Which user account you want to delete (account_no): "))
                        user.Delete_account(account_no)

                    elif option == 3:
                        user.ALL_User_accounts_list()

                    elif option == 4:
                        user.Total_available_balance()

                    elif option == 5:
                        user.Total_Loan_amount()

                    elif option == 6:
                        account_no = int(input("Which user account you want to turn on/off the loan feature (account_no): "))
                        user.Turn_ON_or_OFF_loan(account_no)

                    elif option == 7:
                        user = None
                        break
            else:
                print("Wrong username or password")

        elif op==2:
                oopp = input("Creat your account or Login (cr/lg): ")
                if oopp == 'cr':
                    name = input("Your name: ")
                    email = input("Your email: ")
                    address = input("Your address: ")
                    Type = input("Account Type ( savings(sv) / current (cu) ): ")
                    Bank = Admin()
                    # if Type == 'sv':
                    #     user = Bank.Creat_account(name,email,address,Type)
                    # else:
                    #     user = Bank.Creat_account(name,email,address,Type)
                    #     print(' current er kaj kora lagbe')
                    currentUser = Bank.Creat_account(name,email,address,Type)
                    user = currentUser
                else:
                    name = input("Inter your username: ")
                    email = input("Inter your email: ")
                    currentUser = BankAccount.Login_check(user,name,email)
                    user= currentUser

                if user != None:
                    print(f"\n------WELCOME {user.name}------\n")
                    while True:
                        
                        print("What you want?")
                        print("1.Deposit money")
                        print("2.Withdraw money")
                        print("3.Available balance")
                        print("4.Transaction history")
                        print("5.Transfer money")
                        print("6.Take loan")
                        print("7.Log out")
                        opp = int(input("Choose one option: "))

                        if opp==1:
                            amount = int(input("How much money you want to deposit: "))
                            user.deposit(amount)

                        elif opp==2:
                            amount = int(input("How much money you want to Withdraw: "))
                            user.Withdraw(amount)

                        elif opp==3:
                            user.Check_available_balance()

                        elif opp==4:
                            user.Transaction_history()

                        elif opp==5:
                            acount_no = int(input("\nGive me the account number of whome you want to send money: "))
                            amount = int(input("How much money you want to send: "))
                            if amount>user.balance:
                                print("You dont have enough money to send")
                            else:
                                user.Transfer_amount(acount_no,amount)                        

                        elif opp==6:
                            user.Take_loan()


                        elif opp==7:
                            user = None
                            break
                else:
                    print("\nInvalid account\n")
        elif op==3:
            break

if __name__ == '__main__':
    main()