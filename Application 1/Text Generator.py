import string, random

def Generator():
    L1 = random.choice(string.ascii_lowercase)
    L2 = random.choice(string.ascii_lowercase)
    L3 = random.choice(string.ascii_lowercase)
    return(L1 + L2 + L3)

print(Generator())
