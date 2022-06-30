import random
import string

# get number of characters
length = int(
    input("How many characters would you like your generated password to be?\n"))

# initaliaze data
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = ("!?.")

# combine data
all = lower + upper + num + symbols

temp = random.sample(all, length)

password = "".join(temp)

print(password)
