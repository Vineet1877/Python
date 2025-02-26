class Account:
    def __init__(self, accountNumber: int, name: str, time: int, amount: int):
        self.__accountNumber = accountNumber
        self.__name = name
        self.__time = time
        self.__balance = amount

    def getAccountNumber(self):
        return self.__accountNumber

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getBalance(self):
        return self.__balance

    def setBalance(self, amount: int):
        self.__balance = amount

    def getTime(self):
        return self.__time

    def setTime(self, time):
        self.__time = time

    def depositAmount(self, amount: int):
        self.setBalance(self.getBalance() + amount)
        print(str(amount) + " Deposited")
        print("Balance = " + str(self.getBalance()))

    def depositAmount(self, amount: int, time: int):
        if time > 0:
            print("Can't deposit money ")
            return

        self.setBalance(self.getBalance() + amount)
        print(str(amount) + " Deposited")
        print("Balance = " + str(self.getBalance()))

    def withdrawalAmount(self, amount: int):
        if self.__time > 0:
            print("Can't withdrawn money " + str(self.__time) + " Year Remaining for maturity")
            return

        newBalance = self.getBalance() - amount
        if newBalance < 0:
            print("Can't withdrawn money, Please check the balance")
        else:
            self.setBalance(self.getBalance() - amount)
            print(str(amount) + " Withdrawn")
            print("Balance = " + str(self.getBalance()))

    def balanceInquiry(self):
        print("******************* Account ********************")
        print("Account number: " + str(self.getAccountNumber()))
        print("Name: " + self.getName())
        print("Balance: " + str(self.getBalance()))
        print("************************************************")