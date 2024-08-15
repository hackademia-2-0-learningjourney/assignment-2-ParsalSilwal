'''
Task 3: WAP that first gives 2 options: 
1. Sign up 
2. Sign in 
when 1 is pressed user needs to provide following information 
1. Username, 2. Password, 3. Mobile number 
All this information is saved in a file every time a new user signs up the same file is updated 
(hint Append over the same file)
when 2 is pressed 
User needs to provide username and password 
this username and password is checked with username and password in the database
if matched: 
welcome to the device and show their phone number 
else: 
terminate the program saying incorrect credentials 
Do it using json files, save everything to json and load from json
'''
#solution:
import json
import os

# Check if the JSON file exists, if not, create an empty dictionary in it
if not os.path.exists('login.json'):
    with open('login.json', 'w') as f:
        json.dump({}, f)

choice = int(input('Enter 1 to sign up and 2 to sign in:'))

while True:
    if choice == 1:
        # Sign Up
        user_name = input('Enter username: ')
        password = input('Enter password: ')
        mobile_number = input('Enter mobile number: ')

        # Load existing data
        with open('login.json', 'r') as f:
            data = json.load(f)

        # Update the data with the new user information
        data[user_name] = {'password': password, 'mobile_number': mobile_number}

        # Write the updated data back to the file
        with open('login.json', 'w') as f:
            json.dump(data, f)

        print('User signed up successfully!')
        choice = int(input('Enter 1 to sign up, 2 to sign in, and 3 to exit: '))

    elif choice == 2:
        # Sign In
        user_name = input('Enter username: ')
        password = input('Enter password: ')

        # Load existing data
        with open('login.json', 'r') as f:
            data = json.load(f)

        # Check if the username exists and the password matches
        if user_name in data and data[user_name]['password'] == password:
            print('Welcome to the device')
            print('Your mobile number is:', data[user_name]['mobile_number'])
        else:
            print('Incorrect credentials')

        choice = int(input('Enter 1 to sign up, 2 to sign in, and 3 to exit: '))

    elif choice == 3:
        print('Exiting the program')
        break

    else:
        print('Invalid choice')
        break

