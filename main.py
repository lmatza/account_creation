import random
import os
import sys

pw_lst = ['123', '321']

enter_name = input('Enter your name: ')
enter_email = input('Enter your email: ')

rand_pw = input('Would you like a random password? [y/n] ')

if rand_pw == 'y':
    print('Here is your random password: ' + random.choice(pw_lst))

enter_pw = input('Enter your password: ')
confirm_pw = input('Enter your password again: ')

if enter_pw == confirm_pw:
    print('\n Your passwords match.')
else:
    print('Your paswords do not match.')

if enter_pw != confirm_pw: 
    print('The program will now close. \n')
    sys.exit(0)

print('\n {} \n {} \n {} \n'.format(enter_name, enter_email, enter_pw))

account_confirm = input('Is this correct? [y/n]')

if account_confirm == 'n':
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
