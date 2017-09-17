def CtoF(Celcius):
    if Celcius < -273.15:
        return("Error")
        else:
        Fahrenheit = Celcius * (9 / 5) + 32
        return Fahrenheit

temperatures=[10,-20,-289,100]
for item in temperatures:
    print(CtoF(item))
