import SavingAccount
import DepositAccount
import  random

while True:
    print("************** Choices ****************")
    print("1. Create Saving Account")
    print("2. Create Deposit Account")
    print("0. quit")

    choice = int(input("Enter choice: "))
    if choice == 1:
        accountNumber = random.randint(111111, 999999)
        name = str(input("Enter name: "))
        account: SavingAccount = SavingAccount.SavingAccount(accountNumber, name)
    elif choice == 0:
        break
    else:
        accountNumber = random.randint(111111, 999999)
        name = str(input("Enter name: "))
        time = int(input("Enter time span: "))
        balance = int(input("Enter amount: "))
        account: DepositAccount = DepositAccount.DepositAccount(accountNumber, name, time, balance)

    while True:
        print("************** Choices ****************")
        print("1. Withdrawn")
        print("2. Deposit")
        print("3. Balance inquiry")
        print("4. Intrest calculation")

        choice = int(input("Enter choice: "))
        if choice == 1:
            amount = int(input("Amount: "))
            account.withdrawalAmount(amount)
        elif choice == 2:
            amount = int(input("Amount: "))
            account.depositAmount(amount, account.getTime())
        elif choice == 3:
            account.balanceInquiry()
        elif choice == 4:
            account.intrestCalculation()
        else:
            break