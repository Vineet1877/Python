import Account

class SavingAccount(Account.Account):
    def __init__(self, accountNumber: int, name: str):
        super().__init__(accountNumber, name, 0, 0)
        self.__intrestRate: float = 2

    def getIntrestRate(self):
        return self.__intrestRate

    def setIntrestRate(self, rate: float):
        self.__intrestRate = rate

    def intrestCalculation(self):
        intrestAmount: int = (self.getIntrestRate() / 100) * self.getBalance()
        print("***************** Saving Account ******************")
        print("Intrest rate: " + str(float(self.getIntrestRate())) + "%")
        print("Balance: " + str(self.getBalance()) + "₹")
        print("Intrest amount: " + str(int(intrestAmount)) + "₹")
        print("***************************************************")