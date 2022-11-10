"""A number-guessing game."""
#imported random fucntion from python library 
import random
#sudo code 
'''greet player
get player name
choose random number between 1 and 100
repeat forever:
    get guess
    if guess is incorrect:
        give hint
        increase number of guesses
    else:
        congratulate player
 '''

#players name 
name= input('\nwelcome, what is your name?\n')
#assign the variable guess to -1 to instantiate the variable globally.
#use -1 or anything outside of the range (0,101) so that we always enter the while loop at least once becasuse if the number generated is 0 otherwise it will skip the loop
guess= -1     

#we set our counter to 0 to help us initialize the counter 
counter=0
#using the random function we imported to pick a random number 
number= random.randint(0,101)

#friednly greeting that prints the players name and we are using interpolation with the variable name 
print(f'\nhey there, {name}\n')

#creating game play by using the input in a loop

#while the players guess is not equal to the number, kick off the below set of instructions 
while guess != number: 

    #here we are parsing the number into an interger 
    guess= int(input('\nwhat is your guess? \n'))
    #we add a conditional that prints the string below if the players guess is higher than the random number 
    if number < guess:
        print('\nyou are too high, try again\n')
    #we add a conditional that prints the string below if the players guess is lower than the random number 
    elif number > guess:
        print('\nyou are too low, try again\n')
    #we set a counter that will help us track the number of tries (guesses)    
    counter= counter +1

    #if the players guess is equal to the random number that was generated than the below string will print 
    if guess == number:
        #here we are using interpolation in our string for the variable counter
        print(f'\ncongrats you got it in {counter} tries\n')
  
    





