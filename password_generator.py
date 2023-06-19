# Write your solution here
from string import *
from random import *

def generate_strong_password(length: int,number: bool,special: bool):
    random_pass = ""
    special_characters = "!?=+-()#"
    for letter in range(length):
        if number is True and special is False:
            random_pass += choice((choice(ascii_letters),choice(digits)))
            
        elif number is False and special is True:
            random_pass += choice((choice(ascii_letters),choice(special_characters)))
            
        elif number is True and special is True:
            random_pass += choice((choice(ascii_letters),choice(special_characters),choice(digits)))
            
        else:
            random_pass += choice(ascii_letters)
    print(random_pass)

length = int(input("Please input the desired length of password:"))
bool1 = input("Do you want numbers in your password(y/n):")
if bool1 == "y":
    number = True
else:
    number = False

bool2 = input("Do you want special characters in your password(y/n):")
if bool2 == "y":
    special = True
else:
    special = False




generate_strong_password(length,number,special)
