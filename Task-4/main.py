import random
import util

numbers: list[int] = []
for i in range(1000):
    num = random.randint(1, 1000)
    numbers.append(num)

print("Even numbers: " + str(util.getEven(numbers)))
print("Multiplier of 17: " + str(util.multiplier(numbers)))
print("Greater numbers: " + str(util.greaterNumbers(numbers,int(input("Enter any number: ")))))