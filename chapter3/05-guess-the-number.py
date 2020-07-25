

import random

def random_Number():
    return random.randint(1,20)

def Guess():
    print('Take a guess')
    Guess = Guess(int(input()))
    if guess != random:
        print("Nope! Enter another guess")
        Guess = Guess(int(input()))
    elif guess == random:
        print("Congrats!")

   

print('I am thinking of a number between 1 and 20.')

random = random_Number()
print(random)
Guess()




      
