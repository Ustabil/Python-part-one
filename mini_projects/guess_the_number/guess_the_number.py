# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

#Codeskulptor URL: http://www.codeskulptor.org/#user40_06oB2cbaGvb17j2.py

import simplegui
import random

current_game = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here

    # remove this when you add your code    
    global secret_number
    if current_game == 0:
        range100()
    elif current_game == 1:
        range1000()
    else:
        print "Something bad happened..."



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    
    # remove this when you add your code    
    global secret_number
    global allowed_Guesses
    global current_game

    current_game = 0
    allowed_Guesses = 7
    secret_number = random.randrange(0, 100)

    print "\nGuess a number between 0 and 100, within", allowed_Guesses, "guesses!"

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global allowed_Guesses
    global current_game

    current_game = 1

    allowed_Guesses = 10
    secret_number = random.randrange(0, 1000)

    print "\nGuess a number between 0 and 1000, within", allowed_Guesses, "guesses!"
    
def input_guess(guess):
    # main game logic goes here	
    global allowed_Guesses
    guess = int(guess)
    allowed_Guesses -= 1
    # remove this when you add your code
    print "\nGuess was", guess
    if guess == secret_number:
        print "Correct!"
        new_game()
    elif allowed_Guesses == 0:
        print "No more guesses!"
        new_game()
    elif guess > secret_number:
        print "Lower!"       
        print "Remaining guesses:", allowed_Guesses
    elif guess < secret_number:
        print "Higher!"
        print "Remaining guesses:", allowed_Guesses
    else:
        print "Something weird happened o.O"

    
# create frame
frame = simplegui.create_frame('Guess the Number', 200, 200)



# register event handlers for control elements and start frame
button1 = frame.add_button('Range is 0 - 100', range100, 200)
button2 = frame.add_button('Range is 0 - 1000', range1000, 200)
inp = frame.add_input('Enter a guess:', input_guess, 200)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
