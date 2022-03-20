import random
import string


def generate_random_letters_and_digits_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def generate_random_digit_string(length):
    rand_string = ''.join(random.sample(string.digits, length))
    return rand_string
