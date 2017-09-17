temperatures=[10,-20,-289,100]
with open('temperatures.txt', 'w') as file:
    for Celcius in temperatures:
        if Celcius > -273.15:
            Fahrenheit = Celcius * (9 / 5) + 32
            file.write(str(Celcius) + "\n")
