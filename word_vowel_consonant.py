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
    #Step 3: Count number of vowels and consonants
    #add global variable for consonant and vowel
    vowels = 0
    consonants =0
    for i in user_input_:
        if(i == 'a'or i == 'e'or i == 'i'or i == 'o'or i == 'u' or
            i == 'A'or i == 'E'or i == 'I'or i == 'O'or i == 'U' ):
           vowels=vowels+1 #vowel is incremented by 1
#Display
    print (f"The number of words in the sentence is {number_words}")
    print (f"The number of vowels in the sentence is {vowels}")

getSentence()

