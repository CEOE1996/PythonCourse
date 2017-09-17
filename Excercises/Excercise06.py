import os
import datetime

Carpeta = "./Excercise06Files"
dir = os.listdir(Carpeta)
with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as nuevo:
    for archivo in dir:
        with open(Carpeta + '/' + archivo, 'r') as file:
            nuevo.write(file.read() + "\n")
