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
def test(passwordA):

#Variables for initial numbers:

    lowercase =0 
    uppercase = 0
    for i in passwordA:
        if (i>='a' and i<='z'): #counting the letters in password
            lowercase = lowercase +1
        elif (i>='A' and i<='Z'):
            uppercase = uppercase +1
#Step 3: Put condition for a. password must have greater than 15 letters
#Step 4: Put condition for b. Have at least one capital letter
#Step 5: Put condition for c. Have at least one number
#Step 6: Put condition for d. Have atleast one special i
#display overall
    letters = uppercase + lowercase
    print (letters)


password = getPassword()
test (password)