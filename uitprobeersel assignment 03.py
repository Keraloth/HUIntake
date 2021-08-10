email = input("What's your e-mail?")
password = input("What's the password?")

email_input = input ("Fill in your e-mail")
password_input = input ("Fill in your password")

while email_input != email:
    print("email is incorrect. Try again")
    email_input = input ("Fill in your email")
while password_input != password:
    print("password is incorrect. Try again")
    password_input = input ("Fill in your password")

if email_input == email:
    print ("That's correct, Welcome", username)
