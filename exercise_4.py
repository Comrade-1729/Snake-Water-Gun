''' 
    Secret Code Language 
'''
import random
import string

while True :
    f=input("Enter 'C' for Code , 'D' for Decode : ")
    strng = input("Enter a String : ").strip()
    c=0 # each 'strng' word start-index tracking variable
    code=""
    strng = strng + " "
    if  f.upper() == "C" :
        for i,v in enumerate(strng) :
            if v == " " : 
                if i-c == 1 :
                    code = code+strng[c] + " "
                    c = c+2
                elif i-c == 2 :
                    code = code + strng[c+1] + strng[c] + " "
                    c = c+3
                else :
                    strg = strng[c+1:i]+strng[c]
                    # Get 3 random alphabets
                    RANDOM_THREE = "".join(random.choice(string.ascii_letters) for _ in range(6))
                    code = code + RANDOM_THREE[:3] + strg + RANDOM_THREE[3:] + " "
                    # code = code + RANDOM_THREE[k:k+3] + strg + RANDOM_THREE[k+i+3-j:k+i+6-j]+" "
                    # k=k+i+7
                    c=i+1
        print(code)
    elif f.upper() == "D" :
        for i,v in enumerate(strng) :
            if v == " " :
                if i - c == 1 :
                    code = code + strng[c] + " "
                    c = i + 1
                elif i - c == 2 :
                    code = code + strng[c+1] + strng[c] + " "
                    c = i + 1
                elif i - c >= 9 :
                    strg = strng[c+3:i-3]
                    code = code + strg[len(strg)-1] + strg[:len(strg)-1] + " "
                    c = i + 1
                else :
                    print(f"{strng} is an Invalid String to Decode :( " )
                    break
        print(code)
    else :
        print(f"{f} is an Invalid Input :( ")
        break
