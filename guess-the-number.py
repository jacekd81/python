import random as rnd


def read_a_int():
    try:
        Integer = int(input())
    except ValueError:
        print ('Use integer numbers only!')
        return read_a_int()
    return Integer

# Init
SecretNumber = int (rnd.randrange(0,100))
Tries = int(0)
print ('Guess the secret number from 0 to 100')

# Main loop
GuessNumber = read_a_int()
while GuessNumber != SecretNumber:
    if GuessNumber < SecretNumber:
        print ('The secret number is higher!\nTry again')
        Tries += 1 
    elif GuessNumber > SecretNumber:
        print ('The secret number is smaller!\nTry again')
        Tries += 1 
    else:    
        break

    GuessNumber = read_a_int()


# End
Tries += 1
print('You got it!\nThe secret number is', SecretNumber,'\nYou got this after',Tries,'guesses')