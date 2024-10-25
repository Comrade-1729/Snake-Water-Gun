""" 
    Greeting the User 
"""
import time

name=input("Enter your name : ").title()
hour=int(time.strftime('%H'))

if 4 <= hour < 12:
    print("Good Morning",name)
if 12 <= hour < 17:
    print("Good Afternoon",name)
if 17 <= hour < 21:
    print("Good Evening",name)
else:
    print("Good Night",name)
