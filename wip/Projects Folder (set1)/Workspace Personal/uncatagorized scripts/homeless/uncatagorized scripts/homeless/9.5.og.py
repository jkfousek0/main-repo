# var = amount of messages
var = 1
tmobile = 1
condition = True
print("Messages: You have 4 new messages.")
while var < 5:
    print("unread" or "You have no unread messages.")
    var += 1
# read or unread values 
var_two = 1
while var_two < 1:
    var_two = True
    print("read messsage" if var_two is True else "You have no read messages." )
var_two += 1
tmobile = True
print("service on, tmobile") if tmobile is True else tmobile is False
print("service off") if tmobile is False else tmobile is True 
condition = False 
print("WiFi Disconnected" if condition is False else "WiFi Connected")
