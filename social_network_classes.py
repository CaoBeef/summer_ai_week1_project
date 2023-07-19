SocialNetwork = []

# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
#class SocialNetwork:
 #   def __init__(self):
   #     self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
  #  def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
   #     pass

    ## For more challenge try this
  #  def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
   #     pass

   # def  create_account(self):
        #implement function that creates account here
       # print("Creating ...")
        #pass


class Person():
    def __init__(self,user_id,age,password,friendlist,receivedmessages,sentmessages):
        self.user_id = user_id
        self.age = age
        self.password = password
        self.friendlist = friendlist
        self.receivedmessages = receivedmessages
        self.sentmessages = sentmessages

    def create_account(self,new_name,new_age,new_password,new_friendlist,new_received_messages,new_sent_messages):
        SocialNetwork.append(Person(new_name,new_age,new_password,[],[],[]))
    
    def add_friend(self,new_friend):
        #implement adding friend. Hint add to self.friendlist
        self.friendlist.append(new_friend)
    
    def view_all_friends(self,username):
        for persona in SocialNetwork:
            if (persona.user_id == username):
                for friend in persona.friendlist:
                    print(friend)
    
    def block_friend(self,blocked_friend):
        self.friendlist.remove(blocked_friend)
        self.blockedlist.append(blocked_friend)
    
    def send_message(self,message):
        #implement sending message to friend here
        self.receivedmessages.append(message)
    
    def all_sent_messages(self,sent_message):
        self.sentmessages.append(sent_message)