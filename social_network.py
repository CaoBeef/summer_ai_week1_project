from social_network_classes import SocialNetwork, Person
import social_network_ui

ai_social_network = SocialNetwork()

if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")

    while True:
        choice = social_network_ui.mainMenu()

        if choice == '1':
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == '2':
            inner_menu_choice = social_network_ui.manageAccountMenu()
            if login_bool == True:
                manage_choice = social_network_ui.manageAccountMenu()
                # Handle inner menu here
            else:
                continue
            if manage_choice == '8':
                continue
            else:
                if manage_choice == '1':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    updated_userid = input("What would you like your new user ID to be? ")
                    updated_age = int(input("What would you like your new age to be? "))
                    updated_password = input("What would you like your new password to be? ")
                    updated_user_found = False
                    for person in ai_social_network:
                        if person.user_id == updated_userid:
                            print("This username is already in use!")
                            updated_user_found = True
                            break
                    if not updated_user_found:
                        for index in range(len(ai_social_network)):
                            if (ai_social_network[index].user_id == current_userid) and (ai_social_network[index].password == current_password):
                                ai_social_network[index] = Person(updated_userid, updated_age, updated_password, ai_social_network[index].friendlist, ai_social_network[index].receivedmessages, ai_social_network[index].sentmessages)
                                print("User info successfully updated!")
                                updated_user_found = True
                                break
                        if not updated_user_found:
                            print("Couldn't update user credentials!")

                elif manage_choice == '2':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    new_friend = input("What is the username of the friend you'd like to add? ")
                    user_exist = False
                    current_object = None
                    current_index = None
                    for person1 in ai_social_network:
                        if (person1.user_id == current_userid) and (person1.password == current_password):
                            user_exist = True
                            current_object = person1
                            current_index = ai_social_network.index(person1)
                            break
                    if not user_exist:
                        print("Incorrect credentials!")
                    else:
                        friend_exist = False
                        for person2 in ai_social_network:
                            if person2.user_id == new_friend:
                                if person2.user_id not in current_object.friendlist:
                                    current_object.add_friend(new_friend)
                                    ai_social_network[current_index] = current_object
                                    print("Friend added successfully!")
                                else:
                                    print("Friend already added!")
                                friend_exist = True
                                break
                        if not friend_exist:
                            print("Error! Make sure the friend exists!")
                
                elif manage_choice == '3':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    found_object = False
                    for person3 in ai_social_network:
                        if (person3.user_id == current_userid) and (person3.password == current_password):
                            for element in person3.friendlist:
                                print(element)
                            found_object = True
                            break
                    if not found_object:
                        print("Couldn't find user!")
                
                elif manage_choice == '4':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    blocked_friend = input("What is the username of the user you'd like to block? ")
                    found_blocked = False
                    for index2, person in enumerate(ai_social_network):
                        if (person.user_id == current_userid) and (person.password == current_password):
                            if blocked_friend in person.friendlist:
                                person.friendlist.remove(blocked_friend)
                                print("Friend Blocked!")
                                found_blocked = True
                                break
                    if not found_blocked:
                        print("Couldn't find user or incorrect credentials!")
                
                elif manage_choice == '5':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    found_recipient = False
                    sender_object = None
                    for person1 in ai_social_network:
                        if (person1.user_id == current_userid) and (person1.password == current_password):
                            sender_object = person1
                            message = input("What is the message you'd like to send? ")
                            recipient = input("What is the username of the recipient? ")
                            for person2 in ai_social_network:
                                if (person2.user_id == recipient):
                                    person2.send_message(f'{current_userid}: {message}')
                                    person1.all_sent_messages(f'{current_userid}: {message}')
                                    print("Message sent successfully!")
                                    found_recipient = True
                                    break
                    if not found_recipient:
                        print("Sorry! Could not send the message!")
                
                elif manage_choice == '6':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    found_user = False
                    for person3 in ai_social_network:
                        if (person3.user_id == current_userid) and (person3.password == current_password):
                            found_user = True
                            for message in person3.receivedmessages:
                                print(message)
                            break
                    if not found_user:
                        print("Couldn't find user!")
                
                elif manage_choice == '7':
                    current_userid = input("What is your username? ")
                    current_password = input("What is your password? ")
                    found_user = False
                    for person3 in ai_social_network:
                        if (person3.user_id == current_userid) and (person3.password == current_password):
                            found_user = True
                            for message in person3.sentmessages:
                                print(message)
                            break
                    if not found_user:
                        print("Couldn't find user!")
                
        elif choice == '3':
            break