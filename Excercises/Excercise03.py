def CtoF(Celcius):
    Fahrenheit = Celcius * (9 / 5) + 32
    return Fahrenheit

Celcius = float(input("Enter Celcius: "))

if Celcius > -273.15:
    print(CtoF(Celcius))
else:
    print("Error")
