def CtoF(Celcius):
    Fahrenheit = Celcius * (9 / 5) + 32
    return Fahrenheit

Celcius = float(input("Enter Celcius: "))
print(CtoF(Celcius))
