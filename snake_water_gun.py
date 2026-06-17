#Implement a python program for snake,water,gun game

'''
snake=1
water=2
gun=3
'''

import random

comp=random.randint(1,3)
print("Welcome to Snake-Water-Gun game!")
you_str=input("Enter your choice (S/W/G):")
d1={"S":1,"W":2,"G":3}
you=d1[you_str]
d2={1:"Snake",2:"Water",3:"Gun"}
your_choice=d2[you]
comp_choice=d2[comp]
print(f"Your choice is {your_choice}\nComputer's choice is {comp_choice}")

if(comp==you):
    print("It's a draw")
else:
    if(comp==1 and you==2):
        print("You lose!")
    elif(comp==1 and you==3):
        print("You Win!")
    elif(comp==2 and you==1):
        print("You Win!")
    elif(comp==2 and you==3):
        print("You lose!")
    elif(comp==3 and you==1):
        print("You lose!")
    elif(comp==3 and you==2):
        print("You Win!")
    else:
        print("Something went wrong")