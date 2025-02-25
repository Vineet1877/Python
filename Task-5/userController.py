import random
import Book
import User
import userService

def create(users: list):
    userId: int = random.randint(1, 10000)
    userName: str = str(input("Enter name: "))
    luckyNumber: int = int(input("Enter lucky number: "))

    n = int(input("How many hobby you want to enter: "))
    hobbies: list[str] = []
    for i in range(n):
        hobbies.append(str(input("Enter hobby: ")))

    n = int(input("How many books you want to enter: "))
    books = []
    for i in range(n):
        name = input("Enter book name: ")
        authorName = input("Enter authorName: ")
        book = Book.Book(name, authorName)
        books.append(book)

    user = User.User(userId, userName, luckyNumber, hobbies, books)
    users.append(user)
    print("User created!!!")

def searchById(users: list, userId: int):
    user = userService.searchById(users, userId)
    if user is None:
        print("404 User not found")
    else:
        user.display()

def searchByName(users: list, name: str):
    user = userService.searchByName(users, name)
    if user is None:
        print("404 User not found")
    else:
        user.display()

def listUsers(users: list):
    userService.listUser(users)

def remove(users: list, userId: int):
    user = userService.searchById(users, userId)
    if user is None:
        print("404 User not found")
    else:
        user.display()
        userService.remove(users, userId)
        print(user.getName() + " is Removed")