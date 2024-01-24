import time
import os
import winsound

print("Countdown")
i=int(input("Enter the time: "))
while(i>0):
    print(i)
    time.sleep(1)
    i=i-1
    os.system('cls')
    winsound.Beep(2500,100)
    
winsound.Beep(2500,1000)    
print("You can proceed further")
