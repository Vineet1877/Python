import User

def create(users: list, user: User):
    users.append(user)
    return users

def searchById(users: list, userId: int):
    for user in users:
        if user.getUserId() == userId:
            return user

def searchByName(users: list, userName: str):
    for user in users:
        if user.getName() == userName:
            return user

def listUser(users: list):
    for user in users:
        user.display()

def remove(users: list, userId: int):
    for i in range(len(users)):
        if users[i].getUserId() == userId:
            del users[i]