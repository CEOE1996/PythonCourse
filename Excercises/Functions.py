def Format(word, char = ':', len = 2):
    new_string = ''
    for i in range(0 ,len(word), len):
        new_string += word[i:i+len] + char
    return new_string[:-1].upper()

print(Format("Hello World", "."))
