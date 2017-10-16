import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    sw = get_close_matches(word, data.keys())
    if word in data:
        return data[word]

    elif len(sw) > 0:
        yn = input("Did you mean %s?\nY = Yes, N = No: " % sw[0])

        if yn.upper() == 'Y':
            return data[sw[0]]
        elif yn.upper() == 'N':
            return "The word doesn't exists"
        else:
            return "Wrong answer"
    else:
        return "The word doesn't exists"

word = input("Enter your Word: ")

r = translate(word)

if type(r) == list:
    for w in r:
        print(w)
else:
    print(r)
#print(type(translate(word)))
