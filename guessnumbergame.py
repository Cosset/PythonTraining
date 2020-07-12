# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 10.')
secretNumber = random.randint(1, 10)

#print('DEBUG: Secret number is ' + str(secretNumber) ) , for debug purposes

for guessesTaken in range(1, 6):
    print('Take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess
        
if guess == secretNumber:
    print ('Good job, ' + name + '! You guessed the correct number in ' + str(guessesTaken) + ' trys!' )
else:
    print('Sorry, the number I was thinking of was ' + str(secretNumber) + '.')
