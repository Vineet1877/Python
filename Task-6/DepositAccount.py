import Account

class DepositAccount(Account.Account):
    def __init__(self, accountNumber: int, name: str, time: int, amount: int):
        super().__init__(accountNumber, name, time, amount)
        self.__intrestRate: float = 4.95

    def getIntrestRate(self):
        return self.__intrestRate

    def setIntrestRate(self, rate: float):
        self.__intrestRate = rate

    def intrestCalculation(self):
        intrestAmount: int = (self.getIntrestRate() / 100) * self.getBalance() * self.getTime()
        print("***************** Deposit Account ******************")
        print("Intrest rate: " + str(float(self.getIntrestRate())) + "%")
        print("Balance: " + str(self.getBalance()) + "₹")
        print("Intrest amount: " + str(int(intrestAmount)) + "₹")
        print("Time span: " + str(self.getTime()))
        print("Total amount: " + str(intrestAmount + self.getBalance()))
        print("***************************************************")
