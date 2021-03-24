# grab input from the user, and convert it into an interger
number = int(input("please input number: "))

# force user into a loop until they enter a positive interger
while number < 0:
    number = int(input("please enter an integer greater than 0: "))

# square the input
number = number ** 2
# print the squared input
print(number)
