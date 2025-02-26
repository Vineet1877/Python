class Book:
    def __init__(self, name: str, authorName: str):
        self.__name = name
        self.__authorName = authorName

    def getName(self):
        return self.__name

    def setName(self, name: str):
        self.__name = name

    def getAuthorName(self):
        return self.__authorName

    def setAuthorName(self, authorName: str):
        self.__authorName = authorName