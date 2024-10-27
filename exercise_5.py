'''
    Snake, Water & Gun
'''
import random
l1 = ['S','W','G']
l2 = [['Draw','Win','Loss'],['Loss','Draw','Win'],['Win','Loss','Draw']]
def result(u,c) :
    ''' Function top  '''
    u = l1.index(u)
    c = l1.index(c)
    return l2[u][c]
def main():
    ''' The Main Function '''
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
if __name__ == '__main__':
    main()
