import userController

users = []

while True:
    print("****************** choices ********************")
    print("1. Create user")
    print("2. Search by id")
    print("3. Search by name")
    print("4. List users")
    print("5. Remove user")
    print("**********************************************")

    choice = int(input("Enter choice: "))
    if choice == 1:
        userController.create(users)
    elif choice == 2:
        userController.searchById(users, int(input("Enter userId: ")))
    elif choice == 3:
        userController.searchByName(users, str(input("Enter userName: ")))
    elif choice == 4:
        userController.listUsers(users)
    elif choice == 5:
        userController.remove(users, int(input("Enter userId: ")))
    else:
        print("Invalid input")