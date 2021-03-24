# array has to be outside due to recursive functions
array = []


def fibonacci(x):
    # define the fibonacci function
    # base value 0
    if x == 0:
        return 0
    # base value 1
    if x == 1:
        return 1
    # recursive function for fibbonaci, calculated up to number
    else:
        return fibonacci(x-1) + fibonacci(x-2)


# initalize a input variable, set to null
number = None
# check if input is a integer, and bigger than 0
while isinstance(number, int) == False or number < 0:
    # ask the user for a positive integer
    try:
        number = int(input("Please enter a positive integer: "))
    # if the input is not an interger, just try again
    except ValueError:
        pass

# for every number inside the sequence length specified
for i in range(number):
    # generate the number for that index
    array.append(fibonacci(i))

# then print the array
print(array)
