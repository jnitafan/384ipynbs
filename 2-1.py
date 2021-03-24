# define the fibonacci function
def fibonacci(x):
    # initalize a list with the two starting numbers, 0 and 1
    array = [0, 1]
    # edge case to remove a number if the user decides to input 1 or 0
    if x == 1:
        del array[1]
    elif x == 0:
        array = []
    # if not, then proceed to iterate on the sequence
    else:
        # iterate as much times ("range(x)") as required
        # range(x - 2) because there are already two numbers inside the array
        for i in range(x - 2):
            # add in the new number to the end of the sequence
            array.append(array[i] + array[i+1])

    return array


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

# print the returned value of the function
print(fibonacci(number))
