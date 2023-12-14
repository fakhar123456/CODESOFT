import random

def main():
    length = input(" 🔑 🔑 Enter the lenght of Password 🔑 🔑: ")
    length_pass = int(length)
    password1 = ""
    special(length_pass, password1)

def smalls(length_pass, password1):
    while length_pass > 0:
        small = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        password1 =password1 + random.choice(small)
        length_pass = length_pass - 1
        special(length_pass, password1)
        print1(length_pass, password1)
        return length_pass


def number(length_pass, password1):
    while length_pass > 0:
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        password1 =password1 + random.choice(numbers)
        length_pass = length_pass - 1
        smalls(length_pass, password1)
        print1(length_pass, password1)
        return length_pass


def capital(length_pass, password1):
    while length_pass > 0:
        capitals = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        password1 = password1 +  random.choice(capitals)
        length_pass = length_pass - 1
        number(length_pass, password1)
        print1(length_pass, password1)
        return length_pass



def special(length_pass, password1):
    while length_pass > 0:
        specials = ['!', '"', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|', '}', '~']
        password1 =password1 + random.choice(specials)
        length_pass = length_pass - 1
        capital(length_pass, password1)
        print1(length_pass, password1)
        return length_pass

def print1(length_pass, password1):
    if length_pass == 0:
        print(password1)

main()