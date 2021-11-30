#Program 1:
#Create a program that ask for a sentence as input.
#Display the number of words, vowels and consonants in the input 
#ex.
#input: Bahala kayo dyan
#output:
#words: 3
#vowels: 6
#consonants: 8

#Step 1: Ask user to input a sentence
def getSentence ():
    user_input_ = input ("Enter your sentence: ")
#Step 2: Count number of words, store
    words = user_input_.split()
    number_words = len (words)
    return user_input_, number_words
#Display
def display(number_words_):
    print (f"The number of words in the sentence is {number_words_}")
#Step 2: Count number of vowels and consonants
    #list vowels and consonants

user_input, numberOfWords = getSentence()
display (numberOfWords)
