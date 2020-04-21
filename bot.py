
import fbchat 
import lyricwikia
from getpass import getpass 
username = str(raw_input("Username: ")) 
client = fbchat.Client(username, getpass()) 
no_of_friends = int(raw_input("Number of friends: ")) 
for i in xrange(no_of_friends): 
    name = str(raw_input("Name: ")) 
    friends = client.searchForUsers(name)  # return a list of names 
    friend = friends[0] 
    print(friends)
    case = int(raw_input("1 for Lyrics, 2 for personal message:"))
    if case == 1:
        lyrics = lyricwikia.get_lyrics('Eminem', 'Mockingbird')
        lyrics = lyrics.split(" ")
        for word in lyrics:
            sent = client.sendMessage(word, thread_id=friend.uid) 
        if sent: 
            print("Message sent successfully!") 
    else:
        msg = str(raw_input("Message: ")) 
        n = int(raw_input("No. of times: "))
        for i in range(0,n):
            sent = client.sendMessage(msg, thread_id=friend.uid) 
        if sent:
            print("Message sent successfully")    
