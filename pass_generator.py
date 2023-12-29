#!/usr/bin/python3

import random
import string


length = int(input("How long do you want your password? "))
characters = string.ascii_letters + string.digits + string.punctuation
password = "".join([random.choice(characters) for char in range(length)])

print(password)
