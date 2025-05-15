# variable for numbers in passcode
numbers_and_characters = "1234567890!@#$%^&*"
# greeting to explain purpose
print("Hi! This is a password strength tester! To strengthen your password we recommend using over 8 characters and at least one number or special character ({})." .format(numbers_and_characters))
# prompt for password input
password = input("Please enter your password!")
# strips password of unneeded spaces
password.strip()
# checks if password length is over 8 characters and prints feedback
if len(password) <8:
    print("Your password is too short! To add strength make your password over 8 characters!")
# checks if password length is over 8 characters and has a number/special character in it and prints feedback
elif any(i in numbers_and_characters for i in password) and len(password) >=8:
    print("Well done! Your password is extra strong and secure!")
# if password is over 8 characters but does not have a number/special character in it this prints feedback
else :
    print("Your password is strong! To make it stronger add numbers and/or special characters!")
# reassures users that their password will not be stored
print("Your password will now be deleted from our data storage")
# deletes user's password
del(password)
