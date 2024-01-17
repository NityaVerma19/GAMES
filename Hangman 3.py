# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 16:50:51 2023

@author: DELL
"""

import random

print("Welcome to Hangman!\n ")

print("""Goal: Save the guy from dying by guessing the word
      
Instructions: Choose a topic and try to guess the word related to the topic by guessing one letter at a time. 
      """)

#---------------------------------LAYOUT OF THE GAME----------------------------------------#

Layout = [""" 
          +-----+
                +
                +
                +
                +
            ========
          """,""""
          +-----+
          O     +
                +
                +
                +
            ========          
          """,""" 
          +-----+
          O     +
          |     +
                +
                +
            ========             
          """,""""
          +-----+
          O     +
         /|     +
                +
                +
            ========           
          ""","""
          +-----+
          O     +
         /|\    +
                +
                +
            ========                
          ""","""
          +-----+
          O     +
         /|\    +
           \    +
                +
            ========  
            ""","""
          +-----+
          O     +
         /|\    +
         / \    +
                +
            ========              
         """ ]
         
         
         
         
    
print("Choose a topic among the following")
print("""         1 - Country Names
         2 - Fruits
         3 - Animals
         4 - Programming
         5 - Random
      """)
 
topic = int(input("Enter the number corresponding to the topic "))    
  

Country_names =[ "AFGHANISTAN","ALGERIA","ARGENTINA","AUSTRALIA","BANGLADESH","BELGIUM","BHUTAN","BRAZIL","CANADA","CHILE","CHINA","DENMARK","EGYPT","ETHIOPIA","FIJI","FINLAND","FRANCE","GERMANY","GREECE","HUNGARY","ICELAND"
"INDIA","INDONESIA","IRAN","IRAQ","IRELAND","ITALY","ISRAEL","JAPAN","KENYA","KUWAIT","MEXICO","MOROCCO","NEPAL","NEW ZEALAND","NORTH KOREA","NORWAY","PAKISTAN","PHILIPPINES","RUSSIA","SINGAPORE","SOUTH AFRICA","SOUTH KOREA","SPAIN","SRI LANKA","SWEDEN"]
Fruits = ["APPLE", "GRAPES","KIWI","ORANGE","BANANA","CHERRY","PINEAPPLE","CRANBERRY","BLACKCURRENT","PLUM","WATERMELON","MUSK MELON","GUAVA","STRAWBERRY","MANGO","PEAR","PAPAYA","LYCHEE","FIG","POMEGRANATE"]

Animals  = ["LION","BEAR","ELEPHANT","TIGER","CROCODILE","ALLIAGTOR","MONKEY","GIRAFFE","ANTELOPE","DEER","DUCK","HORSE","ORANGUTAN","FLAMINGO","PENGUIN","OSTRICH","ZEBRA","COBRA","CHIMPANZEE","GORILLA"]

Programming = [ "ALGORITHM",
"VARIABLE",
"FUNCTION",
"LOOP",
"CONDITIONAL",
"INHERITANCE",
"CLASS",
"INTERFACE",
"DEBUGGING",
"COMPILER",
"SYNTAX",
"DATABASE",
"ARRAY",
"POINTER",
"ABSTRACTION",
"POLYMORPHISM",
"ENCAPSULATION",
"STACK",
"QUEUE",
"RECURSION"]

Random_obj =["CHAIR",
"KEYBOARD",
"UMBRELLA",
"CLOCK",
"BICYCLE",
"CAMERA",
"MIRROR",
"SCISSORS",
"BOOK",
"LAMP",
"SHOES",
"PENCIL",
"GLASSES",
"VASE",
"REMOTE",
"RING",
"WALLET",
"COFFEE_MUG",
"TABLET",
"BACKPACK"]


def secret_word(topic):
    global word
    if topic == 1:
        
        random.shuffle(Country_names)
        Country_names
        word = random.choice(Country_names)

    elif topic == 2:
            
        random.shuffle(Fruits)
        Fruits
        word = random.choice(Fruits)
        

            
    elif topic == 3:
            
        random.shuffle(Animals)
        Animals
        word = random.choice(Animals)

                    
    elif topic == 4:
            
        random.shuffle(Programming)
        Programming
        word = random.choice(Programming)
   
    elif topic == 5:
            
        random.shuffle(Random_obj)
        Random_obj
        word = random.choice(Random_obj)
 
        
    else:
        print("Please choose a topic")


secret_word(topic)
correct_letters = " "
missed_letter = " "




def get_letter(l):
    while True:
        guess = input("Guess a letter ").capitalize()
        if len(guess)!=1:
            print("Please choose one letter")
        elif guess in l:
            print("You have already chose this letter. Try again!")
    
        elif guess not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            print("Please choose a LETTER")
        
        else:
            return guess

guess = get_letter(correct_letters+missed_letter)


if guess in word:
    correct_letters = correct_letters+guess
else:
    missed_letter = missed_letter + guess
    print(missed_letter)
    
def board():
    print(Layout[len(missed_letter)])
    print()
    blank = "_"*len(word)
    print(blank)
    
    for i in range(len(word)):
        if word[i] in correct_letters:
            blank = blank[:i] + word[i] + blank[i+1:]
            
    for letter in blank:
        print(letter,end=" ")

gameIsplaying = True

    
        
while gameIsplaying:
    board()
    guess = get_letter(correct_letters + missed_letter)

    if guess in word:
        correct_letters = correct_letters + guess
        found_all_letters = all(letter in correct_letters for letter in word)
        if found_all_letters:
            print("Congratulations! You guessed the word:", word)
            gameIsplaying = False
    else:
        missed_letter = missed_letter + guess
        print("Missed letters:", missed_letter)

        if len(missed_letter) == len(Layout) - 1:
            board()
            print("Sorry, you've run out of guesses. The word was:", word)
            gameIsplaying = False


