import datetime

filename = datetime.datetime.now()

def CreateFile():
    with open(filename.strftime("%Y-%m-%d-%H-%M") + ".txt", "w") as file:
        file.write("")

CreateFile()
