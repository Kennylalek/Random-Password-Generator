import random
import string

def generate_password(length, spaces, digits, symbols, upper) :
    characters = string.ascii_lowercase
    if spaces :
        characters += '          '
    if digits :
        characters += string.digits
    if symbols :
        characters += string.punctuation
    if upper :
        characters += string.ascii_uppercase

    random_string = ''.join(random.choice(characters) for i in range(length))

    return random_string