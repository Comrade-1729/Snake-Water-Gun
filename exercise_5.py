'''
    Snake, Water & Gun Game
'''
import random
l1 = ['S','W','G']
l2 = [['Draw','Win','Loss'],['Loss','Draw','Win'],['Win','Loss','Draw']]
def result(user,comp) :
    u = l1.index(user)
    c = l1.index(comp)
    return l2[u][c]
while True :
    user = input("Choose 'S' for Snake, 'W' for Water or 'G' for Gun : ").upper()
    if user in l1 :
        comp = random.choice(l1)
        print("Jarvis Chooses : ",comp)
        res=result(user,comp)
        print(res)
    else :
        print("Invalid Choice :(")
        break
