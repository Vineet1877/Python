def createUser(dictionary, name: str, age: int):
    dictionary[str(name)] = age

def displayUsers(dictionary):
    for user in dictionary:
        print(user + "\t" + str(dictionary.get(user)))

def separateUser(dictionary):
    array = [None, None, None, None, None, None, None, None]

    for name, age in dictionary.items():
        if 18 <= age <= 35:
            if array[0] is None or age < array[0][1]:
                array[0] = (name, age)
            if array[1] is None or age > array[1][1]:
                array[1] = (name, age)
        elif 36 <= age <= 50:
            if array[2] is None or age < array[2][1]:
                array[2] = (name, age)
            if array[3] is None or age > array[3][1]:
                array[3] = (name, age)
        elif 51 <= age <= 65:
            if array[4] is None or age < array[4][1]:
                array[4] = (name, age)
            if array[5] is None or age > array[5][1]:
                array[5] = (name, age)
        elif 66 <= age <= 90:
            if array[6] is None or age < array[6][1]:
                array[6] = (name, age)
            if array[7] is None or age > array[7][1]:
                array[7] = (name, age)

    return array
                