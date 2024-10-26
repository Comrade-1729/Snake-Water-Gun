''' 
    Secret Code Language 
'''
import random
import string

def random_letters(n=6):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

def code_word(word):
    if len(word) == 1:
        return word
    elif len(word) == 2:
        return word[::-1]
    else:
        random_three = random_letters()
        return random_three[:3] + word[1:] + word[0] + random_three[3:]

def decode_word(word):
    if len(word) == 1:
        return word
    elif len(word) == 2:
        return word[::-1]
    elif len(word) >= 9:
        return word[-4] + word[3:-4]
    return None

def process_string(strng, mode):
    words = strng.split()
    if mode == 'C':
        return ' '.join(code_word(word) for word in words)
    elif mode == 'D':
        decoded = [decode_word(word) for word in words]
        if None in decoded:
            return f"{strng} is an Invalid String to Decode :("
        return ' '.join(decoded)

while True:
    mode = input("Enter 'C' for Code, 'D' for Decode: ").upper()
    if mode not in ['C', 'D']:
        print(f"{mode} is an Invalid Input :(")
        break
    strng = input("Enter a String: ").strip()
    result = process_string(strng, mode)
    print(result)
