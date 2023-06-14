# Write your solution here
from string import *
from random import *

def generate_password(length: int):
    random_pass = ""
    for letter in range(length):
        random_pass += choice(ascii_lowercase)
    return random_pass

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(2))
