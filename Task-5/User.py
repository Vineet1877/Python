import Book

class User:
    def __init__(self, userId: int, name: str, luckyNumber: int, hobbies: list[str], books: list[Book]):
        self.__userId = userId
        self.__name = name
        self.__luckyNumber = luckyNumber
        self.__hobbies = hobbies
        self.__books = books

    def getUserId(self):
        return self.__userId

    def setUserId(self, userId: int):
        self.__userId = userId

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getLuckyNumber(self):
        return self.__luckyNumber

    def setLuckyNumber(self, luckyNumber: int):
        self.__luckyNumber = luckyNumber

    def getHobbies(self):
        return self.__hobbies

    def setHobbies(self, hobbies: list[str]):
        self.__hobbies = hobbies

    def getBooks(self):
        return self.__books

    def setBooks(self, books: list[Book]):
        self.__books = books

    def display(self):
        print("userId: " + str(self.__userId))
        print("name: " + self.__name)
        print("luckyNumber: " + str(self.__luckyNumber))
        print("hobbies: " + str(self.__hobbies))
        print("----------------- Books ------------------")
        for book in self.__books:
            print(book.getName() + " | " + book.getAuthorName())
        print("------------------------------------------")
