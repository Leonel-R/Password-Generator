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

generate_strong_password(10,True,True)
