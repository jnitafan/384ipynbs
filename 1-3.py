# grab input from the user, and convert it into an interger
number = int(input("please input number: "))

# force user into a loop until they enter a positive interger
while number < 0:
    number = int(input("please enter an integer greater than 0: "))

# print a square as big as big as required
square = str("")

for x in range(number):
    for y in range(number):
        square = square + "* "
    square = square + "\n"

print(square)
