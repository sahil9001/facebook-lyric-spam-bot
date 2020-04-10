
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
    msg = str(raw_input("Message: ")) 
    lyrics = lyricwikia.get_lyrics('Eminem', 'Mockingbird')
    lyrics = lyrics.split(" ")
    for word in lyrics:
   	    sent = client.sendMessage(word, thread_id=friend.uid) 
    if sent: 
        print("Message sent successfully!") 

