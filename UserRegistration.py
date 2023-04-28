import random
import re

while True:
    # USERNAME
    username = input('Enter a username (only alphanumeric characters): \n')

    while not re.match("^[a-zA-Z0-9]*$", username):
        print('Username can only consist of alphanumeric characters. Please try again.')
        username = input('Enter a username (only alphanumeric characters): \n')

    # PASSWORD
    password_pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    password = input('Enter a password \nmust be at least 8 characters long \ncontain at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character:\n ')
    reentered_password = input('Re-enter the password to confirm: \n')

    while password != reentered_password or not re.match(password_pattern, password):
        print('Passwords do not match or do not meet the requirements. Please re-enter.\n')
        password = input('Enter a password \nmust be at least 8 characters long \ncontain at least 1 uppercase, 1 lowercase, 1 digit, and 1 special character:\n ')
        reentered_password = input('Re-enter the password to confirm: \n')

    # CAPTCHA
    captcha = str(random.randint(1000, 9999))
    user_captcha = input(f'Enter the captcha: {captcha} ')

    while user_captcha != captcha:
        print('Captcha does not match. Please try again.')
        user_captcha = input(f'Enter the captcha: {captcha} ')

    # COMPLETED
    print('Registration successful.')
    break
