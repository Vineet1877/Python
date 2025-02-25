def getEven(numbers: list[int]):
    evenNumbers: list[int] = []
    for number in numbers:
        if number % 2 == 0:
            evenNumbers.append(number)

    return evenNumbers

def multiplier(numbers: list[int]):
    seventeenMul: list[int] = []
    for number in numbers:
        if number % 17 == 0:
            seventeenMul.append(number)

    return seventeenMul

def greaterNumbers(numbers: list[int], num: int):
    greaterList: list[int] = []
    for number in numbers:
        if number > num:
            greaterList.append(number)

    return greaterList