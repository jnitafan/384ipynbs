# import REGEX
import re

# initalize email variable
email = input("Please enter your email: ")

# note: this regex was taken from the (RFC 5322 Official Standard) General Email Regex
# this standard can be seen here https://www.ietf.org/rfc/rfc5322.txt
while bool(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)) == False:
    # ask the user for their email again
    email = input("Your email is not a valid email, enter again: ")

# split the email with regex into the groups
split = re.search(r'([a-zA-Z0-9./-]+)@([a-zA-Z0-9./-]+)', email)

# then print out with concatenation the email, username and domain
print("email: " + email + ", username: " +
      split.group(1) + ", domain: " + split.group(2))
