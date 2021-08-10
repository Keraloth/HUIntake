#Create a static dictionary with a number of users and with the following values: First name, Last name, Email address,Password
#Ask the user for: Email address, Password
#Loop (for()) through the dictionary and if (if()) the user is found print the following: 
    # Hello, first name last name you have successfully logged in ; 
    # Notify the user if the password and email address are wrong ; 
    # Additional challenge: if you want the program to keep asking for a username and password when the combination is wrong, you will need a while() loop.
# Save the file as assignment03yourlastname.py 

users = {
    1: {"first_name" : "Denise", "last_name" : "van Doorn", "email_address": "denise-vandoorn@hotmail.nl", "password": "denisevdoorn"},
    2: {"first_name" : "Melissa", "last_name" : "van Doorn", "email_address": "melissa@hotmail.nl", "password": "melissa1"},
    3: {"first_name" : "Jan", "last_name" : "van Doorn", "email_address": "jan@hotmail.nl", "password": "jan1"},
    4: {"first_name" : "Marjolein", "last_name" : "van Doorn", "email_address": "marjolein@hotmail.nl", "password": "marjolein1"},
    5: {"first_name" : "Harley", "last_name" : "van Doorn", "email_address": "harley@hotmail.nl", "password": "harley1"},
    6: {"first_name" : "Finn", "last_name" : "van Doorn", "email_address": "finn@hotmail.nl", "password": "finn1"},
}

#print ("Hello, can you fill in your email and password?")
#input("email_adress")
#dictionary key, value. Checken of een key bestaat. ask key in c#. get key/has key. python, dictionary has key.

email_addres_input = input("what is your email address? ")
password_input = input ("What is your password? ")

for value,key, in users.items():
    if email_addres_input == value ():
        print(value["first_name"])

#for password_input in users.items():
    
