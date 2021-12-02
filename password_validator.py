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
print ("\nWelcome to Password Validator")
name = input ("\nWhat is your name? ")
print (f"\nHi {name}! This program will evaluate your password if it is valid or not.")
print ("\nHere are the following criteria:") 
print ("\nA. Greater than 15 letters \nB. Have at least one capital letter\nC. Have at least one number\nD. Have at least one special character (!@#$%^&*()_+ etc.)")


#Step 1: Ask password from user
def getPassword():
    password_= input("\nTo continue, please enter your password below.\n--> ")
    return password_

#Step 2: Loop each through each character of input
def test(passwordA):

#Variables for initial numbers:
    lowercase =0 
    uppercase = 0
    digit = 0
    specialchar =0 

    for i in passwordA:
        if (i>='a' and i<='z'): #counting the letters in password
            lowercase = lowercase +1
        elif (i>='A' and i<='Z'):
            uppercase = uppercase +1
        elif i.isdigit ():
            digit = digit +1 
        else:
            specialchar = specialchar +1

    letters = uppercase + lowercase   #(for total letters)
    
#Step 3: Conditions for the password to be valid
         #a              #b                #c             #d
    if letters >15 and uppercase >=1 and digit >=1 and specialchar >=1:
        print ("\nYour password is VALID\n")
    elif letters <=15 and uppercase >=1 and digit >=1 and specialchar >=1:
        print ("\nYour password is INVALID. Make sure that it has more than 15 letters.\n")
    elif letters >15 and uppercase == 0 and digit >=1 and specialchar >=1:
        print ("\nYour password is INVALID. Make sure that it has at least one capital letter.\n")
    else:
        print ("\nInvalid password\n")

password = getPassword()
test (password)