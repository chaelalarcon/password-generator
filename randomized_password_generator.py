# import a function to randomize and a string
import random
import string

# declare a function and initialize a variable
def password_gen (length = 12):
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    for i in range (length):
        password += random.choice (characters)
    return password