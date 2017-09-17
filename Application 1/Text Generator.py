import string, random

vowels = 'aeiouy'
consonants = 'bcdfhjklmnpqrstvwxz'

def Generator(choice):
    if choice == 'v':
        Letter = random.choice(vowels)
    elif choice == 'c':
        Letter = random.choice(consonants)
    elif choice == 'l':
        Letter = random.choice(string.ascii_lowercase)
    else:
        Letter = choice
    return(Letter)

Letter1 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
Letter2 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")
Letter3 = input("What letter do you want? Enter 'v' for vowels, 'c' for consonants or 'l' for any letter: ")

for i in range(20):
    L1 = Generator(Letter1)
    L2 = Generator(Letter2)
    L3 = Generator(Letter3)

    print(L1 + L2 + L3)
