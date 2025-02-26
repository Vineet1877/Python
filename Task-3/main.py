import util

dictionary = {}

while True:
    print("***** Choices *****")
    print("1. Create user")
    print("2. Display user")
    print("3. Separate user")

    choice = int(input("Enter choice: "))
    if choice == 1:
        util.createUser(dictionary, str(input("Enter name: ")), int(input("Enter age: ")))
    elif choice == 2:
        util.displayUsers(dictionary)
    elif choice == 3:
        separateUser = util.separateUser(dictionary)
        print(separateUser)
    else:
        continue