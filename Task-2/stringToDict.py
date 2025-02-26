def convert(array: list[str]):
    dictionary = {}

    for i in range(len(array)):
        dictionary[i] = str(array[i])

    return dictionary