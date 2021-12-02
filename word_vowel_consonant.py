#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8
name= input("\nWelcome! What is your name? ")
print (f"\nHi {name}! This program will look into your sentence. It will help you count words, vowels, and consonants.\n")
#Step 1: Ask user to input a sentence
def getSentence ():
    user_input_ = input ("To continue, please Enter your sentence below.\n-->")
#Step 2: Count number of words, store
    words = user_input_.split()
    number_words = len (words)
    #Step 3: Count number of vowels and consonants

    #Initial number for vowels and consonants
    vowels = 0
    consonants =0
    for i in user_input_:
        if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or #lower case vowel
            i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ): #upper case vowel
            vowels=vowels+1 #vowel is incremented by 1
        else: 
            consonants= consonants +1 #consonant is incremented by 1
            if (i == " " or i == ".") or (i== "!" or i == ",") or (i== "?" or i== "-") or (i== "'" or ";") or (i== ":" or i== "/"):
                consonants= consonants -1
            #It is to minus spaces and most commonly used punctuation marks in the sentence. 
#Display
    
    print (f"\nThe number of words in the sentence is {number_words}")
    print (f"The number of vowels in the sentence is {vowels}")
    print (f"The number of consonants in the sentence is {consonants} \n")

getSentence()

