import time
hour=time.strftime('%H')
print(hour)

if hour>0 and hour<12 :
    print("Hello sir, Good Morning")
elif hour>12 and hour<17 :
    print("Hello sir, Good afternoon Sir")
elif hour>=17 and hour<0 :
    print("Good night sir")
