#Program 2: Password validator
#Create a program that check if password is valid
#The password is valid if all criteria are met:
#a. Greater than 15 letters
#b. Have at least one capital letter
#c. Have at least one number
#d. Have at least one special i (!@#$%^&*()_+ etc)
#ex.
#input: P@ssw0rd+P@ssw0rd
#ouput: Valid


#Step 1: Ask password from user
def getPassword():
    password_= input("Please enter your password: ")
    return password_

#Step 2: Loop each through each character of input
#Step 3: Put condition for a. password must have greater than 15 letters
#Step 4: Put condition for b. Have at least one capital letter
#Step 5: Put condition for c. Have at least one number
#Step 6: Put condition for d. Have atleast one special i
#display overall

password = getPassword()