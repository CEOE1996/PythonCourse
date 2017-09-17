# define the function blocks
def zero(param):
    print("You typed zero.\n")
    print(param)

def sqr():
    print("n is a perfect square\n")

def even():
    print ("n is an even number\n")

def prime():
    print( "n is a prime number\n")

param = 40
# map the inputs to the function blocks
options = {0 : zero,
           1 : sqr,
           4 : sqr,
           9 : sqr,
           2 : even,
           3 : prime,
           5 : prime,
           7 : prime,
}

options[0](param)
