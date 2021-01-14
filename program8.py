#functions

def pypart(n):
    for i in range(0,n):
        for j in range(0, i+1):
            print("* ",end="")
        print("\r")

num = 5
pypart(num)


pypart(6)

def evenOdd( x ):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")

evenOdd(2)
evenOdd(17)

print('------')

def my_function():
    print("hello")

my_function()
my_function()

def my_function2(fname):
    print(fname + " Joseph")

my_function2("Jason")
my_function2("John")
my_function2("Linus")

def my_function3(fname, lname):
    print(fname + " " + lname)

my_function3("Jason","Joseph")
