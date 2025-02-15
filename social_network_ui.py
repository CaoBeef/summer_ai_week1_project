# You can implement user interface functions here.
from social_network_classes import SocialNetwork,Person

def userLogin():
    login_name = input("What is your name? ")
    login_password = input("What is your password? ")
    able_login = False
    for object in SocialNetwork:
        if (object.user_id == login_name):
            print("Login Successful!")
            able_login = True
            break
    if able_login == False:
        print("Login Unsuccessful!")
    return able_login

def createAccount():
    create_userid = input("What name would you like to use to create your account? ")
    create_age = int(input("What is your current age? "))
    create_password = input("What is your password? (Don't share this with anyone!) ")
    able_create = False
    while not able_create:
        for object1 in SocialNetwork:
            if (object1.user_id == create_userid):
                print("Name is already in use!")
                able_create = True
        if able_create == False:
            person = Person(create_userid,create_age,create_password,[],[],[])
            person.create_account(create_userid,create_age,create_password,[],[],[])
            able_create = True

def mainMenu():
    print("")
    print("########################################################")
    print("1. Create New Account")
    print("2. Manage Account")
    print("3. Quit")
    print("########################################################")
    return input("Please Choose a number: ")

def manageAccountMenu():
    print("")
    print("1. Edit my details")
    print("2. Add a friend")
    print("3. View all my friends")
    print("4. Block a friend")
    print("5. Send a message")
    print("6. View all messages sent to me")
    print("7. View all messages sent by me")
    print("8. <- Go Back")
    return input("Please Choose a number: ")