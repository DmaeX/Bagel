import random

NUM_DIGITS = 3
MAX_GUESES = 10

def main():
    print('''Bagels, a deductive logic game. 
    
I am thinking of a number {}-digit number with no repeated digits. 
Try to guess what it is. Here are some clues: 
When I say:    That means:
    Pico       One digit is correct but in the wrong position.
    Fermi      One digit is correct and in the right position.
    Bagels     No digit is correct. 
    
For example, if the secret number is 248 and your guess was 843, the clues would be Fermi pico'''.format(NUM_DIGITS))

    while True: 
        # Stores the secret number the players needs to guess
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print('You have {} gueses to get it.'.format(MAX_GUESES))

        numGuesses = 1
        while numGuesses <= MAX_GUESES:
            guess = ''
            # Keeps looping until they enter a valid guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input ('> ')

            # Gets the clues 
            clues = getClues(guess, secretNum)
            print(clues)
            # Adds the number of guesses
            numGuesses +=1

            # The number they guessed was correct so they break out of the loop
            if guess == secretNum: 
                break 
            # If the player has reached their maximum guesses. 
            if numGuesses > MAX_GUESES:
                print(get_friendly_loss_message())
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again(yes or no)')
        if not input('< ').lower().startswith('y'):
            break 

    Print('Thanks for playing!')


def getSecretNum():
    # Creates a list of digits 0 to 9
    numbers = list('0123456789')
    # Shuffles them into random order 
    random.shuffle(numbers) 

    # Gets the first NUM_DIGITS in the list for the secret number
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess: str, secretNum: str):
    
    if guess == secretNum:
        return "IGHT BET 🥶"

    clues = []

    for i in range(len(guess)): 
        if guess[i] == secretNum[i]:
            clues.append('Fermi')

        elif guess[i] in secretNum:
            clues.append('Pico')

    if len(clues) == 0: 
        return 'Bagels'
    else: 
        clues.sort()
        return ''.join(clues)

def get_friendly_loss_message():
    messages = [
        'D for do not even come home 😭',
        'Is your brain there? 🤣',
        'Silly you, go play again but with 1 digit 😤',
        'Go play chess 🤓',
        'THATS UNFORTUNATE 😤'
    ]

    random.shuffle(messages)

    return messages[0]

main()



