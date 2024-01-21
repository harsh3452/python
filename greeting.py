import time
timestamp = time.strftime('%H:%M:%S')
print("Here is your Local Time : ",timestamp)
hour = int(time.strftime('%H'))
if(hour > 4 and hour < 6):
    print("Very Good Morning")
if(hour > 6 and hour < 12):
    print("Good Morning!")
if(hour > 12 and hour < 16):
    print("Good Afternoon!") 
if(hour > 16 and hour < 20):
    print("Good Evening!") 
if(hour > 20 or hour < 4):
    print("Good Night")
